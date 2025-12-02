# TouchDesigner Python Script - Set Attribute-To-Index Parameter Help Text

op_name = target

# Page: Index
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Inputattr.help = "Name of the attribute to read and remap to index values."
op_name.par.Inputattrrange1.help = "Minimum and maximum values of the input attribute range to remap from."
op_name.par.Indexsteps.help = "Number of discrete index values to generate (number of variations)."
op_name.par.Indexstart.help = "Starting integer value for the index range."
op_name.par.Outputattr.help = "Name of the attribute to write index values to."
op_name.par.Debugcolor.help = "When enabled, visualizes index values using vertex colors for debugging."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Attribute-To-Index parameter help text updated successfully!")
