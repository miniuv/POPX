# TouchDesigner Python Script - Set Voxelize Parameter Help Text

op_name = target

# Page: Voxelize
op_name.par.Maxaxisresolution.help = "Maximum resolution along the longest axis of the voxel grid."
op_name.par.Lowerboundsx.help = "Minimum XYZ coordinates of the voxelization volume."
op_name.par.Upperboundsx.help = "Maximum XYZ coordinates of the voxelization volume."
op_name.par.Margin.help = "Additional padding around the geometry bounds."
op_name.par.Getbounds.help = "Automatically calculate bounds from input geometry."
op_name.par.Displaybounds.help = "Visualize the voxelization volume bounds as a bounding box."
op_name.par.Raydirx.help = "Direction vector for ray casting when Ray Direction Mode is set to Constant."
op_name.par.Enablemaxpointcount.help = "Limits the number of points processed when voxelizing point clouds."
op_name.par.Maxpointcount.help = "Maximum number of points to process for point cloud voxelization."
op_name.par.Overrideifexists.help = "When enabled, uses the Color parameter instead of point color from the geometry."
op_name.par.Colorr.help = "RGB color applied to voxels."
op_name.par.Densityscale.help = "Multiplier for voxel density values."
op_name.par.Bgcolorr.help = "RGB color for empty voxel regions."
op_name.par.Bgalpha.help = "Alpha value for empty voxel regions."
op_name.par.Enableblur.help = "Applies blur filtering to smooth the voxelized volume."
op_name.par.Preshrink.help = "Resolution reduction before applying blur for performance optimization."
op_name.par.Size.help = "Size of the blur filter kernel."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Voxelize parameter help text updated successfully!")
