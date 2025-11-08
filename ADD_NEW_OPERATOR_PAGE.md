# Adding a New Operator Page

This guide provides a complete walkthrough for adding a new operator to the POPX documentation system, including parameter integration, navigation updates, and page structure.

## Table of Contents

1. [Creating a New Operator Page](#creating-a-new-operator-page)
2. [Overview](#overview)
3. [JSON Parameter Structure](#json-parameter-structure)
4. [HTML Parameter Structure](#html-parameter-structure)
5. [Parameter Types](#parameter-types)
6. [Integration Process](#integration-process)
7. [Examples](#examples)
8. [Best Practices](#best-practices)

---

## Creating a New Operator Page

This section provides a complete walkthrough for adding a new operator to the POPX documentation system. Follow these steps in order to ensure all navigation, search functionality, and page structure are properly integrated.

### Step 1: Create Directory Structure

Create a new directory for your operator in the appropriate category:

```
docs/operators/[category]/[operator-name]/
```

Categories include:
- `generators/` - For operators that create or generate geometry (Convert, Explode, Instancer, etc.)
- `falloffs/` - For operators that create falloff fields (Radial Falloff, Shape Falloff, etc.)
- `modifiers/` - For operators that modify geometry (Aim, Magnetize, Pivot, etc.)
- `tools/` - For utility operators (Attribute Manager, Voxelize, etc.)
- `simulations/` - For simulation solvers (FLIP Solver, SPH Solver, etc.)

Example:
```
docs/operators/modifiers/my-new-operator/
```

### Step 2: Create the HTML File

Create `index.html` inside your new operator directory. Start with the HTML boilerplate structure.

#### HTML Boilerplate Template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>POPX Docs | [Operator Name]</title>
  <meta name="description" content="[Brief description of what this operator does]">
  <link rel="icon" type="image/png" href="../../../../media/popx-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../../assets/css/style.css">
</head>
<body>
  <script>
    // Clean URL - remove index.html if present
    if (window.location.pathname.endsWith('/index.html')) {
      window.history.replaceState(null, '', window.location.pathname.replace('/index.html', '/'));
    }

    // Prevent flash during page transitions
    if (performance.navigation.type === 1) {
      // Page was reloaded, no transition needed
      document.body.style.opacity = '1';
    } else {
      // Normal navigation, start hidden for fade-in
      document.body.classList.add('page-transitioning');
    }
  </script>

  <!-- Top Navigation Bar -->
  <header class="top-bar">
    <div class="top-bar-logo-container">
      <a href="/" class="top-bar-logo">
        <img src="../../../../media/popx_logo_full_light.png" alt="POPX Docs" class="logo-light">
        <img src="../../../../media/popx_logo_full_dark.png" alt="POPX Docs" class="logo-dark">
      </a>
      <div class="logo-tagline">
        <div>POPs Extension</div>
        <div>for TouchDesigner</div>
      </div>
    </div>

    <!-- Search Bar (Desktop Only) -->
    <div class="top-bar-search">
      <div class="search-input-wrapper">
        <span class="search-icon">⌕</span>
        <input type="text" placeholder="Search" aria-label="Search">
      </div>
    </div>

    <!-- Theme Selector (Desktop Only) -->
    <div class="theme-selector">
      <button class="theme-selector-button" aria-label="Select theme">Dark</button>
      <div class="theme-selector-dropdown">
        <div class="theme-option selected" data-theme="dark">Dark</div>
        <div class="theme-option" data-theme="light">Light</div>
        <div class="theme-option" data-theme="auto">Auto</div>
      </div>
    </div>
  </header>

  <div class="page-layout">
    <!-- Mobile Menu Toggle -->
    <button class="mobile-menu-toggle" aria-label="Toggle menu">☰</button>

    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <!-- Copy sidebar from an existing operator page -->
      <!-- Make sure to add your new operator link in the appropriate section -->
    </aside>

    <!-- Main Content -->
    <main class="main-content">
      <article class="operator-page">
        <!-- Page content goes here -->
      </article>
    </main>

    <!-- Table of Contents -->
    <aside class="toc">
      <!-- TOC will be populated here -->
    </aside>
  </div>

  <!-- Mobile Menu Overlay -->
  <div class="menu-overlay"></div>

  <script src="../../../../assets/js/script.js"></script>
</body>
</html>
```

**Important:** Adjust the `../../../../` path depth based on your operator's location. Count the directory levels from your operator to the root:
- `docs/operators/category/operator/` = 4 levels = `../../../../`

### Step 3: Add Summary Section

Add the operator summary at the beginning of the main content:

```html
<article class="operator-page">
  <h1>[Operator Name]</h1>

  <section class="summary">
    <p>[1-2 sentences describing what this operator does and its primary use cases.]</p>
  </section>

  <!-- Rest of content follows -->
</article>
```

**Example:**
```html
<h1>Shape Falloff</h1>

<section class="summary">
  <p>Shape Falloff generates distance-based falloff values from geometric primitives. It creates smooth attenuation fields for controlling particle behavior, colors, and transformations based on proximity to shapes like spheres, boxes, and tori.</p>
</section>
```

### Step 4: Add Parameters Section

Following the JSON integration process (see [Integration Process](#integration-process) and [Parameter Types](#parameter-types)), add all operator parameters organized by pages:

```html
<section id="parameters" class="parameters">
  <h2>Parameters</h2>

  <!-- Page 1: [Page Name] -->
  <h3 class="page-heading">[Page Name]</h3>

  <!-- Add all parameters from this page here -->
  <!-- Follow the parameter structure guidelines below -->

  <hr class="section-divider">

  <!-- Page 2: [Page Name] -->
  <h3 class="page-heading">[Page Name]</h3>

  <!-- Add all parameters from this page here -->

  <!-- Continue for all pages -->
</section>
```

**Key Points:**
- Group parameters by their TouchDesigner page
- Use `<hr class="section-divider">` between pages
- Follow the [Parameter Types](#parameter-types) section for proper HTML structure
- Use `<div class="param-group">` for parameters with sub-parameters (Menu, Vec3, RGB, Vec2)
- Use `<div class="parameter-item">` for simple parameters (Float, Int, Toggle, etc.)

**Special Note for Falloff Operators:**
All Falloff operators (in `docs/operators/falloffs/`) must have **identical** parameter pages for:
- **Falloff Page** - Parameters controlling falloff behavior
- **Noise Page** - Parameters for adding noise to the falloff
- **Remap Page** - Parameters for remapping falloff values with curves/ramps

These three parameter pages should be copied exactly from existing Falloff operators (e.g., Shape Falloff, Radial Falloff) to ensure consistency across all falloff operators. Only the first page (Shape-specific, Radial-specific, etc.) will differ between falloff operators.

### Step 5: Add Inputs and Outputs

Add the Inputs and Outputs section after parameters:

```html
<section id="inputs-outputs">
  <h2>Inputs and Outputs</h2>

  <h3>Inputs</h3>
  <div class="io-section">
    <div class="parameter-item">
      <div class="param-header param-header-inline">
        <span class="param-label">Input 1</span>
        <span class="param-separator">–</span>
        <span class="param-name">POP</span>
        <span class="param-separator">–</span>
        <span class="param-text">POPX Geometry</span>
      </div>
    </div>
    <!-- Add more inputs if applicable -->
  </div>

  <h3>Outputs</h3>
  <div class="io-section">
    <div class="parameter-item">
      <div class="param-header param-header-inline">
        <span class="param-label">Output 0</span>
        <span class="param-separator">–</span>
        <span class="param-name">POP</span>
        <span class="param-separator">–</span>
        <span class="param-text">POPX_out1</span>
      </div>
    </div>
    <!-- Add more outputs if applicable -->
  </div>
</section>
```

**Important Notes:**
- Most POPX operators use Input 1 (not Input 0)
- Standard input description is "POPX Geometry"
- Standard output description is "POPX_out1"
- Adjust based on your operator's actual inputs/outputs

### Step 6: Add Page Navigation

Add previous/next page navigation at the bottom:

```html
<nav class="page-nav">
  <a href="../[previous-operator]/" class="page-nav-link page-nav-prev">
    <div class="page-nav-arrow">←</div>
    <div class="page-nav-label">
      <div class="page-nav-title">[Previous Operator Name]</div>
    </div>
  </a>
  <a href="../[next-operator]/" class="page-nav-link page-nav-next">
    <div class="page-nav-label">
      <div class="page-nav-title">[Next Operator Name]</div>
    </div>
    <div class="page-nav-arrow">→</div>
  </a>
</nav>
```

**Navigation Order:**
The page navigation should follow the same order as the sidebar navigation. For example, in the Modifiers section:
- Aim → Color Modifier
- Color Modifier → Magnetize
- Magnetize → Move Along Curve
- etc.

**IMPORTANT:** When you add a new operator, you must also **update the prev/next navigation buttons** in the surrounding operator pages:
- Update the **previous operator's** next button to point to your new operator
- Update the **next operator's** previous button to point to your new operator

**Example:** If you insert "My New Operator" between "Magnetize" and "Move Along Curve":
1. In `magnetize/index.html`: Update the next button from "Move Along Curve" to "My New Operator"
2. In `move-along-curve/index.html`: Update the prev button from "Magnetize" to "My New Operator"
3. In `my-new-operator/index.html`: Set prev to "Magnetize" and next to "Move Along Curve"

### Step 7: Update All Navigation

**Critical:** You must update navigation in **ALL** existing operator pages and the home page. This includes both sidebar links AND prev/next buttons.

#### Files to Update for Sidebar:

**All pages** (~30+ files):
1. **index.html** (home page) - sidebar only
2. All files in **docs/guides/** - sidebar only
3. All files in **docs/operators/generators/** - sidebar only
4. All files in **docs/operators/falloffs/** - sidebar only
5. All files in **docs/operators/modifiers/** - sidebar only
6. All files in **docs/operators/tools/** - sidebar only
7. All files in **docs/operators/simulations/** - sidebar only
8. All files in **docs/contact/** - sidebar only

#### Files to Update for Prev/Next Navigation:

**Only 2 operator pages** (the operators immediately before and after your new operator):
1. The **previous operator page** - update next button
2. The **next operator page** - update prev button

#### How to Update Sidebar:

Find the appropriate section in the sidebar and add your new operator link:

**Example - Adding to Modifiers:**
```html
<div class="sidebar-subsection">
  <h4>Modifiers</h4>
  <div class="sidebar-subsection-content">
    <ul>
      <li><a href="../../../operators/modifiers/aim/">Aim</a></li>
      <li><a href="../../../operators/modifiers/color-modifier/">Color Modifier</a></li>
      <li><a href="../../../operators/modifiers/magnetize/">Magnetize</a></li>
      <!-- Add your new operator here in alphabetical order -->
      <li><a href="../../../operators/modifiers/my-new-operator/">My New Operator</a></li>
      <li><a href="../../../operators/modifiers/move-along-curve/">Move Along Curve</a></li>
      <!-- ... rest of operators -->
    </ul>
  </div>
</div>
```

**Important:**
- Maintain alphabetical order within each category
- Adjust the path depth (`../../../`) based on the file's location
- Update the path in **every single page** - the paths are relative and will differ

**Path Examples:**
- From `index.html` (root): `docs/operators/modifiers/my-new-operator/`
- From `docs/guides/getting-started/index.html`: `../../operators/modifiers/my-new-operator/`
- From `docs/operators/modifiers/aim/index.html`: `../my-new-operator/`
- From `docs/operators/generators/convert/index.html`: `../../modifiers/my-new-operator/`

#### How to Update Prev/Next Navigation:

You only need to update 2 existing operator pages - the ones immediately surrounding your new operator.

**Example - Inserting "My New Operator" between Magnetize and Move Along Curve:**

1. **In `magnetize/index.html`** - Update the next button:
```html
<!-- OLD -->
<nav class="page-navigation">
  <a href="../color-modifier/" class="nav-button prev">Color Modifier</a>
  <a href="../move-along-curve/" class="nav-button next">Move Along Curve</a>
</nav>

<!-- NEW -->
<nav class="page-navigation">
  <a href="../color-modifier/" class="nav-button prev">Color Modifier</a>
  <a href="../my-new-operator/" class="nav-button next">My New Operator</a>
</nav>
```

2. **In `move-along-curve/index.html`** - Update the prev button:
```html
<!-- OLD -->
<nav class="page-navigation">
  <a href="../magnetize/" class="nav-button prev">Magnetize</a>
  <a href="../move-along-mesh/" class="nav-button next">Move Along Mesh</a>
</nav>

<!-- NEW -->
<nav class="page-navigation">
  <a href="../my-new-operator/" class="nav-button prev">My New Operator</a>
  <a href="../move-along-mesh/" class="nav-button next">Move Along Mesh</a>
</nav>
```

**Important:**
- The prev/next navigation must match the exact order in the sidebar
- Only update the 2 surrounding operators, not all operators
- Use relative paths (`../operator-name/`)

### Step 8: Update Search Functionality

The search functionality is automatically handled by `assets/js/script.js`. However, you need to ensure your page has proper heading structure for search indexing:

```html
<h1>[Operator Name]</h1>
<h2>Parameters</h2>
<h3 class="page-heading">[Page Name]</h3>
<!-- etc -->
```

**Search indexes:**
- Page title (h1)
- Section headings (h2)
- Page headings (h3)
- Parameter labels
- Parameter descriptions

No additional configuration is needed - the search bar will automatically find your page once it's added to the navigation.

### Step 9: Create Table of Contents

The Table of Contents (TOC) is automatically generated by JavaScript, but you need to ensure proper heading hierarchy:

```html
<h1>Operator Name</h1>           <!-- Not included in TOC -->
<h2>Parameters</h2>               <!-- TOC item -->
<h3 class="page-heading">Shape</h3>  <!-- TOC sub-item -->
<h3 class="page-heading">Transform</h3>  <!-- TOC sub-item -->
<h2>Inputs and Outputs</h2>       <!-- TOC item -->
```

**Important:**
- Only h2 and h3 with class `page-heading` appear in TOC
- Each section must have an `id` attribute for anchor links
- Common section IDs: `parameters`, `inputs-outputs`

### Step 10: Verify Integration

Before finalizing, verify the following checklist:

#### ✓ Directory and Files
- [ ] Directory created in correct category folder
- [ ] `index.html` created with proper file structure
- [ ] Paths to assets (CSS, JS, images) are correct for depth level

#### ✓ Content Sections
- [ ] Title (h1) matches operator name
- [ ] Summary section provides clear overview
- [ ] All parameters documented with proper structure
- [ ] Parameters grouped by page
- [ ] Input/Output section complete
- [ ] Page navigation (prev/next) links to correct operators

#### ✓ Navigation Updates
- [ ] Sidebar updated in **all ~30+ existing pages** (home, guides, all operators, contact)
- [ ] New operator link added in alphabetical order within category
- [ ] Sidebar paths adjusted correctly for each file's location
- [ ] All sidebar links tested and working
- [ ] **Previous operator's next button** updated to point to new operator
- [ ] **Next operator's prev button** updated to point to new operator
- [ ] New operator's prev/next buttons point to correct surrounding operators

#### ✓ Search and TOC
- [ ] Proper heading hierarchy (h1, h2, h3)
- [ ] Section IDs added for anchor links
- [ ] Page-heading class on parameter page h3 tags
- [ ] Search functionality finds the new page

#### ✓ Parameters
- [ ] All parameters from JSON exported and integrated
- [ ] Menu parameters have all sub-parameters listed
- [ ] Vec3/RGB/Vec2 parameters use full label (not component letters)
- [ ] Component naming follows conventions (lowercase x, y, z, r, g, b)
- [ ] All descriptions are clear and accurate

#### ✓ Testing
- [ ] Page loads without errors
- [ ] All links work correctly
- [ ] Navigation (prev/next) works
- [ ] Sidebar navigation works from all pages
- [ ] Search finds the new operator
- [ ] Table of Contents generates correctly
- [ ] Mobile menu works
- [ ] Theme selector works

### Common Issues and Solutions

#### Issue 1: Broken Asset Links
**Symptom:** CSS not loading, images not showing
**Solution:** Count directory depth correctly. From `docs/operators/category/operator/` you need `../../../../` to reach root.

#### Issue 2: Sidebar Links Don't Work
**Symptom:** Clicking sidebar link goes to 404
**Solution:** Paths are relative to each file. Update paths based on where each file is located, not copying the same path everywhere.

#### Issue 3: Search Doesn't Find Page
**Symptom:** Typing operator name in search returns no results
**Solution:** Ensure the page is linked in the sidebar navigation. Search only indexes pages that are in the navigation.

#### Issue 4: TOC Not Generating
**Symptom:** Table of Contents sidebar is empty
**Solution:** Add `id` attributes to h2 sections and `class="page-heading"` to parameter page h3 tags.

#### Issue 5: Page Navigation Broken
**Symptom:** Previous/Next buttons don't work or go to wrong pages
**Solution:** Follow the exact order from sidebar navigation. Previous/Next should match the list order in the sidebar. Remember to update the surrounding operators' prev/next buttons when inserting a new operator.

#### Issue 6: Navigation Chain Broken After Adding Operator
**Symptom:** Clicking next/prev buttons skips over the new operator or goes to wrong page
**Solution:** You forgot to update the 2 surrounding operators. When you insert an operator between two existing ones, you MUST update:
1. The previous operator's **next button** (to point to your new operator)
2. The next operator's **prev button** (to point to your new operator)

### Quick Reference: File Locations

```
POPX/
├── index.html                                    (Update sidebar)
├── docs/
│   ├── guides/
│   │   ├── getting-started/index.html           (Update sidebar)
│   │   ├── installation/index.html              (Update sidebar)
│   │   └── tutorials/index.html                 (Update sidebar)
│   ├── operators/
│   │   ├── generators/
│   │   │   ├── convert/index.html               (Update sidebar)
│   │   │   ├── explode/index.html               (Update sidebar)
│   │   │   ├── instancer/index.html             (Update sidebar)
│   │   │   ├── subdivider/index.html            (Update sidebar)
│   │   │   └── sweep/index.html                 (Update sidebar)
│   │   ├── falloffs/
│   │   │   ├── falloff-field/index.html         (Update sidebar)
│   │   │   ├── radial-falloff/index.html        (Update sidebar)
│   │   │   └── shape-falloff/index.html         (Update sidebar)
│   │   ├── modifiers/
│   │   │   ├── aim/index.html                   (Update sidebar)
│   │   │   ├── color-modifier/index.html        (Update sidebar)
│   │   │   ├── magnetize/index.html             (Update sidebar)
│   │   │   ├── move-along-curve/index.html      (Update sidebar)
│   │   │   ├── move-along-mesh/index.html       (Update sidebar)
│   │   │   ├── noise-modifier/index.html        (Update sidebar)
│   │   │   ├── pivot/index.html                 (Update sidebar)
│   │   │   ├── randomize/index.html             (Update sidebar)
│   │   │   ├── relax/index.html                 (Update sidebar)
│   │   │   ├── spring-modifier/index.html       (Update sidebar)
│   │   │   └── transform-modifier/index.html    (Update sidebar)
│   │   ├── tools/
│   │   │   ├── attribute-manager/index.html     (Update sidebar)
│   │   │   └── voxelize/index.html              (Update sidebar)
│   │   └── simulations/
│   │       ├── flip-solver/index.html           (Update sidebar)
│   │       └── sph-solver/index.html            (Update sidebar)
│   └── contact/
│       ├── contact-us/index.html                (Update sidebar)
│       └── community/index.html                 (Update sidebar)
└── assets/
    ├── css/style.css
    └── js/script.js
```

**Total files to update:**
- **~30+ files** for sidebar navigation (all pages in the site)
- **2 files** for prev/next navigation (only the surrounding operators)

### Navigation Update Summary

When adding a new operator, navigation updates are split into two parts:

**1. Sidebar Navigation (All Pages)**
- Update the sidebar in every single page (~30+ files)
- Add your new operator link in alphabetical order within its category
- Adjust relative paths for each file's location

**2. Prev/Next Navigation (Only 2 Pages)**
- Update only the 2 operators that surround your new operator
- Previous operator: change its **next button** to point to your new operator
- Next operator: change its **prev button** to point to your new operator

**Example workflow for adding "My New Operator" between Magnetize and Move Along Curve:**

| Step | File to Update | What to Change |
|------|---------------|----------------|
| 1 | All ~30+ pages | Add `<li><a href="...">My New Operator</a></li>` to sidebar |
| 2 | `magnetize/index.html` | Change next button from "Move Along Curve" → "My New Operator" |
| 3 | `move-along-curve/index.html` | Change prev button from "Magnetize" → "My New Operator" |
| 4 | `my-new-operator/index.html` | Set prev="Magnetize", next="Move Along Curve" |

---

## Overview

POPX operator parameters are exported from TouchDesigner as JSON data. This data contains all parameter information including labels, names, types, menu options, and metadata. The integration process transforms this JSON data into structured HTML documentation.

---

## Obtaining Complete Parameter Exports from TouchDesigner

This section explains how to get **complete parameter exports** from TouchDesigner operators, which include all metadata needed for accurate documentation.

### Why Complete Exports Matter

Complete parameter exports include critical metadata that simplified exports lack:
- `tupletName`: Groups related parameters
- `sequence`: Parameter ordering within pages
- `defaultMode`: How default values are set
- `enableExpr`: Conditional parameter availability
- `min`, `max`, `clampMin`, `clampMax`: Value constraints
- `menuSource`: Dynamic menu population
- All custom parameter properties

### How to Export Complete Parameter Data

1. **Open TouchDesigner** and load the POPX operator you want to document
2. **Run the parameter introspection script** (contact POPX developers for the export script)
3. **Copy the complete JSON output** - this will include all parameters across all pages
4. **Save to `parameters.json`** in the operator's documentation directory

**Example directory structure:**
```
docs/operators/modifiers/my-operator/
├── index.html
└── parameters.json  (complete export goes here)
```

### Complete vs Simplified Exports

**Simplified Export (AVOID):**
```json
{
  "Combineop": {
    "name": "Combineop",
    "label": "Combine Op",
    "style": "Menu"
  }
}
```

**Complete Export (USE THIS):**
```json
{
  "Combineop": {
    "name": "Combineop",
    "tupletName": "Combineop",
    "label": "Combine Op",
    "page": "Falloff",
    "style": "Menu",
    "order": 0,
    "sequence": 0,
    "size": 1,
    "startSection": false,
    "readOnly": false,
    "default": 0,
    "defaultMode": true,
    "clampMin": false,
    "clampMax": false,
    "normMin": 0.0,
    "normMax": 1.0,
    "enable": true,
    "enableExpr": null,
    "menuNames": ["add", "sub", "mult", "div", "screen", "overlay", "max", "min", "set"],
    "menuLabels": ["Add", "Substract", "Multiply", "Divide", "Screen", "Overlay", "Maximum", "Minimum", "Set"],
    "menuIndex": 0,
    "help": "Mathematical operation for combining attributes."
  }
}
```

### Critical Pattern: Menu vs StrMenu Parameters

**This is extremely important** - there are two types of menu-style parameters, and they are handled **completely differently** in the HTML:

#### Menu Parameters (style: "Menu")

Fixed dropdown menus with predefined options. **MUST have sub-parameters in HTML.**

**JSON Characteristics:**
```json
{
  "style": "Menu",
  "menuNames": ["add", "sub", "mult"],
  "menuLabels": ["Add", "Subtract", "Multiply"]
}
```

**HTML Structure (param-group with sub-parameters):**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Combine Op</span>
    <span class="param-name">Combineop</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Mathematical operation.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Add</span>
      <span class="param-name">add</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Subtract</span>
      <span class="param-name">sub</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Multiply</span>
      <span class="param-name">mult</span>
    </div>
  </div>
</div>
```

#### StrMenu Parameters (style: "StrMenu")

Dynamic attribute menus populated at runtime. **NO sub-parameters - treat as simple parameter.**

**JSON Characteristics:**
```json
{
  "style": "StrMenu",
  "menuSource": "op('./somenode').par.someparam",
  "menuNames": [],
  "menuLabels": []
}
```

**HTML Structure (parameter-item WITHOUT sub-parameters):**
```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Falloff Attribute</span>
    <span class="param-name">Falloffattr</span>
    <span class="param-separator">–</span>
    <span class="param-description">Name of the falloff attribute to use.</span>
  </div>
</div>
```

**Key Rule:**
- `style: "Menu"` → Use `<div class="param-group">` with `<div class="param-subparams">`
- `style: "StrMenu"` → Use `<div class="parameter-item">` (like Float, Int, Toggle)

### Menu Parameter Naming Conventions

For Menu parameters, there are two parallel arrays:

**menuLabels**: User-friendly display text (capitalized, readable)
- Examples: "Add", "Substract", "Multiply", "Scale Rotate Translate"

**menuNames**: Internal identifiers (lowercase, abbreviated)
- Examples: "add", "sub", "mult", "srt"

**HTML Pattern:**
```html
<div class="param-subparam">
  <span class="param-label">[menuLabels[i]]</span>
  <span class="param-name">[menuNames[i]]</span>
</div>
```

**Real Example:**
```json
"menuLabels": ["Add", "Substract", "Multiply"],
"menuNames": ["add", "sub", "mult"]
```

Becomes:
```html
<div class="param-subparam">
  <span class="param-label">Add</span>
  <span class="param-name">add</span>
</div>
<div class="param-subparam">
  <span class="param-label">Substract</span>
  <span class="param-name">sub</span>
</div>
<div class="param-subparam">
  <span class="param-label">Multiply</span>
  <span class="param-name">mult</span>
</div>
```

### Bulk Navigation Updates with sed

When adding or removing operators, you need to update navigation across **all ~30+ HTML files**. Use sed for efficient bulk updates.

**Add navigation link to all files:**
```bash
# From the root POPX directory
find docs -name "*.html" -type f -exec sed -i '/<li><a href=".*\/existing-operator\/">Existing Operator<\/a><\/li>/a\    <li><a href="RELATIVE_PATH\/my-new-operator\/">My New Operator<\/a><\/li>' {} \;
```

**Remove navigation link from all files:**
```bash
find docs -name "*.html" -type f -exec sed -i '/<li><a href=".*\/obsolete-operator\/">Obsolete Operator<\/a><\/li>/d' {} \;
```

**Important Notes:**
- Paths in sed must match the pattern used across files (use `.*` for flexible path matching)
- Alphabetical order must be maintained manually
- Main `index.html` may need separate manual update due to different path structure
- Always verify changes with grep after running sed

**Verification command:**
```bash
# Check that the link was added/removed correctly
grep -r "My New Operator" docs/
```

---

## Navigation and Search Integration

When adding a new operator, you must update **four separate systems**:

### Summary: What to Update

| System | Files to Update | What to Update |
|--------|----------------|----------------|
| **1. Sidebar Navigation** | All ~30+ HTML files | Add operator link in alphabetical order |
| **2. Prev/Next Buttons** | 2 operator HTML files | Update surrounding operators' navigation |
| **3. Search Index** | `assets/js/script.js` | Add operator entry to searchIndex array |
| **4. Parameters** | Operator's index.html | Document all parameters from JSON export |

### Detailed Instructions

When adding a new operator, you must update **three separate navigation systems** plus the search index:

### 1. Sidebar Navigation (All Pages)

**Files to Update:** ALL ~30+ HTML files across the entire site
- `index.html` (homepage)
- All files in `docs/guides/`
- All files in `docs/operators/generators/`
- All files in `docs/operators/falloffs/`
- All files in `docs/operators/modifiers/`
- All files in `docs/operators/tools/`
- All files in `docs/operators/simulations/`
- All files in `docs/contact/`

**What to Update:**
Add your new operator link to the appropriate sidebar section in alphabetical order.

**Example - Adding "Noise Modifier" to Modifiers section:**
```html
<div class="sidebar-subsection">
  <h4>Modifiers</h4>
  <div class="sidebar-subsection-content">
    <ul>
      <li><a href="../../../operators/modifiers/aim/">Aim</a></li>
      <li><a href="../../../operators/modifiers/color-modifier/">Color Modifier</a></li>
      <li><a href="../../../operators/modifiers/magnetize/">Magnetize</a></li>
      <!-- Add new operator here -->
      <li><a href="../../../operators/modifiers/noise-modifier/">Noise Modifier</a></li>
      <li><a href="../../../operators/modifiers/move-along-curve/">Move Along Curve</a></li>
    </ul>
  </div>
</div>
```

**Path Adjustments:**
Paths are relative to each file's location. You MUST adjust the path depth:
- From `index.html` (root): `docs/operators/modifiers/noise-modifier/`
- From `docs/guides/getting-started/index.html`: `../../operators/modifiers/noise-modifier/`
- From `docs/operators/modifiers/aim/index.html`: `../noise-modifier/`
- From `docs/operators/generators/convert/index.html`: `../../modifiers/noise-modifier/`

**Bulk Update with sed:**
```bash
# Add link to all pages (example - adjust paths as needed)
find docs -name "*.html" -type f -exec sed -i '/<li><a href=".*\/magnetize\/">Magnetize<\/a><\/li>/a\    <li><a href="ADJUST_PATH\/noise-modifier\/">Noise Modifier<\/a><\/li>' {} \;
```

### 2. Prev/Next Navigation Buttons

**Files to Update:** Only the 2 operators immediately surrounding your new operator

**What to Update:**
- **Previous operator**: Change its `next` button to point to your new operator
- **Next operator**: Change its `prev` button to point to your new operator

**Example - Inserting "Noise Modifier" between "Magnetize" and "Move Along Curve":**

**In `magnetize/index.html`** - Update next button:
```html
<!-- OLD -->
<nav class="page-nav">
  <a href="../color-modifier/" class="page-nav-link page-nav-prev">
    <div class="page-nav-arrow">←</div>
    <div class="page-nav-label">
      <div class="page-nav-title">Color Modifier</div>
    </div>
  </a>
  <a href="../move-along-curve/" class="page-nav-link page-nav-next">
    <div class="page-nav-label">
      <div class="page-nav-title">Move Along Curve</div>
    </div>
    <div class="page-nav-arrow">→</div>
  </a>
</nav>

<!-- NEW -->
<nav class="page-nav">
  <a href="../color-modifier/" class="page-nav-link page-nav-prev">
    <div class="page-nav-arrow">←</div>
    <div class="page-nav-label">
      <div class="page-nav-title">Color Modifier</div>
    </div>
  </a>
  <a href="../noise-modifier/" class="page-nav-link page-nav-next">
    <div class="page-nav-label">
      <div class="page-nav-title">Noise Modifier</div>
    </div>
    <div class="page-nav-arrow">→</div>
  </a>
</nav>
```

**In `move-along-curve/index.html`** - Update prev button:
```html
<!-- OLD -->
<nav class="page-nav">
  <a href="../magnetize/" class="page-nav-link page-nav-prev">
    <div class="page-nav-arrow">←</div>
    <div class="page-nav-label">
      <div class="page-nav-title">Magnetize</div>
    </div>
  </a>
  <a href="../move-along-mesh/" class="page-nav-link page-nav-next">
    <div class="page-nav-label">
      <div class="page-nav-title">Move Along Mesh</div>
    </div>
    <div class="page-nav-arrow">→</div>
  </a>
</nav>

<!-- NEW -->
<nav class="page-nav">
  <a href="../noise-modifier/" class="page-nav-link page-nav-prev">
    <div class="page-nav-arrow">←</div>
    <div class="page-nav-label">
      <div class="page-nav-title">Noise Modifier</div>
    </div>
  </a>
  <a href="../move-along-mesh/" class="page-nav-link page-nav-next">
    <div class="page-nav-label">
      <div class="page-nav-title">Move Along Mesh</div>
    </div>
    <div class="page-nav-arrow">→</div>
  </a>
</nav>
```

**In your new operator `noise-modifier/index.html`:**
```html
<nav class="page-nav">
  <a href="../magnetize/" class="page-nav-link page-nav-prev">
    <div class="page-nav-arrow">←</div>
    <div class="page-nav-label">
      <div class="page-nav-title">Magnetize</div>
    </div>
  </a>
  <a href="../move-along-curve/" class="page-nav-link page-nav-next">
    <div class="page-nav-label">
      <div class="page-nav-title">Move Along Curve</div>
    </div>
    <div class="page-nav-arrow">→</div>
  </a>
</nav>
```

### 3. Search Functionality

**IMPORTANT:** Search is NOT automatic - you MUST manually add new operators to the search index!

The search functionality uses a hardcoded index in `assets/js/script.js`. Every time you add a new operator, you MUST add it to the `searchIndex` array.

**Where to Add:**
File: `assets/js/script.js`
Location: Around line 726 (search for `const searchIndex = [`)

**How to Add:**

1. **Find the correct category section** in searchIndex:
   - Guides (Getting Started, Installation, Tutorials)
   - Contact (Contact Us, Community)
   - Generators (Convert, Explode, Instancer, Subdivider, Sweep)
   - Falloffs (Noise Falloff, Shape Falloff)
   - Modifiers (Aim through Transform Modifier)
   - Tools (Attribute Manager, Voxelize - NOT YET CREATED)
   - Simulations (FLIP Solver, SPH Solver - NOT YET CREATED)

2. **Add your operator in alphabetical order** within its category

3. **Use this template:**

```javascript
{
  title: 'Your Operator Name',
  path: 'docs/operators/category/your-operator/',
  type: 'Operator',
  category: 'Category Name',  // Generators, Falloffs, Modifiers, Tools, Simulations
  sections: [
    { title: 'Summary', anchor: '#summary' },
    { title: 'Page: Page Name', anchor: '#page-pagename', keywords: ['keyword1', 'keyword2'] },
    { title: 'Page: Common', anchor: '#page-common' },
    { title: 'Inputs', anchor: '#inputs' },
    { title: 'Outputs', anchor: '#outputs' }
  ]
},
```

**Complete Example - Adding Noise Falloff:**

```javascript
// Falloffs section
{
  title: 'Noise Falloff',
  path: 'docs/operators/falloffs/noise-falloff/',
  type: 'Operator',
  category: 'Falloffs',
  sections: [
    { title: 'Summary', anchor: '#summary' },
    { title: 'Page: Noise', anchor: '#page-noise', keywords: ['perlin', 'simplex', 'harmonics', 'amplitude', 'frequency'] },
    { title: 'Page: Transform', anchor: '#page-transform', keywords: ['translate', 'rotate', 'scale', 'pivot'] },
    { title: 'Page: Falloff', anchor: '#page-falloff', keywords: ['combine', 'blend', 'attribute'] },
    { title: 'Page: Remap', anchor: '#page-remap', keywords: ['fit', 'clamp', 'invert', 'ramp'] },
    { title: 'Page: Common', anchor: '#page-common' },
    { title: 'Inputs', anchor: '#inputs' },
    { title: 'Outputs', anchor: '#outputs' }
  ]
},
```

**Important Notes:**

- **Path**: Must match your operator's directory path exactly (no leading slash)
- **Category**: Must match one of the sidebar categories
- **Sections**: List ALL major sections and parameter pages from your operator
- **Anchors**: Must match the `id` attributes in your HTML (e.g., `id="page-noise"`)
- **Keywords** (optional): Add relevant search terms for each section to improve discoverability
- **Alphabetical Order**: Within each category, operators should be in alphabetical order
- **Comma**: Don't forget the trailing comma after the closing brace

**Verification:**

After adding to searchIndex:
1. Open the site in a browser
2. Type your operator name in the search bar
3. Verify it appears in results
4. Click the result and verify navigation works
5. Try searching for parameter page names (e.g., "noise", "transform")
6. Verify section links work correctly

**Example heading structure for good search results:**
```html
<article class="operator-page">
  <h1>Noise Modifier</h1>  <!-- Indexed: main title -->

  <section class="summary">
    <p>Adds procedural noise to particle attributes.</p>  <!-- Indexed: summary -->
  </section>

  <section id="parameters" class="parameters">
    <h2>Parameters</h2>  <!-- Indexed: section title -->

    <h3 class="page-heading">Noise</h3>  <!-- Indexed: parameter page -->
    <h3 class="page-heading">Transform</h3>  <!-- Indexed: parameter page -->

    <div class="parameter-item">
      <div class="param-header">
        <span class="param-label">Amplitude</span>  <!-- Indexed: parameter label -->
        <span class="param-name">Amplitude</span>  <!-- Indexed: parameter name -->
        <span class="param-description">Strength of the noise effect.</span>  <!-- Indexed: description -->
      </div>
    </div>
  </section>

  <section id="inputs-outputs">
    <h2>Inputs and Outputs</h2>  <!-- Indexed: section title -->
  </section>
</article>
```

**Search Result Format:**
When users search, results show:
- **Page title** (e.g., "Noise Modifier")
- **Section** where the match was found (e.g., "Parameters > Noise")
- **Snippet** of matching text with highlighting

**Testing Search:**
1. Add your operator to the sidebar navigation
2. Open the site in a browser
3. Type your operator name in the search bar
4. Verify it appears in results
5. Verify clicking the result navigates to your page
6. Try searching for specific parameters - they should also appear

**Common Search Issues:**

❌ **Issue:** New operator doesn't appear in search
✅ **Solution:** Check that it's linked in the sidebar navigation

❌ **Issue:** Parameters don't show up in search results
✅ **Solution:** Ensure proper HTML structure with param-label and param-description

❌ **Issue:** Search results don't show correct section
✅ **Solution:** Add `class="page-heading"` to parameter page h3 tags

### Navigation Update Checklist

When adding a new operator, verify:

#### ✓ Sidebar Navigation
- [ ] Added to **all ~30+ HTML files** (homepage, guides, all operators, contact pages)
- [ ] Link added in correct category section
- [ ] Maintained alphabetical order
- [ ] Paths adjusted correctly for each file's location
- [ ] All sidebar links tested and working

#### ✓ Prev/Next Navigation
- [ ] Updated **previous operator's next button** to point to new operator
- [ ] Updated **next operator's prev button** to point to new operator
- [ ] New operator's prev/next buttons point to correct surrounding operators
- [ ] Navigation chain tested - clicking through works correctly

#### ✓ Search Integration
- [ ] **Operator added to searchIndex array** in `assets/js/script.js` (REQUIRED!)
- [ ] Entry added in correct category and alphabetical order
- [ ] All parameter pages listed in sections array
- [ ] Anchors match HTML id attributes
- [ ] Keywords added for important sections (optional but recommended)
- [ ] Proper heading hierarchy (h1, h2, h3 with page-heading class)
- [ ] Parameter labels and descriptions are complete
- [ ] Search bar finds the new operator by name
- [ ] Search finds specific parameters
- [ ] Search results link correctly to the page

### Quick Update Workflow

**Step 1: Create Operator Page**
- Create directory: `docs/operators/category/operator-name/`
- Create `index.html` with complete structure
- Create `parameters.json` with complete TouchDesigner export

**Step 2: Update Sidebar Navigation (All ~30+ Files)**
```bash
# Use sed to add link to all files (adjust pattern and paths)
find docs -name "*.html" -type f -exec sed -i '/<li><a href=".*\/existing-operator\/">Existing Operator<\/a><\/li>/a\    <li><a href="RELATIVE_PATH\/new-operator\/">New Operator<\/a><\/li>' {} \;

# Manually update main index.html (different path structure)
# Edit: index.html
```

**Step 3: Update Prev/Next Navigation (2 Files Only)**
```bash
# Manually edit the 2 surrounding operator files
# Edit: docs/operators/category/previous-operator/index.html (next button)
# Edit: docs/operators/category/next-operator/index.html (prev button)
```

**Step 4: Update Search Index (CRITICAL - DO NOT SKIP!)**
```bash
# Edit: assets/js/script.js
# Find: const searchIndex = [
# Add your operator entry in the correct category, in alphabetical order
# Use the template provided in Section 3 above
```

**Step 5: Verification**
```bash
# Check sidebar was updated everywhere
grep -r "New Operator" docs/ | wc -l
# Should show ~30+ matches (one per file)

# Check prev/next navigation updated
grep -A5 -B5 "page-nav" docs/operators/category/previous-operator/index.html
grep -A5 -B5 "page-nav" docs/operators/category/next-operator/index.html

# Check search index was updated
grep "New Operator" assets/js/script.js
# Should show your operator in searchIndex

# Test in browser:
# 1. Open site
# 2. Type operator name in search bar
# 3. Verify it appears in results
# 4. Click result and verify navigation works
```

---

## JSON Parameter Structure

### Basic Parameter Fields

Each parameter in the JSON contains the following key fields:

```json
{
  "name": "Paramname",           // Internal parameter name (used in scripting)
  "label": "Param Label",        // Display label shown in UI
  "page": "PageName",            // Parameter page/tab name
  "style": "Menu",               // Parameter type/style
  "size": 1,                     // Number of components (1, 2, 3, 4)
  "menuLabels": [...],           // Menu option labels (for Menu style)
  "menuNames": [...],            // Menu option internal names
  "help": "Description text"     // Parameter description
}
```

### Parameter Styles

Common parameter styles include:

- **Menu**: Dropdown menu with predefined options (has sub-parameters)
- **StrMenu**: Dynamic attribute menu (NO sub-parameters - references existing attributes)
- **Float**: Floating-point number input
- **Int**: Integer number input
- **Toggle**: Boolean on/off switch
- **Pulse**: Momentary button
- **OP**: Operator reference
- **Str**: String/text input
- **RGBA**: 4-component color (R, G, B, A)
- **XYZ**: 3-component vector (X, Y, Z)
- **XYZW**: 4-component vector (X, Y, Z, W)
- **UV**: 2-component coordinate (U, V)

**Important:** `StrMenu` parameters are attribute menus that dynamically list available attributes. These should be treated as **simple parameters** without sub-parameters, even though they are menu-like.

---

## HTML Parameter Structure

### Single Parameter (Non-Grouped)

For simple parameters without sub-parameters:

```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Parameter Label</span>
    <span class="param-name">Paramname</span>
    <span class="param-separator">–</span>
    <span class="param-description">Description of what this parameter does.</span>
  </div>
</div>
```

### Grouped Parameter (With Sub-Parameters)

For parameters with sub-parameters (Menu, Vec3, RGBA, etc.):

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Parameter Label</span>
    <span class="param-name">Paramname</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Description of what this parameter does.</span>
  </div>
  <div class="param-subparams">
    <!-- Sub-parameters go here -->
  </div>
</div>
```

### Sub-Parameter Format

Each sub-parameter follows this structure:

```html
<div class="param-subparam">
  <span class="param-label">Sub-Parameter Label</span>
  <span class="param-name">subparamname</span>
</div>
```

---

## Parameter Types

### 1. Menu Parameters (style: "Menu")

Menu parameters have multiple predefined options with sub-parameters.

**JSON Example:**
```json
{
  "name": "Shapetype",
  "label": "Shape Type",
  "style": "Menu",
  "size": 1,
  "menuLabels": ["Sphere", "Box", "Torus"],
  "menuNames": ["sphere", "box", "torus"],
  "help": "Selects the geometric primitive."
}
```

### 1.5. Attribute Menu Parameters (style: "StrMenu")

**IMPORTANT:** Attribute menus (StrMenu) are dynamic menus that reference existing attributes in the geometry. These should be treated as **simple parameters WITHOUT sub-parameters**.

**JSON Example:**
```json
{
  "name": "Falloffattr",
  "label": "Falloff Attribute",
  "style": "StrMenu",
  "size": 1,
  "menuSource": "op('./somenode').par.someparam",
  "help": "Name of the falloff attribute to use."
}
```

**HTML Output:**
```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Falloff Attribute</span>
    <span class="param-name">Falloffattr</span>
    <span class="param-separator">–</span>
    <span class="param-description">Name of the falloff attribute to use.</span>
  </div>
</div>
```

**Key Difference:**
- **Menu (style: "Menu")**: Use `<div class="param-group">` with sub-parameters
- **StrMenu (style: "StrMenu")**: Use `<div class="parameter-item">` WITHOUT sub-parameters

**HTML Output:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Shape Type</span>
    <span class="param-name">Shapetype</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Selects the geometric primitive.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Sphere</span>
      <span class="param-name">sphere</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Box</span>
      <span class="param-name">box</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Torus</span>
      <span class="param-name">torus</span>
    </div>
  </div>
</div>
```

### 2. Vec3/XYZ Parameters

Vec3 parameters have 3 components (X, Y, Z).

**JSON Example:**
```json
{
  "name": "T",
  "tupletName": "T",
  "label": "Translate",
  "style": "XYZ",
  "size": 3,
  "help": "Translation offset applied to the shape."
}
```

**Component Naming:**
- Base name: `T`
- X component: `Tx`
- Y component: `Ty`
- Z component: `Tz`

**HTML Output:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Translate</span>
    <span class="param-name">T</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Translation offset applied to the shape.</span>
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

**Important:** The sub-parameter label uses the **full parameter label** (e.g., "Translate"), NOT just the component letter (X, Y, Z).

### 3. RGB/RGBA Parameters

RGB parameters have 3 components (R, G, B). RGBA adds an Alpha component.

**JSON Example:**
```json
{
  "name": "Color",
  "label": "Color",
  "style": "RGB",
  "size": 3,
  "help": "Color used to display the shape."
}
```

**Component Naming:**
- Base name: `Color`
- R component: `Colorr`
- G component: `Colorg`
- B component: `Colorb`

**HTML Output:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Color</span>
    <span class="param-name">Color</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Color used to display the shape.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Color</span>
      <span class="param-name">Colorr</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Color</span>
      <span class="param-name">Colorg</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Color</span>
      <span class="param-name">Colorb</span>
    </div>
  </div>
</div>
```

**Important:** The sub-parameter label uses the **full parameter label** (e.g., "Color"), NOT the component letter (R, G, B).

### 4. Vec2/UV Parameters

Vec2 parameters have 2 components (X, Y or U, V).

**JSON Example:**
```json
{
  "name": "Strength",
  "label": "Strength",
  "style": "UV",
  "size": 2,
  "help": "Strength parameters for the shape."
}
```

**Component Naming:**
- Base name: `Strength`
- X component: `Strengthx`
- Y component: `Strengthy`

**HTML Output:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Strength</span>
    <span class="param-name">Strength</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Strength parameters for the shape.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Strength</span>
      <span class="param-name">Strengthx</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Strength</span>
      <span class="param-name">Strengthy</span>
    </div>
  </div>
</div>
```

### 5. Simple Parameters

Simple parameters (Float, Int, Toggle, Pulse, String, OP) don't have sub-parameters.

**JSON Example:**
```json
{
  "name": "Height",
  "label": "Height",
  "style": "Float",
  "size": 1,
  "help": "Height parameter for Cylinder Rounded."
}
```

**HTML Output:**
```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Height</span>
    <span class="param-name">Height</span>
    <span class="param-separator">–</span>
    <span class="param-description">Height parameter for Cylinder Rounded.</span>
  </div>
</div>
```

---

## Integration Process

### Step 1: Extract JSON Data

Export parameter data from TouchDesigner operator. The JSON should contain all parameters with their metadata.

### Step 2: Organize by Pages

Group parameters by their `page` field:
- Shape
- Transform
- Falloff
- Noise
- Remap
- Common

### Step 3: Determine Parameter Type

Check the `style` and `size` fields to determine the parameter type:

- If `style: "Menu"` → Menu parameter with sub-parameters
- If `size: 3` and name contains color-like terms → RGB parameter
- If `size: 3` and style is XYZ-related → Vec3 parameter
- If `size: 2` → Vec2 parameter
- If `size: 1` → Simple parameter (no sub-parameters)

### Step 4: Generate HTML Structure

For each parameter:

1. **Create parameter container:**
   - Use `<div class="param-group">` for parameters with sub-parameters
   - Use `<div class="parameter-item">` for simple parameters

2. **Add parameter header:**
   - Include label, name, and description
   - Add toggle separator for grouped parameters

3. **Add sub-parameters (if applicable):**
   - For Menu: Use `menuLabels` and `menuNames` arrays
   - For Vec3/RGB: Use full parameter label + component suffix
   - For Vec2: Use full parameter label + x/y suffix

### Step 5: Apply Naming Conventions

**For Menu Parameters:**
- Label: Use `menuLabels[i]`
- Name: Use `menuNames[i]`

**For Vec3/XYZ Parameters:**
- Label: Use full parameter label (e.g., "Translate")
- Name: Use base name + component (e.g., "Tx", "Ty", "Tz")

**For RGB Parameters:**
- Label: Use full parameter label (e.g., "Color")
- Name: Use base name + component (e.g., "Colorr", "Colorg", "Colorb")

**For Vec2/UV Parameters:**
- Label: Use full parameter label (e.g., "Strength")
- Name: Use base name + component (e.g., "Strengthx", "Strengthy")

---

## Examples

### Example 1: Transform Order Menu

**JSON:**
```json
{
  "name": "Xord",
  "label": "Transform Order",
  "style": "Menu",
  "menuLabels": [
    "Scale Rotate Translate",
    "Scale Translate Rotate",
    "Rotate Scale Translate",
    "Rotate Translate Scale",
    "Translate Scale Rotate",
    "Translate Rotate Scale"
  ],
  "menuNames": ["srt", "str", "rst", "rts", "tsr", "trs"],
  "help": "Order in which Scale, Rotate, and Translate operations are applied."
}
```

**HTML:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Transform Order</span>
    <span class="param-name">Xord</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Order in which Scale, Rotate, and Translate operations are applied.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Scale Rotate Translate</span>
      <span class="param-name">srt</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Scale Translate Rotate</span>
      <span class="param-name">str</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Rotate Scale Translate</span>
      <span class="param-name">rst</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Rotate Translate Scale</span>
      <span class="param-name">rts</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Translate Scale Rotate</span>
      <span class="param-name">tsr</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Translate Rotate Scale</span>
      <span class="param-name">trs</span>
    </div>
  </div>
</div>
```

### Example 2: Rotate Order Menu

**JSON:**
```json
{
  "name": "Rord",
  "label": "Rotate Order",
  "style": "Menu",
  "menuLabels": ["Rx Ry Rz", "Rx Rz Ry", "Ry Rx Rz", "Ry Rz Rx", "Rz Rx Ry", "Rz Ry Rx"],
  "menuNames": ["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"],
  "help": "Order in which rotations around axes are applied."
}
```

**HTML:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Rotate Order</span>
    <span class="param-name">Rord</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Order in which rotations around axes are applied.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Rx Ry Rz</span>
      <span class="param-name">xyz</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Rx Rz Ry</span>
      <span class="param-name">xzy</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Ry Rx Rz</span>
      <span class="param-name">yxz</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Ry Rz Rx</span>
      <span class="param-name">yzx</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Rz Rx Ry</span>
      <span class="param-name">zxy</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Rz Ry Rx</span>
      <span class="param-name">zyx</span>
    </div>
  </div>
</div>
```

### Example 3: Scale Vec3 Parameter

**JSON:**
```json
{
  "name": "S",
  "tupletName": "S",
  "label": "Scale",
  "style": "XYZ",
  "size": 3,
  "help": "Scale factors applied to the shape along each axis."
}
```

**HTML:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Scale</span>
    <span class="param-name">S</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Scale factors applied to the shape along each axis.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Scale</span>
      <span class="param-name">Sx</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Scale</span>
      <span class="param-name">Sy</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Scale</span>
      <span class="param-name">Sz</span>
    </div>
  </div>
</div>
```

### Example 4: Shape Color RGB Parameter

**JSON:**
```json
{
  "name": "Shapecolor",
  "label": "Shape Color",
  "style": "RGB",
  "size": 3,
  "help": "Color used to display the shape when Display Shape is enabled."
}
```

**HTML:**
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Shape Color</span>
    <span class="param-name">Shapecolor</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Color used to display the shape when Display Shape is enabled.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Shape Color</span>
      <span class="param-name">Shapecolorr</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Shape Color</span>
      <span class="param-name">Shapecolorg</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Shape Color</span>
      <span class="param-name">Shapecolorb</span>
    </div>
  </div>
</div>
```

---

## Best Practices

### 1. Consistent Naming

- **Menu parameters:** Always use both `menuLabels` and `menuNames`
- **Vec3/RGB parameters:** Always use full parameter label for sub-parameters
- **Component suffixes:** Use lowercase (x, y, z, r, g, b)

### 2. Structure Organization

- Group parameters by page
- Maintain alphabetical or logical order within pages
- Use section dividers (`<hr class="section-divider">`) between pages

### 3. Description Quality

- Write clear, concise descriptions
- Explain what the parameter does, not just what it is
- Include units or value ranges when relevant
- Mention conditional availability (e.g., "available when Shape Type is Box")

### 4. HTML Formatting

- Maintain consistent indentation (2 spaces per level)
- Keep opening and closing tags aligned
- Use semantic class names
- Preserve line breaks for readability

### 5. Validation Checklist

Before finalizing parameter integration:

- ✓ All menu parameters have sub-parameters with labels and names
- ✓ All Vec3/RGB parameters use full label (not component letters)
- ✓ All parameter names match JSON exactly
- ✓ All descriptions are clear and accurate
- ✓ HTML structure is valid and properly nested
- ✓ Class names follow established conventions

### 6. Common Mistakes to Avoid

❌ **Wrong:** Using component letters for Vec3/RGB labels
```html
<span class="param-label">X</span>  <!-- Don't do this -->
```

✅ **Correct:** Using full parameter label
```html
<span class="param-label">Translate</span>  <!-- Do this -->
```

❌ **Wrong:** Missing sub-parameters for Menu parameters
```html
<div class="param-group">
  <!-- Missing param-subparams section -->
</div>
```

✅ **Correct:** Including all menu options
```html
<div class="param-group">
  <div class="param-group-header">...</div>
  <div class="param-subparams">
    <!-- All menu options listed -->
  </div>
</div>
```

❌ **Wrong:** Inconsistent component naming
```html
<span class="param-name">TranslateX</span>  <!-- Don't capitalize -->
```

✅ **Correct:** Lowercase component suffix
```html
<span class="param-name">Tx</span>  <!-- Use single lowercase letter -->
```

---

## Conclusion

Following this guide ensures consistent, accurate, and maintainable parameter documentation across all POPX operator pages. The key principles are:

1. **Accuracy:** Match JSON data exactly
2. **Consistency:** Use standardized HTML structure
3. **Clarity:** Write helpful descriptions
4. **Completeness:** Include all sub-parameters
5. **Validation:** Check against established patterns

For questions or issues, refer to existing operator pages like Transform Modifier, Move Along Curve, or Shape Falloff as reference examples.
