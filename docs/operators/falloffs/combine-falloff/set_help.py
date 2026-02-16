# TouchDesigner Python Script - Set Combine-Falloff Parameter Help Text

op_name = target

# Page: Combine
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Combineop.help = "Mathematical operation used to combine falloff attributes."
op_name.par.Swaporder.help = "Reverses the order of operands in the combination operation (useful for non-commutative operations like subtraction and division)."
op_name.par.Outputfalloffattr.help = "Name of the attribute where the combined falloff result will be stored."
op_name.par.Falloffs.help = "Sequence of falloff inputs to combine. Each entry specifies a POP source, falloff attribute, and gain multiplier."
op_name.par.Falloffs0pop.help = "Reference to the POP operator containing the falloff attribute to combine."
op_name.par.Falloffs0falloffattr.help = "Name of the falloff attribute to read from the specified POP."
op_name.par.Falloffs0gain.help = "Multiplier applied to the falloff value before combining (0.0 to 1.0)."

# Page: Falloff
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Fallofframp.help = "Color ramp preset used for visualizing falloff values when Preview Falloff is enabled."
op_name.par.Opencustumramp.help = "Opens the custom color ramp editor for defining a custom falloff visualization gradient."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Converttoptprim.help = "Converts points to primitive points when Render Primitives is toggled off."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner instances."

print("Combine-Falloff parameter help text updated successfully!")
