# TouchDesigner Python Script - Set Delete Parameter Help Text

op_name = target

# Page: Delete
op_name.par.Cpureadback.help = "Enable copying the point count and topology information held on the GPU to the."

# Page: Attribute
op_name.par.Attr.help = "Start of Sequential Parameter Blocks to create new attributes."
op_name.par.Attr0inattr.help = "Name of attribute for conditions."
op_name.par.Attr0func.help = "Comparison function used to determine which elements are selected based on its."
op_name.par.Attr0value.help = "Attribute value."
op_name.par.Attr0invert.help = "Invert the selection resulting from the current conditions in the block."

# Page: Thin
op_name.par.Thinenabled.help = "Enable thinning by index range, index step or random index."
op_name.par.Thinoutrange.help = "Enable index-based point filtering."
op_name.par.Thinrangestart.help = "Determines the starting index for range-based point filtering."
op_name.par.Thinrangelength.help = "Determines the number of points being filtered by index range."
op_name.par.Thinstep.help = "Filters every Nth point."
op_name.par.Thinrandom.help = "Determines the proportion of points randomly filtered."
op_name.par.Thinrandomseed.help = "Sets the random seed for points being randomly filtered."
op_name.par.Thininvert.help = "Invert the selection resulting from the current conditions in the block."

# Page: Pattern
op_name.par.Pattern.help = "Start of Sequential Parameter Blocks for index-matching pattern."
#op_name.par.Pattern0pattern.help = "Index-matching pattern."
#op_name.par.Pattern0invert.help = "Invert the selection resulting from the current conditions in the block."

# Page: Group
op_name.par.Group.help = "Start of Sequential Parameter Blocks for input groups."
#op_name.par.Group0name.help = "The name of the group to use."
#op_name.par.Group0invert.help = "Invert the selection resulting from the current conditions in the block."

# Page: Bounding
op_name.par.Bound.help = "Start of Sequential Parameter Blocks for bounding volumes."
#op_name.par.Bound0inattr.help = "Name of position attribute."
#op_name.par.Bound0type.help = "Bounding volume type."
#op_name.par.Bound0translate.help = "Translate the bounding volume."
#op_name.par.Bound0rotate.help = "Rotate the bounding volume."
#op_name.par.Bound0scale.help = "Scale the bounding volume."
#op_name.par.Bound0invert.help = "Invert the selection resulting from the current conditions in the block."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Delete parameter help text updated successfully!")
