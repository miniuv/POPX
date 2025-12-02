# TouchDesigner Python Script - Set Subdivider Parameter Help Text

op_name = target

# Page: Subdivider
op_name.par.Maxtriangles.help = "Maximum number of triangles allowed in the output geometry."
op_name.par.Subdivisions.help = "Number of subdivision iterations to perform."
op_name.par.Extrudestrength.help = "Controls the peak distance of each extrusion."
op_name.par.Extrusionfalloffexp.help = "Controls how far each extrusion goes compared to the last."
op_name.par.Inset.help = "Amount to inset subdivided faces."
op_name.par.Minarea.help = "Minimum face area threshold for extrusion."
op_name.par.Dofalloff.help = "Enables falloff-based subdivision control."
op_name.par.Falloffattr.help = "Name of the falloff attribute to use for extrusion control."
op_name.par.Postsubdivide.help = "Enables additional subdivision pass after extrusion."
op_name.par.Iterations.help = "Number of post-subdivision iterations."
op_name.par.Creaseweight.help = "Determines how much sharp edges in the geometry should be preserved."
op_name.par.Simplecoeffs.help = "Enables simple coefficient computation when smoothing the interpolated points."
op_name.par.Maxprimsperpoint.help = "Maximum number of primitives a point can be part of in the input geometry."
op_name.par.Angle.help = "For vertex normals, the threshold angle between faces above which the shared."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Subdivider parameter help text updated successfully!")
