# TouchDesigner Python Script - Set Move-Along-Mesh Parameter Help Text

op_name = target

# Page: Move Along Mesh
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Mesh.help = "Reference to a POP for the mesh to attach instances to when no second input is."
op_name.par.Displaymesh.help = "Visualizes the mesh in the viewport."
op_name.par.Initializepulse.help = "Resets the simulation state to initial conditions."
op_name.par.Startpulse.help = "Begins the simulation from the current state."
op_name.par.Play.help = "Toggles simulation playback on or off."
op_name.par.Steppulse.help = "Advances the simulation by one frame."

# Page: Attach
op_name.par.Locktomesh.help = "Locks the initial attachment positions so they don't need to be recalculated."
op_name.par.Reattachtomesh.help = "Recomputes attachment points for all instances."
op_name.par.Seed.help = "Random seed value for scatter-based attachment."
op_name.par.Searchradius.help = "Maximum distance for finding nearest attachment points when using Nearest Point."
op_name.par.Maintainoffset.help = "Blend amount for maintaining the original offset distance from the mesh surface."
op_name.par.Maintainorientoffset.help = "Blend amount between the original orientation and the mesh orientation."
op_name.par.Visualizeoffset.help = "Displays lines showing the offset between instances and their attachment points."
op_name.par.Fetchoffsetslines.help = "Creates a select POP with the selected offsets lines of the instances for."

# Page: Animate
op_name.par.Dofalloff.help = "Enables falloff-based modulation of movement effects."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that modulate movement."
op_name.par.Speed.help = "Global speed multiplier for instance movement along the mesh."
op_name.par.Randomspeed.help = "Amount of random variation applied to each instance's speed."
op_name.par.Speedseed.help = "Random seed value for speed randomization."
op_name.par.Enablelifetime.help = "Enables lifetime-based effects for instances, causing them to age and."
op_name.par.Life.help = "Base lifetime duration in seconds for each instance."
op_name.par.Lifevariance.help = "Amount of random variation in lifetime duration between 0 (no variance) and 1."
op_name.par.Lifeseed.help = "Random seed value for lifetime variance."
op_name.par.Outputlifeattrs.help = "Outputs LifeTime and Age attributes for each instance when enabled."
op_name.par.Scalebyage.help = "Enables age-based scale modulation using a ramp curve."
op_name.par.Openscaleramp.help = "Opens the internal scale ramp editor for creating custom scale curves over."
op_name.par.Resetscaleramp.help = "Resets the scale ramp to default values."
op_name.par.Scaletop.help = "Reference to an external TOP for scale control."
op_name.par.Enablepointrelax.help = "Enables relaxation forces that push instances apart to prevent crowding on the."
op_name.par.Relaxiters.help = "Number of relaxation iterations to perform per frame."
op_name.par.Maxrelaxradius.help = "Maximum distance at which relaxation forces affect neighboring instances."
op_name.par.Maxneighbors.help = "Maximum number of neighboring instances to consider for relaxation calculations."
op_name.par.Relaxstrength.help = "Intensity of the relaxation force."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Move-Along-Mesh parameter help text updated successfully!")
