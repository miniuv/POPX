# TouchDesigner Python Script - Set Remap-Falloff Parameter Help Text

op_name = target

# Page: Remap
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Inputattr.help = "Name of the falloff attribute to read values from for remapping."
op_name.par.Outputattr.help = "Name of the attribute to write the remapped falloff values to."
op_name.par.Clamp.help = "When enabled, constrains falloff values to the 0-1 range."
op_name.par.Fit.help = "Enables remapping of falloff values from an input range to an output range."
op_name.par.Auto.help = "Automatically determines input range from actual min/max falloff values."
op_name.par.Inputmin.help = "Minimum value of the input range for remapping."
op_name.par.Inputmax.help = "Maximum value of the input range for remapping."
op_name.par.Outputmin.help = "Minimum value of the output range for remapping."
op_name.par.Outputmax.help = "Maximum value of the output range for remapping."
op_name.par.Absvalue.help = "Converts all falloff values to their absolute values (positive only)."
op_name.par.Invert.help = "Reverses the falloff values (1 - value)."
op_name.par.Enablerampremap.help = "Applies a custom curve defined by a ramp to remap the falloff values."
op_name.par.Openrampeditor.help = "Opens the ramp editor for defining the custom remapping curve."
op_name.par.Resetramp.help = "Resets the remap ramp editor."
op_name.par.Customramptop.help = "Reference to an external TOP for remap control. When specified, overrides the internal ramp editor."

# Page: Falloff
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Fallofframp.help = "Color ramp preset used for visualizing falloff values when Preview Falloff is enabled."
op_name.par.Opencustumrampeditor.help = "Opens the custom color ramp editor for defining a custom falloff visualization gradient."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Converttoptprim.help = "Converts points to primitive points when Render Primitives is toggled off."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner instances."

print("Remap-Falloff parameter help text updated successfully!")
