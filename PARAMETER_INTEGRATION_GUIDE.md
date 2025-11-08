# Parameter Integration Guide

This guide documents the process of reading TouchDesigner operator JSON parameter data and integrating it into POPX documentation operator pages.

## Table of Contents

1. [Overview](#overview)
2. [JSON Parameter Structure](#json-parameter-structure)
3. [HTML Parameter Structure](#html-parameter-structure)
4. [Parameter Types](#parameter-types)
5. [Integration Process](#integration-process)
6. [Examples](#examples)
7. [Best Practices](#best-practices)

---

## Overview

POPX operator parameters are exported from TouchDesigner as JSON data. This data contains all parameter information including labels, names, types, menu options, and metadata. The integration process transforms this JSON data into structured HTML documentation.

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

- **Menu**: Dropdown menu with predefined options
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

### 1. Menu Parameters

Menu parameters have multiple predefined options.

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
