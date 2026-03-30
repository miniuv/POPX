# TouchDesigner Python Script - Set Dla Parameter Help Text

op_name = target

# Page: DLA
op_name.par.Walkersupdatepop.help = "Reference to a POP node downstream in the network. This creates a feedback loop that re-injects the seed points each frame."
op_name.par.Simboundsx.help = "Defines the XYZ boundaries for particle simulation and diffusion."
op_name.par.Displaybounds.help = "Visualizes the simulation bounds in the viewport."
op_name.par.Displayrandomwalkers.help = "Shows the diffusing random walker particles in the viewport."
op_name.par.Displaydlapoints.help = "Shows the DLA structure as points in the viewport."
op_name.par.Displaydlalines.help = "Shows the DLA structure as connected lines in the viewport."
op_name.par.Maxpoints.help = "Maximum number of diffusing particles in the simulation."
op_name.par.Seed.help = "Random seed for particle spawn positions and diffusion paths."
op_name.par.Maxsearchdist.help = "Maximum distance particles search for attachment points (affects branch density)."
op_name.par.Attachdist.help = "Distance threshold for particles to stick to the structure (smaller = finer detail)."
op_name.par.Attachstrength.help = "Controls the strength of the attachment force when particles approach the structure."
op_name.par.Maxneighbors.help = "Maximum number of neighboring structure points considered for attachment."
op_name.par.Internalnoise.help = "Enable internal noise for randomized particle diffusion."
op_name.par.Noiseamp.help = "Controls the amplitude of the internal noise applied to particle movement."
op_name.par.Initializepulse.help = "Pulse to reset simulation and create initial seed point."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one frame while paused."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Dla parameter help text updated successfully!")
