import os
import re
from html.parser import HTMLParser

class ParameterParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parameters = []
        self.current_page = None
        self.in_param_header = False
        self.in_param_label = False
        self.in_param_name = False
        self.in_param_description = False
        self.in_param_group_description = False
        self.in_page_heading = False
        self.current_param = {}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'h3' and 'class' in attrs_dict and 'page-heading' in attrs_dict['class']:
            self.in_page_heading = True
        elif tag == 'div' and 'class' in attrs_dict and 'param-header' in attrs_dict['class']:
            self.in_param_header = True
            self.current_param = {}
        elif tag == 'span' and 'class' in attrs_dict:
            if 'param-label' in attrs_dict['class']:
                self.in_param_label = True
            elif 'param-name' in attrs_dict['class']:
                self.in_param_name = True
            elif 'param-description' in attrs_dict['class']:
                self.in_param_description = True
            elif 'param-group-description' in attrs_dict['class']:
                self.in_param_group_description = True

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_page_heading = False
        elif tag == 'div':
            if self.in_param_header and self.current_param.get('name'):
                self.current_param['page'] = self.current_page
                self.parameters.append(self.current_param.copy())
            self.in_param_header = False
        elif tag == 'span':
            self.in_param_label = False
            self.in_param_name = False
            self.in_param_description = False
            self.in_param_group_description = False

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return

        if self.in_page_heading and data.startswith('Page:'):
            self.current_page = data.replace('Page:', '').strip()
        elif self.in_param_label:
            self.current_param['label'] = data
        elif self.in_param_name:
            self.current_param['name'] = data
        elif self.in_param_description or self.in_param_group_description:
            self.current_param['description'] = data

def shorten_description(desc, max_len=80):
    """Shorten description to ~80 chars while keeping key information."""
    if len(desc) <= max_len:
        return desc

    # Try to cut at sentence boundary
    sentences = desc.split('. ')
    if len(sentences[0]) <= max_len:
        return sentences[0] + '.'

    # Cut at word boundary
    words = desc.split()
    result = []
    length = 0
    for word in words:
        if length + len(word) + 1 > max_len:
            break
        result.append(word)
        length += len(word) + 1

    return ' '.join(result) + ('.' if not result[-1].endswith('.') else '')

def generate_help_script(operator_folder, operator_name):
    """Generate help script for an operator."""
    html_file = os.path.join(operator_folder, 'index.html')

    if not os.path.exists(html_file):
        return None

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = ParameterParser()
    parser.feed(html_content)

    if not parser.parameters:
        return None

    # Generate script
    script_lines = [
        f"# TouchDesigner Python Script - Set {operator_name.title()} Parameter Help Text",
        "",
        "op_name = target",
        ""
    ]

    # Group by page
    pages = {}
    for param in parser.parameters:
        page = param.get('page', 'Main')
        if page not in pages:
            pages[page] = []
        pages[page].append(param)

    # Write parameters by page
    for page, params in pages.items():
        script_lines.append(f"# Page: {page}")
        for param in params:
            name = param['name']
            desc = param.get('description', '')
            if desc:
                desc = shorten_description(desc)
                script_lines.append(f'op_name.par.{name}.help = "{desc}"')
        script_lines.append("")

    script_lines.append(f'print("{operator_name.title()} parameter help text updated successfully!")')
    script_lines.append("")

    return '\n'.join(script_lines)

# Find all operator folders
operators = []
for root, dirs, files in os.walk('docs/operators'):
    if 'index.html' in files:
        operators.append(root)

print(f"Found {len(operators)} operators")

# Generate help scripts
created = 0
for op_folder in operators:
    op_name = os.path.basename(op_folder)
    script_content = generate_help_script(op_folder, op_name)

    if script_content:
        script_path = os.path.join(op_folder, 'set_help.py')
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        print(f"Created: {script_path}")
        created += 1
    else:
        print(f"Skipped: {op_folder} (no parameters found)")

print(f"\nCreated {created} help scripts!")
