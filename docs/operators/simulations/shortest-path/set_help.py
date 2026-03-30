# TouchDesigner Python Script - Set Shortest Path Parameter Help Text

op_name = target

# Page: Shortest Path
op_name.par.Startgroup.help = "Group defining the start points for pathfinding. Sourced from path geometry, or nearest path points to alternate input if connected."
op_name.par.Endgroup.help = "Group defining the end points for pathfinding. Sourced from path geometry, or nearest path points to alternate input if connected."
op_name.par.Costattrib.help = "Point attribute used as traversal cost weight for pathfinding."
op_name.par.Iterations.help = "Number of solver iterations for path computation."
op_name.par.Nebrtype.help = "Method for determining point connectivity."
op_name.par.Maxdistance.help = "Maximum search distance for neighbor connections. Enabled when Neighbors Type is By Distance."
op_name.par.Numhashbuckets.help = "Number of hash buckets for spatial neighbor lookups. Enabled when Neighbors Type is By Distance."
op_name.par.Maxneighbors.help = "Maximum number of neighbors per point."
op_name.par.Displaylinestrips.help = "Displays the computed paths as line strips in the viewport."
op_name.par.Displaygeo.help = "Displays the path geometry in the viewport."
op_name.par.Visualizationseed.help = "Random seed for visualization colors."
op_name.par.Visualizepaths.help = "Colors each path with a unique color for identification."
op_name.par.Visualizestartend.help = "Highlights start and end points in the viewport."
op_name.par.Visualizecost.help = "Visualizes the cost attribute as a color gradient."
op_name.par.Lockalternate.help = "Locks alternate start and end point locations to prevent recomputation."
op_name.par.Maxpaths.help = "Maximum number of paths to compute."
op_name.par.Maxverts.help = "Maximum number of vertices across all paths."
op_name.par.Cpureadback.help = "Copies path topology information back to CPU for downstream processing."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Shortest Path parameter help text updated successfully!")
