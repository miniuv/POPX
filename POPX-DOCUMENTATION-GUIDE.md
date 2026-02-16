# POPX Documentation - Comprehensive Instructions

Complete guide for updating POPX operator documentation pages, set_help.py scripts, release notes, search index, sidebar, and table of contents.

---

## 1. OPERATOR PAGE STRUCTURE (index.html)

Each operator page lives at `docs/operators/{category}/{operator-name}/index.html`.

### Full Page Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OperatorName | POPX</title>
  <meta name="description" content="Brief description of the operator.">
  <link rel="icon" type="image/png" href="../../../../media/popx-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../../assets/css/style.css">
</head>
<body>
  <script>
    if (performance.navigation.type === 1) {
      document.body.style.opacity = '1';
    } else {
      document.body.classList.add('page-transitioning');
    }
  </script>
  <div id="navbar-container"></div>

  <div class="page-layout">
    <div id="mobile-menu-container"></div>
    <div id="sidebar-container"></div>

    <main class="main-content">
      <h1>OperatorName <span class="operator-version">v1.2.0</span></h1>

      <!-- Summary Section -->
      <section id="summary">
        <h2>Summary</h2>
        <p>Description paragraphs...</p>
      </section>

      <!-- Parameters Section -->
      <section id="parameters">
        <h2>Parameters</h2>

        <h3 id="page-operatorname" class="page-heading">Page: OperatorName</h3>
        <!-- parameter-item and param-group elements here -->

        <hr class="section-divider">

        <h3 id="page-common" class="page-heading">Page: Common</h3>
        <!-- Common page parameters -->
      </section>

      <!-- Inputs Section -->
      <section id="inputs">
        <h2>Inputs</h2>
        <!-- Input items with param-header-inline -->
      </section>

      <!-- Outputs Section -->
      <section id="outputs">
        <h2>Outputs</h2>
        <!-- Output items with param-header-inline -->
      </section>

      <!-- Navigation -->
      <nav class="page-navigation">
        <a href="../prev-operator/" class="nav-button prev">Previous</a>
        <a href="../next-operator/" class="nav-button next">Next</a>
      </nav>
    </main>

    <!-- Table of Contents -->
    <aside class="toc">
      <h4>Contents</h4>
      <ul>
        <li><a href="#summary">Summary</a></li>
        <li><a href="#parameters">Parameters</a>
          <ul>
            <li><a href="#page-operatorname">Page: OperatorName</a></li>
            <li><a href="#page-common">Page: Common</a></li>
          </ul>
        </li>
        <li><a href="#inputs">Inputs</a></li>
        <li><a href="#outputs">Outputs</a></li>
      </ul>
    </aside>
  </div>

  <div id="menu-overlay-container"></div>

  <script src="../../../../assets/js/component-loader.js"></script>
  <script src="../../../../assets/js/script.js"></script>
</body>
</html>
```

---

## 2. PARAMETER HTML PATTERNS

### 2a. Simple Parameter (Toggle, Float, Int, Pulse, String with size 1)

```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Human Readable Label</span>
    <span class="param-name">Parametername</span>
    <span class="param-separator">–</span>
    <span class="param-description">Description text.</span>
  </div>
</div>
```

### 2b. Parameter Group (Menu, Vec2, Vec3, RGB, RGBA/Size 4)

Used for any multi-value parameter: menus with options, vector components, color channels.

**CRITICAL**: ALL param-groups MUST include `<span class="param-toggle"></span>` AND a second `<span class="param-separator">–</span>` between the toggle and description.

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Parameter Label</span>
    <span class="param-name">Parametername</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Description text.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Sub Label</span>
      <span class="param-name">subname</span>
    </div>
    <!-- more sub-params -->
  </div>
</div>
```

### 2c. Menu Parameter (with named options)

Menu options use lowercase `param-name` values matching the menuNames from TouchDesigner.

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Solver Mode</span>
    <span class="param-name">Solvermode</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Switches between Simple and Advect modes.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Simple</span>
      <span class="param-name">simple</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Advect</span>
      <span class="param-name">advect</span>
    </div>
  </div>
</div>
```

### 2d. Vec3 Parameter (XYZ components)

Sub-param names use the base name + x/y/z suffix. Labels repeat the parent label.

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Translate</span>
    <span class="param-name">T</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Translation in world space.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Translate</span>
      <span class="param-name">Tx</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Translate</span>
      <span class="param-name">Ty</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Translate</span>
      <span class="param-name">Tz</span>
    </div>
  </div>
</div>
```

### 2e. RGB Parameter (Color components)

