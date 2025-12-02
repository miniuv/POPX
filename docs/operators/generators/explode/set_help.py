# TouchDesigner Python Script - Set Explode Parameter Help Text

op_name = target

# Page: Define Pieces
op_name.par.Numberofclusters.help = "Specifies the number of clusters to create."
op_name.par.Clustersseed.help = "Random seed value for cluster generation."
op_name.par.Maxdistance.help = "Maximum distance threshold for clustering."
op_name.par.Visualizepieces.help = "Enables color visualization of pieces."
op_name.par.Visualizationseed.help = "Random seed for visualization colors."

# Page: Orient
op_name.par.Generatenormals.help = "Generates vertex normals for the output geometry."
op_name.par.Maxprimsperpoint.help = "Maximum number of primitives a point can be part of in the input geometry."
op_name.par.Angle.help = "Threshold angle between faces above which shared edge vertices don't share."
op_name.par.Computesourceorient.help = "Computes orientation based on the input geometry."
op_name.par.Usecustomupvector.help = "Enables custom up vector specification."
op_name.par.Invertn.help = "Inverts the normal vector direction."
op_name.par.Invertup.help = "Inverts the up vector direction."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Explode parameter help text updated successfully!")
