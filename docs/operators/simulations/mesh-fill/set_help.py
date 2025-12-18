# TouchDesigner Python Script - Set Mesh-Fill Parameter Help Text

op_name = target

# Page: Mesh Fill
op_name.par.Timestep.help = "Controls simulation speed per frame (higher values = faster filling)."
op_name.par.Switchtovol.help = "Use 3D texture input instead of mesh geometry for density field."
op_name.par.Normalizeinputmesh.help = "Scale input mesh to unit size before voxelization."
op_name.par.Maxaxisres.help = "Voxel grid resolution for mesh-to-volume conversion (higher = more detail)."
op_name.par.Raydirmode.help = "Method for determining ray direction during voxelization."
op_name.par.Raydirx.help = "Direction vector for ray casting when Ray Direction Mode is set to Constant."
op_name.par.Precision.help = "Texture precision for density field."
op_name.par.Fillsurface.help = "Restricts particles to surface boundary instead of filling entire volume."
op_name.par.Radius.help = "Particle spacing radius controlling packing density (smaller = tighter packing)."
op_name.par.Filterscale.help = "Multiplier for density field filtering iterations."
op_name.par.Size.help = "Blur kernel size for density field smoothing."
op_name.par.Initializepulse.help = "Pulse to reset simulation and prepare density field."
op_name.par.Startpulse.help = "Pulse to begin filling simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."

# Page: Seed
op_name.par.Spawn.help = "Enables spawning new particles from density field during simulation."
op_name.par.Seedcount.help = "Number of seed particles to spawn per frame when spawning enabled."
op_name.par.Seed.help = "Random seed for particle spawn positions."
op_name.par.Maxattempts.help = "Maximum spawn position attempts before giving up (prevents infinite loops)."

# Page: Trails
op_name.par.Enabletrails.help = "Enables trail geometry generation showing particle movement paths."
op_name.par.Length.help = "Maximum trail length in frames (history buffer size)."
op_name.par.Filtertype.help = "Smoothing filter for trail curve (gaussian, catmull-rom, etc.)."
op_name.par.Filterdist.help = "Distance metric for edge filtering along trail curves."
op_name.par.Effect.help = "Smoothing effect strength (0 = no smoothing, 1 = full effect)."
op_name.par.Endpointsfixed.help = "Prevents smoothing from moving trail endpoints."

# Page: Lookup
op_name.par.Lookuptrails.help = "Samples the trails texture onto input geometry."
op_name.par.Applyblurtrails.help = "Applies blur filtering to the trails texture before sampling."
op_name.par.Preshrinktrials.help = "Resolution reduction before applying blur for trails texture."
op_name.par.Sizetrials.help = "Blur kernel size for trails texture smoothing."
op_name.par.Lookupfilledvol.help = "Samples the filled volume texture onto input geometry."
op_name.par.Outputinverted.help = "Also outputs the inverted filled volume texture."
op_name.par.Applyblurvol.help = "Applies blur filtering to the filled volume texture before sampling."
op_name.par.Preshrinkvol.help = "Resolution reduction before applying blur for filled volume texture."
op_name.par.Sizevol.help = "Blur kernel size for filled volume texture smoothing."
op_name.par.Lookupoffsetx.help = "Offset applied to lookup coordinates when sampling textures."
op_name.par.Lookupscalex.help = "Scale applied to lookup coordinates when sampling textures."
op_name.par.Debug.help = "Selects which texture to visualize for debugging."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Mesh-Fill parameter help text updated successfully!")