Sub-param names use base name + r/g/b suffix.

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Base Color</span>
    <span class="param-name">Basecolor</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Diffuse albedo color.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Base Color</span>
      <span class="param-name">Basecolorr</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Base Color</span>
      <span class="param-name">Basecolorg</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Base Color</span>
      <span class="param-name">Basecolorb</span>
    </div>
  </div>
</div>
```

### 2f. Size 4 Parameter (RGBA-like, numbered 1-4)

Sub-param names use base name + 1/2/3/4 suffix.

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Channel Mask (RGBA)</span>
    <span class="param-name">Channelmask</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Selects which RGBA channels are sampled.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Channel Mask (RGBA)</span>
      <span class="param-name">Channelmask1</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Channel Mask (RGBA)</span>
      <span class="param-name">Channelmask2</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Channel Mask (RGBA)</span>
      <span class="param-name">Channelmask3</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Channel Mask (RGBA)</span>
      <span class="param-name">Channelmask4</span>
    </div>
  </div>
</div>
```

### 2g. Inputs/Outputs Format

Uses `param-header-inline` class instead of `param-header`.

```html
<section id="inputs">
  <h2>Inputs</h2>
  <div class="parameter-item">
    <div class="param-header param-header-inline">
      <span class="param-label">Input 0</span>
      <span class="param-name">POP</span>
      <span class="param-separator">–</span>
      <span class="param-text">POPX_in1</span>
    </div>
  </div>
</section>

<section id="outputs">
  <h2>Outputs</h2>
  <div class="parameter-item">
    <div class="param-header param-header-inline">
      <span class="param-label">Output 0</span>
      <span class="param-name">POP</span>
      <span class="param-separator">–</span>
      <span class="param-text">POPX_out1</span>
    </div>
  </div>
</section>
```

### 2h. Page Separators

Between parameter pages, use:
```html
<hr class="section-divider">

<h3 id="page-pagename" class="page-heading">Page: PageName</h3>
```

The `id` is lowercase hyphenated: `page-flow`, `page-common`, `page-path-tracer`.

---

## 3. JSON PARAMETER EXPORT INTERPRETATION

When the user provides a JSON export from TouchDesigner, map these fields:

| JSON Field | HTML Element | Notes |
|---|---|---|
| `label` | `param-label` | Human-readable name |
| `name` | `param-name` | Code identifier (camelCase) |
| `style` | Determines structure | See rules below |
| `help` | `param-description` or `param-group-description` | Can be empty |
| `size` | Number of sub-components | 1=simple, 2+=group |
| `menuNames` / `menuLabels` | Sub-params | For Menu style |

### Style-to-HTML Mapping Rules

| JSON style | size | HTML Pattern |
|---|---|---|
| `"Header"` | any | **NOT RENDERED** — headers are not shown in docs |
| `"Toggle"`, `"Float"`, `"Int"`, `"Pulse"`, `"Str"`, `"OP"`, `"TOP"`, `"CHOP"`, `"DAT"`, `"COMP"` | 1 | `parameter-item` |
| `"Float"`, `"Int"` | 2 | `param-group` with x/y sub-params |
| `"Float"`, `"Int"` | 3 | `param-group` with x/y/z sub-params |
| `"Float"`, `"Int"` | 4 | `param-group` with 1/2/3/4 sub-params |
| `"RGB"` | 3 | `param-group` with r/g/b sub-params |
| `"RGBA"` | 4 | `param-group` with r/g/b/a sub-params |
| `"Menu"` | 1 | `param-group` with menuNames/menuLabels as sub-params |

### Sub-param Naming Conventions

| Type | Base Name | Sub-param Names |
|---|---|---|
| Vec2 | `Param` | `Paramx`, `Paramy` |
| Vec3 | `Param` | `Paramx`, `Paramy`, `Paramz` |
| Size 4 (numbered) | `Param` | `Param1`, `Param2`, `Param3`, `Param4` |
| RGB | `Param` | `Paramr`, `Paramg`, `Paramb` |
| RGBA | `Param` | `Paramr`, `Paramg`, `Paramb`, `Parama` |
| Menu | `Param` | Use `menuNames` values (lowercase) |

---

## 4. SET_HELP.PY FILES

Each operator has a `set_help.py` file that mirrors the HTML descriptions into TouchDesigner parameter help text.

### Structure

```python
# TouchDesigner Python Script - Set OperatorName Parameter Help Text

op_name = target

# Page: PageName
op_name.par.Parametername.help = "Description text matching HTML."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("OperatorName parameter help text updated successfully!")
```

### Naming Rules for set_help.py

