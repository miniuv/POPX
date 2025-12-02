# TouchDesigner Python Script - Set Extract-Attributes Parameter Help Text

op_name = target

# Page: Extract
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Extractfullxform.help = "Extracts complete transformation data including position, rotation, and scale as point attributes. Also extracts the full transform matrix attribute and the transform attribute (rotation and scale matrix)."
op_name.par.Extractpivot.help = "Extracts pivot point data as Pivot attribute."
op_name.par.Extractpopxorient.help = "Extracts popxOrient attribute as Orient attribute."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Extract-Attributes parameter help text updated successfully!")
