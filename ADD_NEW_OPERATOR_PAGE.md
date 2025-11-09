# Adding a New Operator Page

Quick guide for adding new operators to the POPX documentation site using the modular component architecture.

## Table of Contents

1. [Site Architecture](#site-architecture)
2. [Quick Start Workflow](#quick-start-workflow)
3. [Parameter Documentation](#parameter-documentation)
4. [Parameter Types Reference](#parameter-types-reference)

---

## Site Architecture

The POPX site uses **modular components** where shared UI elements (navbar, sidebar, mobile menu) are loaded dynamically from `/components/` folder.

### Directory Structure

```
POPX/
├── components/               # Reusable UI components
│   ├── navbar.html          # Top navigation
│   ├── sidebar.html         # Left sidebar navigation
│   ├── mobile-menu.html     # Mobile menu button
│   └── menu-overlay.html    # Mobile overlay
├── docs/operators/
│   ├── generators/          # Convert, Explode, Instancer, etc.
│   ├── falloffs/            # Combine Falloff, Curve Falloff, etc.
│   ├── modifiers/           # Aim, Pivot, Randomize, etc.
│   ├── tools/               # Attribute Manager, Voxelize
│   └── simulations/         # FLIP Solver, SPH Solver
└── assets/js/
    ├── component-loader.js  # Loads components dynamically
    └── script.js            # Main site JavaScript (contains search index)
```

### Key Benefits

- **Update once, apply everywhere**: Edit `components/sidebar.html` to update all pages
- **Automatic path resolution**: Component loader handles relative paths
- **Smaller pages**: ~3x reduction in HTML duplication
- **Guaranteed consistency**: All pages always have identical navigation

### Local Development

The component system requires an HTTP server (not `file://`):

```bash
# Python
python -m http.server 8000

# Node.js
npx http-server -p 8000

# VS Code: Install "Live Server" extension
```

---

## Quick Start Workflow

### Step 1: Create Directory & Files

```bash
# Create operator directory
mkdir -p docs/operators/[category]/[operator-name]/

# Categories: generators, falloffs, modifiers, tools, simulations
```

### Step 2: Create HTML File

Create `index.html` with this template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Operator Name] | POPX</title>
  <meta name="description" content="[Brief operator description]">
  <link rel="icon" type="image/png" href="../../../../media/popx-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../../../assets/css/style.css">
</head>
<body>
  <script>
    // Prevent flash during page transitions
    if (performance.navigation.type === 1) {
      document.body.style.opacity = '1';
    } else {
      document.body.classList.add('page-transitioning');
    }
  </script>

  <!-- Component containers - loaded dynamically -->
  <div id="navbar-container"></div>

  <div class="page-layout">
    <div id="mobile-menu-container"></div>
    <div id="sidebar-container"></div>

    <!-- Main Content -->
    <main class="main-content">
      <h1>[Operator Name]</h1>

      <section id="summary">
        <h2>Summary</h2>
        <p>[1-2 paragraph description of what this operator does]</p>
      </section>

      <section id="parameters">
        <h2>Parameters</h2>

        <h3 class="page-heading" id="page-[pagename]">Page: [Page Name]</h3>
        <!-- Add parameters here - see Parameter Documentation section -->

        <hr class="section-divider">

        <h3 class="page-heading" id="page-common">Page: Common</h3>
        <!-- Standard Common parameters -->
      </section>

      <section id="inputs">
        <h2>Inputs</h2>
        <div class="parameter-item">
          <div class="param-header param-header-inline">
            <span class="param-label">Input 0</span>
            <span class="param-separator">–</span>
            <span class="param-name">POP</span>
            <span class="param-separator">–</span>
            <span class="param-text">POPX Geometry</span>
          </div>
        </div>
      </section>

      <section id="outputs">
        <h2>Outputs</h2>
        <div class="parameter-item">
          <div class="param-header param-header-inline">
            <span class="param-label">Output 0</span>
            <span class="param-separator">–</span>
            <span class="param-name">POP</span>
            <span class="param-separator">–</span>
            <span class="param-text">POPX_out1</span>
          </div>
        </div>
      </section>

      <!-- Page Navigation -->
      <nav class="page-navigation">
        <a href="../[previous-operator]/" class="nav-button prev">[Previous Operator]</a>
        <a href="../[next-operator]/" class="nav-button next">[Next Operator]</a>
      </nav>
    </main>

    <!-- Table of Contents -->
    <aside class="toc">
      <h4>Contents</h4>
      <ul>
        <li><a href="#summary">Summary</a></li>
        <li><a href="#parameters">Parameters</a></li>
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

**Note:** Adjust `../../../../` based on depth (count slashes from operator to root).

### Step 3: Update Sidebar Navigation

**IMPORTANT:** Update **ONLY ONE FILE** - all pages will automatically get the update.

Edit `components/sidebar.html` and add your operator link in alphabetical order:

```html
<div class="sidebar-subsection">
  <h4>[Category Name]</h4>
  <div class="sidebar-subsection-content">
    <ul>
      <li><a href="docs/operators/[category]/[existing-operator]/">Existing Operator</a></li>
      <li><a href="docs/operators/[category]/[your-operator]/">Your New Operator</a></li>
      <li><a href="docs/operators/[category]/[next-operator]/">Next Operator</a></li>
    </ul>
  </div>
</div>
```

**Paths in sidebar:** Always use `docs/operators/[category]/[operator]/` format (relative to site root).

### Step 4: Update Prev/Next Navigation

Update **only 2 files** - the operators immediately surrounding your new one:

**In previous operator's `index.html`:**
```html
<a href="../[your-operator]/" class="nav-button next">Your New Operator</a>
```

**In next operator's `index.html`:**
```html
<a href="../[your-operator]/" class="nav-button prev">Your New Operator</a>
```

### Step 5: Update Search Index

**CRITICAL:** Search is not automatic!

Edit `assets/js/script.js` (around line 726) and add to `searchIndex` array in alphabetical order:

```javascript
{
  title: 'Your Operator Name',
  path: 'docs/operators/category/your-operator/',
  type: 'Operator',
  category: 'Category Name',  // Generators, Falloffs, Modifiers, Tools, Simulations
  sections: [
    { title: 'Summary', anchor: '#summary' },
    { title: 'Page: [Page Name]', anchor: '#page-pagename', keywords: ['keyword1', 'keyword2'] },
    { title: 'Page: Common', anchor: '#page-common' },
    { title: 'Inputs', anchor: '#inputs' },
    { title: 'Outputs', anchor: '#outputs' }
  ]
},
```

### Step 6: Verify Everything

- [ ] Operator page loads without errors
- [ ] Sidebar shows operator on all pages
- [ ] Prev/Next navigation works correctly
- [ ] Search finds the operator by name
- [ ] All component containers load properly

---

## Parameter Documentation

### Export Parameters from TouchDesigner

Get complete JSON parameter export (contact POPX developers for export script). Save as `parameters.json` in operator directory.

### Parameter HTML Structure

**Simple parameters** (Float, Int, Toggle, String, StrMenu):
```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Parameter Label</span>
    <span class="param-name">Paramname</span>
    <span class="param-separator">–</span>
    <span class="param-description">What this parameter does.</span>
  </div>
</div>
```

**Grouped parameters** (Menu, Vec3, RGB, Vec2):
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Parameter Label</span>
    <span class="param-name">Paramname</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">What this parameter does.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Sub-Parameter Label</span>
      <span class="param-name">subparamname</span>
    </div>
    <!-- More sub-parameters -->
  </div>
</div>
```

---

## Parameter Types Reference

### Menu Parameters (`style: "Menu"`)

**Uses sub-parameters from `menuLabels` and `menuNames` arrays.**

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Mode</span>
    <span class="param-name">Mode</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Selects the operation mode.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Add</span>
      <span class="param-name">add</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Multiply</span>
      <span class="param-name">mult</span>
    </div>
  </div>
</div>
```

### StrMenu Parameters (`style: "StrMenu"`)

**NO sub-parameters** - these are dynamic attribute menus:

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

### Vec3/XYZ Parameters (`size: 3`, `style: "XYZ"`)

**Sub-parameters use full label + x/y/z suffix:**

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Translate</span>
    <span class="param-name">T</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Translation offset.</span>
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

### RGB Parameters (`size: 3`, `style: "RGB"`)

**Sub-parameters use full label + r/g/b suffix:**

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Color</span>
    <span class="param-name">Color</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Display color.</span>
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

### Vec2 Parameters (`size: 2`)

**Sub-parameters use full label + x/y suffix:**

```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Scale</span>
    <span class="param-name">Scale</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">2D scale factor.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Scale</span>
      <span class="param-name">Scalex</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Scale</span>
      <span class="param-name">Scaley</span>
    </div>
  </div>
</div>
```

---

## Special Rules for Falloff Operators

All Falloff operators must have **identical** parameter pages:

- **Page: Falloff** - Preview section (Preview Falloff, Falloff Ramp, etc.)
- **Page: Noise** - Noise parameters
- **Page: Remap** - Remapping parameters (Clamp, Fit, Invert, etc.)
- **Page: Common** - Standard common parameters

**Reference:** Copy these pages exactly from existing Falloff operators (Shape Falloff, Radial Falloff) to ensure consistency.

---

## Common Mistakes to Avoid

❌ **Wrong:** Using component letters for Vec3/RGB labels
```html
<span class="param-label">X</span>
```

✅ **Correct:** Using full parameter label
```html
<span class="param-label">Translate</span>
```

❌ **Wrong:** Adding sub-parameters to StrMenu
```html
<div class="param-group">  <!-- Don't use param-group for StrMenu -->
```

✅ **Correct:** Treating StrMenu as simple parameter
```html
<div class="parameter-item">  <!-- Use parameter-item -->
```

❌ **Wrong:** Forgetting to update search index
```
Operator doesn't appear in search results
```

✅ **Correct:** Always add to `assets/js/script.js` searchIndex array

❌ **Wrong:** Updating sidebar in all 30+ HTML files
```
Manually editing every page's sidebar
```

✅ **Correct:** Update only `components/sidebar.html`

---

## Quick Checklist

Before finalizing:

- [ ] Directory created in correct category
- [ ] `index.html` created with proper structure
- [ ] **`components/sidebar.html` updated** with new operator link
- [ ] Previous operator's next button updated
- [ ] Next operator's prev button updated
- [ ] **Search index updated** in `assets/js/script.js`
- [ ] All parameters documented with correct structure
- [ ] Menu parameters have all sub-parameters
- [ ] Vec3/RGB use full labels (not X/Y/Z or R/G/B)
- [ ] Component suffixes are lowercase (x, y, z, r, g, b)
- [ ] Page tested - loads without errors
- [ ] Search finds the operator
- [ ] Navigation works from all pages

---

## Summary: What Changed with Modular Architecture

**Before (OLD WAY):**
- Update sidebar in 30+ HTML files manually
- Carefully adjust relative paths for each file
- High risk of errors and inconsistencies

**Now (NEW WAY):**
- Update `components/sidebar.html` **once**
- Component loader handles all paths automatically
- Guaranteed consistency across all pages

This makes adding new operators **much faster and less error-prone**.
