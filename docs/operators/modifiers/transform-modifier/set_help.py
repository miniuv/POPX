# TouchDesigner Python Script - Set Transform-Modifier Parameter Help Text

op_name = target

# Page: Transform
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Localspace.help = "Apply the transform in local or world space."
op_name.par.Dofalloff.help = "Enables falloff influence for the transform."
op_name.par.Falloffattr.help = "Selects the attribute that controls falloff strength."
op_name.par.Scale.help = "Specifies a uniform scale factor in all axes."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Transform-Modifier parameter help text updated successfully!")
