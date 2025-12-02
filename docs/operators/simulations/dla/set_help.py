# TouchDesigner Python Script - Set Dla Parameter Help Text

op_name = target

# Page: DLA
op_name.par.Seedupdatepop.help = "Reference to a POP node downstream in the network. This creates a feedback loop that re-injects the seed points each frame."
op_name.par.Simboundsx.help = "Defines the XYZ boundaries for particle simulation and diffusion."
op_name.par.Maxpoints.help = "Maximum number of diffusing particles in the simulation."
op_name.par.Maxsearchdist.help = "Maximum distance particles search for attachment points (affects branch."
op_name.par.Attachdist.help = "Distance threshold for particles to stick to the structure (smaller = finer."
op_name.par.Attachstrength.help = "Controls the strength of the attachment force when particles approach the structure."
op_name.par.Seed.help = "Random seed for particle spawn positions and diffusion paths."
op_name.par.Internalnoise.help = "Enable internal noise for randomized particle diffusion."
op_name.par.Noiseamp.help = "Controls the amplitude of the internal noise applied to particle movement."
op_name.par.Initializepulse.help = "Pulse to reset simulation and create initial seed point."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one frame while paused."

# Page: Outputs
op_name.par.Mesh.help = "Header for mesh output settings."
op_name.par.Polygonize.help = "Converts point cloud to polygonal mesh using marching cubes algorithm."
op_name.par.Gridres.help = "Voxel grid resolution for mesh generation (higher = more detail, slower)."
op_name.par.Enableblur.help = "Applies smoothing filter to mesh before polygonization."
op_name.par.Preshrink.help = "Downsamples volume before blur for performance (1 = no downsample)."
op_name.par.Size.help = "Blur kernel size (larger = smoother, more computation)."
op_name.par.Resmult.help = "Resolution multiplier for final polygonization."
op_name.par.Threshold.help = "Isosurface threshold for mesh extraction (lower = thicker mesh)."
op_name.par.Uniquepoints.help = "Generate unique vertices per triangle (no shared points)."
op_name.par.Nmlmethod.help = "Method for computing point normals."
op_name.par.Nmlstepmul.help = "Multiplier for gradient step size when computing normals."
op_name.par.Allocfract.help = "Fraction of maximum memory allocation for mesh generation."
op_name.par.Volume.help = "Generates volumetric TOP output for rendering with volume materials."
op_name.par.Maxaxisres.help = "Maximum resolution along the longest axis of the volume texture."
op_name.par.Densityscale.help = "Multiplier for volume opacity (higher = more opaque)."
op_name.par.Enablevolblur.help = "Applies smoothing filter to volume texture."
op_name.par.Volblurpreshrink.help = "Resolution reduction before applying blur for performance optimization."
op_name.par.Volblursize.help = "Size of the blur filter kernel."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Dla parameter help text updated successfully!")
