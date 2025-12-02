# TouchDesigner Python Script - Set Merge Parameter Help Text

op_name = target

# Page: Merge
op_name.par.Inputs.help = "Sequence of POPX Geometry inputs to merge."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Merge parameter help text updated successfully!")