| Parameter Type | Help Target | Example |
|---|---|---|
| Simple (size 1) | `op_name.par.Name.help` | `op_name.par.Reset.help` |
| Vec3 | First component (x) | `op_name.par.Tx.help`, `op_name.par.Min1.help` |
| RGB | First component (r) | `op_name.par.Basecolorr.help` |
| Size 4 (numbered) | First component (1) | `op_name.par.Channelmask1.help`, `op_name.par.Fromlow1.help` |
| Menu | Base name | `op_name.par.Solvermode.help` |
| Vec3 (numbered) | First component (1) | `op_name.par.Min1.help` |

### Ordering

Parameters in set_help.py MUST follow the same page order as the HTML. Group by page with `# Page: PageName` comments.

---

## 5. RELEASE NOTES

Changes must be documented in TWO places:

### 5a. Plain Text (release_notes.txt)

```
Version 1.2.0 - Future Release
-------------------------------

NEW FEATURES

OperatorName:
  • Added ParameterLabel parameter for description
  • Changed ParameterLabel to menu with Option1 and Option2 options
  • Renamed OldLabel to NewLabel
  • Replaced OldPage page with new NewPage architecture
  • Removed ParameterLabel parameter
```

Categories (in order): `PERFORMANCE`, `NEW OPERATORS`, `NEW FEATURES`, `BUG FIXES`

### 5b. HTML (docs/release-notes/index.html)

Uses inline styles (no CSS classes). Each list item follows this pattern:

```html
<li style="position: relative; padding-left: 16px; margin-bottom: 6px; font-size: 13px; line-height: 1.6; color: var(--color-text-muted);">
  <span style="position: absolute; left: 0; color: var(--color-accent);">•</span>
  Added <strong style="color: var(--color-text);">Parameter Name</strong> parameter for description.
</li>
```

Operator heading:
```html
<div style="margin-bottom: 16px;">
  <h4 style="font-size: 13px; font-weight: 600; color: var(--color-text); margin-bottom: 8px; font-family: 'JetBrains Mono', monospace;">OperatorName</h4>
  <ul style="margin: 0; padding-left: 20px; list-style-type: none;">
    <!-- li items here -->
  </ul>
</div>
```

Section heading (NEW FEATURES, etc.):
```html
<div style="margin-top: 24px;">
  <h3 style="font-size: 15px; font-weight: 600; color: var(--color-accent); margin-bottom: 12px; letter-spacing: 0.5px;">NEW FEATURES</h3>
  <!-- operator divs here -->
</div>
```

---

## 6. SEARCH INDEX

Located in `assets/js/script.js` as a hardcoded array `searchIndex` (starts around line 918).

### Entry Format

```javascript
{
  title: 'OperatorName',
  path: 'docs/operators/category/operator-name/',
  type: 'Operator',
  category: 'CategoryName',  // Generators, Modifiers, Falloffs, Tools, Simulations
  sections: [
    { title: 'Summary', anchor: '#summary' },
    { title: 'Page: PageName', anchor: '#page-pagename', keywords: ['keyword1', 'keyword2'] },
    { title: 'Page: Common', anchor: '#page-common' },
    { title: 'Inputs', anchor: '#inputs' },
    { title: 'Outputs', anchor: '#outputs' }
  ]
}
```

### When to Update

- **New operator**: Add a new entry to the array in alphabetical order within its category
- **New page added to operator**: Add a new section entry with appropriate anchor and keywords
- **Page renamed**: Update the section title and anchor
- **Page removed**: Remove the section entry

### Anchor Naming

The `anchor` must match the `id` attribute on the `<h3>` page heading in HTML:
- `Page: Flow` → `#page-flow`
- `Page: Path Tracer` → `#page-path-tracer`
- `Page: Move Along Curve` → `#page-move-along-curve`

---

## 7. SIDEBAR

Located at `components/sidebar.html`. Operators are listed alphabetically within each subsection.

### When to Update

- **New operator**: Add a `<li><a href="docs/operators/category/operator-name/">Operator Name</a></li>` in alphabetical order
- **Operator removed**: Remove the `<li>` entry
- **Operator renamed**: Update the text and href

### Structure

```html
<div class="sidebar-subsection">
  <h4>CategoryName</h4>
  <div class="sidebar-subsection-content">
    <ul>
      <li><a href="docs/operators/category/operator-name/">Operator Name</a></li>
    </ul>
  </div>
</div>
```

Categories in sidebar order: Generators, Falloffs, Modifiers, Tools, Simulations.

---

## 8. TABLE OF CONTENTS (TOC)

Located within each operator page as `<aside class="toc">`. Must match the page sections.

### Template

