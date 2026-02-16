# TouchDesigner Python Script - Set Convert Parameter Help Text

op_name = target

# Page: Convert
op_name.par.Partitionmethod.help = "Determines how geometry is partitioned into instances."
op_name.par.Numberofpieces.help = "Maximum number of pieces to allocate memory for."
op_name.par.Inputpointcount.help = "Number of points in the input geometry."
op_name.par.Piecesdetected.help = "Read-only display of the number of pieces detected by connectivity."
op_name.par.Minpointsperpiece.help = "Minimum number of points required for a piece."
op_name.par.Searchpasses.help = "Number of passes to search for connectivity."
op_name.par.Attrclass.help = "Type of attribute to use for piece partitioning."
op_name.par.Pieceattr.help = "Name of the attribute to use for partitioning."
op_name.par.Transferattrs.help = "Attributes to transfer to the instances."
op_name.par.Generatenormals.help = "Generates vertex normals for the output geometry."
op_name.par.Maxprimsperpoint.help = "Maximum number of primitives a point can be part of in the input geometry."
op_name.par.Angle.help = "Threshold angle between faces above which shared edge vertices don't share."
op_name.par.Visualizepieces.help = "Enables color visualization of pieces."
op_name.par.Visualizationseed.help = "Random seed for visualization colors."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Convert parameter help text updated successfully!")
