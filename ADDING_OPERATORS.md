# Adding New Operator Pages to POPX Docs

This guide explains how to add a new operator page to the POPX documentation, following the established patterns from existing operators like Explode, Convert, and Subdivider.

## Overview

When adding a new operator, you need to:
1. Create the operator HTML file in `/operators`
2. Update all existing operator pages' sidebars
3. Update all root-level pages' sidebars
4. Maintain alphabetical ordering in all menus

## Step 1: Create the Operator HTML File

Create a new file in `/operators/` directory (e.g., `your-operator.html`).

### File Structure Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>POPX Docs | Your Operator Name</title>
  <meta name="description" content="Brief description of your operator.">
  <link rel="icon" type="image/png" href="../assets/images/popx-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
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

  <!-- Top Navigation Bar -->
  <header class="top-bar">
    <a href="../index.html" class="top-bar-logo">
      <span>POPX</span> Docs
    </a>
    <div class="top-bar-search">
      <div class="search-input-wrapper">
        <span class="search-icon">⌕</span>
        <input type="text" placeholder="Search" aria-label="Search">
      </div>
    </div>
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
    <button class="mobile-menu-toggle" aria-label="Toggle menu">☰</button>

    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <!-- Copy the complete sidebar from an existing operator file -->
      <!-- Make sure to include your new operator in alphabetical order -->
    </aside>

    <!-- Main Content -->
    <main class="main-content">
      <h1>Your Operator Name</h1>

      <!-- Summary Section -->
      <section id="summary">
        <h2>Summary</h2>
        <p>
          Description of what your operator does...
        </p>
      </section>

      <!-- Parameters Section -->
      <section id="parameters">
        <h2>Parameters</h2>

        <!-- Main Parameter Page -->
        <h3 id="page-your-operator">Page: Your Operator</h3>

        <!-- Add your parameters here -->

        <hr class="section-divider">

        <!-- Common Page -->
        <h3 id="page-common">Page: Common</h3>

        <div class="parameter-item">
          <div class="param-header">
            <span class="param-label">Free Extra GPU Memory</span>
            <span class="param-name">Freeextragpumem</span>
            <span class="param-separator">–</span>
            <span class="param-description">Free memory that has accumulated when output memory has grown and shrunk.</span>
          </div>
        </div>
      </section>

      <!-- Inputs Section -->
      <section>
        <h2 id="inputs">Inputs</h2>
        <div class="parameter-item">
          <div class="param-header param-header-inline">
            <span class="param-label">Input 0</span>
            <span class="param-separator">–</span>
            <span class="param-name">POP</span>
            <span class="param-separator">–</span>
            <span class="param-text">Geometry</span>
          </div>
        </div>
      </section>

      <!-- Outputs Section -->
      <section>
        <h2 id="outputs">Outputs</h2>
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
        <a href="previous-operator.html" class="nav-button prev">Previous Operator</a>
        <a href="next-operator.html" class="nav-button next">Next Operator</a>
      </nav>
    </main>

    <!-- Table of Contents -->
    <aside class="toc">
      <h4>Contents</h4>
      <ul>
        <li><a href="#summary">Summary</a></li>
        <li><a href="#parameters">Parameters</a>
          <ul>
            <li><a href="#page-your-operator">Page: Your Operator</a></li>
            <li><a href="#page-common">Page: Common</a></li>
          </ul>
        </li>
        <li><a href="#inputs">Inputs</a></li>
        <li><a href="#outputs">Outputs</a></li>
      </ul>
    </aside>
  </div>

  <div class="menu-overlay"></div>
  <script src="../assets/js/script.js"></script>
</body>
</html>
```

## Step 2: Parameter Types

### Simple Parameter
```html
<div class="parameter-item">
  <div class="param-header">
    <span class="param-label">Parameter Label</span>
    <span class="param-name">Parametername</span>
    <span class="param-separator">–</span>
    <span class="param-description">Description of what this parameter does.</span>
  </div>
</div>
```

### Menu Parameter (with options)
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Menu Label</span>
    <span class="param-name">Menuname</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Description of the menu.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">Option 1</span>
      <span class="param-name">option1</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Option 2</span>
      <span class="param-name">option2</span>
    </div>
  </div>
</div>
```

### Vector Parameter (XYZ)
```html
<div class="param-group">
  <div class="param-group-header">
    <span class="param-label">Vector Name</span>
    <span class="param-name">Vectorname</span>
    <span class="param-separator">–</span>
    <span class="param-toggle"></span>
    <span class="param-separator">–</span>
    <span class="param-group-description">Description of the vector.</span>
  </div>
  <div class="param-subparams">
    <div class="param-subparam">
      <span class="param-label">X</span>
      <span class="param-name">Vectornamex</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Y</span>
      <span class="param-name">Vectornamey</span>
    </div>
    <div class="param-subparam">
      <span class="param-label">Z</span>
      <span class="param-name">Vectornamez</span>
    </div>
  </div>
</div>
```

## Step 3: Update Sidebar Navigation

### For Operator Category Pages

The sidebar must be updated in **ALL** HTML files to include your new operator in alphabetical order.

**Important:** Operators must be listed in alphabetical order within their category!

#### Example: Adding to Generators

