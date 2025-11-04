## POPX Transform Modifier

### Overview
The **POPX Transform Modifier** applies procedural transformations — translation, rotation, and scaling — to incoming particles or instances.  
It can operate in both **world space** and **local space**, and supports orientation-aware transforms through the `popxOrient` attribute.  
This allows for MOPS-style transformations directly within the POPX ecosystem.

---

### Parameters

| Name | Type | Description |
|------|------|--------------|
| **Translate X / Y / Z** | Float | Applies translation offsets along the corresponding axes. |
| **Rotate X / Y / Z** | Float | Rotates particles or instances around the specified axes (in degrees). |
| **Scale X / Y / Z** | Float | Scales particles along each axis independently. |
| **Uniform Scale** | Float | Applies a uniform scale multiplier to all axes. |
| **Pivot** | XYZ | Defines the pivot position for rotation and scaling operations. |
| **Space** | Menu (Local / World) | Determines whether the transformation occurs in local or world coordinates. |
| **Affect Orientation** | Toggle | When enabled, rotations also modify the `popxOrient` quaternion attribute. |
| **Affect Velocity** | Toggle | When enabled, transformations apply to the `velocity` attribute, keeping it consistent with spatial changes. |
| **Use Delta Transform** | Toggle | Enables relative delta transformation mode (like MOPS Apply Attributes), where changes accumulate over time. |
| **Enable** | Toggle | Enables or disables the transform modifier without removing it from the network. |

---

### Inputs
- **Input 0:** Incoming particle or instance stream.

---

### Outputs
- **Output 0:** Transformed particles or instances with updated position, orientation, and scale attributes.

---

### Attributes Affected
- `P` – Position  
- `v` – Velocity (if *Affect Velocity* is enabled)  
- `popxOrient` – Quaternion orientation (if *Affect Orientation* is enabled)  
- `scale` – Non-uniform scale vector or uniform scale float  

---

### Notes
- Works best when chained with other POPX modifiers like **POPX Noise**, **POPX Magnetize**, or **POPX Instancer**.  
- The `Use Delta Transform` toggle makes it possible to accumulate transformations across frames for animation or procedural rigging effects.  
- All parameters can be keyframed or driven by CHOP channels for interactive motion control.
