# TouchDesigner Python Script - Set Color-Modifier Parameter Help Text

op_name = target

# Page: Color
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that drive the color ramp."
op_name.par.Openramp.help = "Opens the internal ramp editor for customizing the color gradient."
op_name.par.Resetramp.help = "Resets the internal ramp to default gradient values."
op_name.par.Ramptop.help = "Reference to an external Ramp TOP for color palette."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Color-Modifier parameter help text updated successfully!")