```html
<aside class="toc">
  <h4>Contents</h4>
  <ul>
    <li><a href="#summary">Summary</a></li>
    <li><a href="#parameters">Parameters</a>
      <ul>
        <li><a href="#page-pagename">Page: PageName</a></li>
        <li><a href="#page-common">Page: Common</a></li>
      </ul>
    </li>
    <li><a href="#inputs">Inputs</a></li>
    <li><a href="#outputs">Outputs</a></li>
  </ul>
</aside>
```

### When to Update

- **New page**: Add `<li><a href="#page-newpage">Page: NewPage</a></li>` in correct order
- **Page renamed**: Update the text and anchor
- **Page removed**: Remove the `<li>` entry

---

## 9. VERSION TAG

Each operator page has a version tag in the `<h1>`:

```html
<h1>OperatorName <span class="operator-version">v1.2.0</span></h1>
```

CSS class defined in `assets/css/style.css`:
```css
.operator-version {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font-mono);
  background-color: rgba(184, 0, 58, 0.15);
  color: var(--color-accent);
  border: 1px solid rgba(184, 0, 58, 0.3);
  vertical-align: middle;
  margin-left: 12px;
  line-height: 1;
  letter-spacing: 0.02em;
}
```

---

## 10. COMMON PAGE PARAMETERS

Most operators share these Common page parameters:

```html
<h3 id="page-common" class="page-heading">Page: Common</h3>

<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Bypass</span>
    <span class="param-name">Bypass</span>
    <span class="param-separator">–</span>
    <span class="param-description">Pass through the first input to the output unchanged.</span>
  </div>
</div>

<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Free Extra GPU Memory</span>
    <span class="param-name">Freeextragpumem</span>
    <span class="param-separator">–</span>
    <span class="param-description">Free memory that has accumulated when output memory has grown and shrunk.</span>
  </div>
</div>

<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Render Primitives</span>
    <span class="param-name">Renderprimitives</span>
    <span class="param-separator">–</span>
    <span class="param-description">Toggles rendering of POPX Geometry or shows it as point instances only.</span>
  </div>
</div>

<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Convert to Point Primitives</span>
    <span class="param-name">Converttoptprim</span>
    <span class="param-separator">–</span>
    <span class="param-description">Converts points to primitive points when Render Primitives is toggled off.</span>
  </div>
</div>

<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">SRT / RST</span>
    <span class="param-name">Srtrst</span>
    <span class="param-separator">–</span>
    <span class="param-description">Sets the transform order when using POPX Geometry as built-in TouchDesigner instances.</span>
  </div>
</div>
```

Not all operators have all Common params. Some only have `Freeextragpumem`.

---

## 11. COLLISIONS PAGE ARCHITECTURE

DLG, Relax, and potentially other operators share a standardized Collisions page. This includes:

1. **Collision Type** menu (None, POP, Box, Plane, Sphere, Torus, 3D SDF, T3D, 2D SDF, T2D)
2. **Collision Damping**, **Solid**, **Project** toggles
3. **Collision POP**, **Collision Offset**
4. **Size** (Vec3), **Radius** (Vec3), **Corner Radius**
5. **Collison TOP** (note: typo in param name is intentional — matches TouchDesigner), **Use Custom Bounds**
6. **Lower Bounds** (Vec3), **Upper Bounds** (Vec3)
7. Transform: **Transform Order** (menu), **Rotate Order** (menu), **Translate** (Vec3), **Rotate** (Vec3), **Scale** (Vec3), **Pivot** (Vec3), **Uniform Scale**
8. **Display Geometry**, **Display Color** (RGB)

---

## 12. CHECKLIST — When Adding a New Operator

1. [ ] Create `docs/operators/{category}/{name}/index.html` with full page template
2. [ ] Create `docs/operators/{category}/{name}/set_help.py`
3. [ ] Add entry to `components/sidebar.html` (alphabetical order)
4. [ ] Add entry to `searchIndex` in `assets/js/script.js` (with sections and keywords)
5. [ ] Add release notes to `release_notes.txt` under NEW OPERATORS
6. [ ] Add release notes to `docs/release-notes/index.html`

## 13. CHECKLIST — When Updating Parameters on an Existing Operator

1. [ ] Update `index.html` — add/modify/remove/reorder parameter HTML
2. [ ] Update `set_help.py` — add/modify/remove help text entries
3. [ ] Update `release_notes.txt` — document changes
4. [ ] Update `docs/release-notes/index.html` — document changes
5. [ ] If pages were added/removed/renamed:
   - [ ] Update TOC in `index.html`
   - [ ] Update `searchIndex` sections in `assets/js/script.js`