If adding a Generator called "Instancer" (alphabetically between Explode and Subdivider):

```html
<div class="sidebar-subsection">
  <h4>Generators</h4>
  <div class="sidebar-subsection-content">
    <ul>
      <li><a href="../operators/convert.html">Convert</a></li>
      <li><a href="../operators/explode.html">Explode</a></li>
      <li><a href="../operators/instancer.html">Instancer</a></li>
      <li><a href="../operators/subdivider.html">Subdivider</a></li>
    </ul>
  </div>
</div>
```

### Files to Update

**Operator files** (in `/operators/` directory):
- aim.html
- color-modifier.html
- convert.html
- explode.html
- magnetize.html
- move-along-curve.html
- move-along-mesh.html
- noise-modifier.html
- pivot.html
- randomize.html
- relax.html
- spring-modifier.html
- subdivider.html
- transform-modifier.html
- (any other operator files)

**Root-level files**:
- getting-started.html
- index.html
- installation.html
- tutorials.html
- contact.html
- community.html

### Path Differences

**In operator files** (use `../operators/`):
```html
<li><a href="../operators/your-operator.html">Your Operator</a></li>
```

**In root-level files** (use `operators/`):
```html
<li><a href="operators/your-operator.html">Your Operator</a></li>
```

## Step 4: Automated Update with Bash

You can use bash commands to update all files at once.

### For Operator Files

```bash
for file in operators/*.html; do
  sed -i '/<h4>Generators<\/h4>/,/<\/ul>/{
    /<li><a href="\.\.\/operators\/convert\.html">Convert<\/a><\/li>/d
    /<li><a href="\.\.\/operators\/explode\.html">Explode<\/a><\/li>/d
    /<li><a href="\.\.\/operators\/your-operator\.html">Your Operator<\/a><\/li>/d
    /<li><a href="\.\.\/operators\/subdivider\.html">Subdivider<\/a><\/li>/d
    /<\/ul>/i\                <li><a href="../operators/convert.html">Convert</a></li>\n                <li><a href="../operators/explode.html">Explode</a></li>\n                <li><a href="../operators/your-operator.html">Your Operator</a></li>\n                <li><a href="../operators/subdivider.html">Subdivider</a></li>
  }' "$file"
done
```

### For Root-Level Files

```bash
for file in getting-started.html index.html installation.html tutorials.html contact.html community.html; do
  sed -i '/<h4>Generators<\/h4>/,/<\/ul>/{
    /<li><a href="operators\/convert\.html">Convert<\/a><\/li>/d
    /<li><a href="operators\/explode\.html">Explode<\/a><\/li>/d
    /<li><a href="operators\/your-operator\.html">Your Operator<\/a><\/li>/d
    /<li><a href="operators\/subdivider\.html">Subdivider<\/a><\/li>/d
    /<\/ul>/i\                <li><a href="operators/convert.html">Convert</a></li>\n                <li><a href="operators/explode.html">Explode</a></li>\n                <li><a href="operators/your-operator.html">Your Operator</a></li>\n                <li><a href="operators/subdivider.html">Subdivider</a></li>
  }' "$file"
done
```

## Step 5: Operator Categories

The documentation supports the following operator categories:

- **Generators**: Convert, Explode, Subdivider
- **Falloffs**: Falloff Field, Radial Falloff
- **Modifiers**: Aim, Color Modifier, Magnetize, Move Along Curve, Move Along Mesh, Noise Modifier, Pivot, Randomize, Relax, Spring Modifier, Transform Modifier
- **Tools**: Attribute Manager, Voxelize
- **Simulations**: FLIP Solver, SPH Solver

Add your operator to the appropriate category in alphabetical order.

## Step 6: Important Terminology

### POPX Geometry vs Packed Primitives

**Use:** "POPX Geometry" or "instances"
**Avoid:** "packed primitives" (especially in Generator pages)

**Example:**
```
✓ "transforms regular geometry into POPX Geometry"
✗ "transforms regular geometry into packed primitives"
```

### Attribute Class Order

When listing attribute classes, always use this order:
1. Point
2. Vertex
3. Primitive

## Checklist

Before considering your operator page complete:

- [ ] Created operator HTML file in `/operators/`
- [ ] Added complete summary section
- [ ] Added all parameters with proper formatting
- [ ] Added parameter page sections (h3 tags)
- [ ] Added Inputs and Outputs sections
- [ ] Added Table of Contents with correct links
- [ ] Updated sidebar in the new operator file
- [ ] Updated sidebars in ALL other operator files (alphabetical order)
- [ ] Updated sidebars in ALL root-level files (alphabetical order)
- [ ] Used correct path prefix (`../operators/` vs `operators/`)
- [ ] Verified alphabetical ordering in all menus
- [ ] Used "POPX Geometry" terminology (not "packed primitives" for Generators)
- [ ] Tested page navigation links work correctly

## Examples to Reference

Look at these existing operator pages for reference:

- **Explode** (`operators/explode.html`): Generator with clustering, orientation controls
- **Convert** (`operators/convert.html`): Generator with partitioning, attribute transfer
- **Subdivider** (`operators/subdivider.html`): Generator with falloff, post-processing options

These three examples demonstrate all common parameter types and page structures used in POPX documentation.
