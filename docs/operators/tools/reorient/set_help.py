# TouchDesigner Python Script - Set Reorient Parameter Help Text

op_name = target

# Page: Reorient
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Referencegeo.help = "POP geometry to use as reference for transferring orientation."
op_name.par.Maxdistance.help = "Maximum distance to search for nearest neighbor points on reference geometry."
op_name.par.Distribution.help = "Method for selecting neighbor points when using reference geometry."
op_name.par.Quatattr.help = "Name of the quaternion attribute to read when Attribute Type is Quaternion."
op_name.par.Normalattr.help = "Name of the normal vector attribute when Attribute Type is Two Vectors."
op_name.par.Upattr.help = "Name of the up vector attribute when Attribute Type is Two Vectors."
op_name.par.Matrixattr.help = "Name of the matrix attribute to read when Attribute Type is Matrix."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Reorient parameter help text updated successfully!")
