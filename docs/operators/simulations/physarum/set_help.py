# TouchDesigner Python Script - Set Physarum Parameter Help Text

op_name = target

# Page: Physarum
op_name.par.Particlesupdatepop.help = "Reference to a POP node downstream in the network."
op_name.par.Trailupdatetop.help = "Reference to a TOP node downstream in the network."
op_name.par.Maxaxisres.help = "Maximum voxel/pixel resolution for longest axis of trail texture."
op_name.par.Numberofparticles.help = "Particle count when no input connected (spawned at initialization)."
op_name.par.Seed.help = "Random seed for particle spawn positions and directions."
op_name.par.Pointsize.help = "Particle render size in 2D mode for trail deposition."
op_name.par.Sensordistancebase.help = "Base distance for sensor probe ahead of particle."
op_name.par.Sensordistancepower.help = "Power function applied to trial-sampled sensor distance variation."
op_name.par.Sensordistancescale.help = "Multiplier for trial-sampled sensor distance variation range."
op_name.par.Sensoranglebase.help = "Base angle offset for sensors from forward direction (degrees)."
op_name.par.Sensoranglepower.help = "Power function applied to trial-sampled sensor angle variation."
op_name.par.Sensoranglescale.help = "Multiplier for trial-sampled sensor angle variation range (degrees)."
op_name.par.Rotationanglebase.help = "Base rotation angle when turning toward detected trails (degrees)."
op_name.par.Rotationanglepower.help = "Power function applied to trial-sampled rotation angle variation."
op_name.par.Rotationanglescale.help = "Multiplier for trial-sampled rotation angle variation range (degrees)."
op_name.par.Movedistancebase.help = "Base distance particles move forward per iteration."
op_name.par.Movedistancepower.help = "Power function applied to trial-sampled move distance variation."
op_name.par.Movedistancescale.help = "Multiplier for trial-sampled move distance variation range."
op_name.par.Decay.help = "Rate at which trails fade over time (0 = permanent, 1 = instant)."
op_name.par.Diffusepasses.help = "Number of blur iterations to spread trails (0 = no diffusion)."
op_name.par.Size.help = "Blur kernel radius (larger = wider spread)."
op_name.par.Initializepulse.help = "Pulse to reset simulation and spawn initial particles."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one iteration while paused."

# Page: Constraint Volume
op_name.par.Constrainttovolume.help = "Confines particle movement within texture-defined regions."
op_name.par.Constraintvolume.help = "Reference to a 2D/3D texture TOP to use as constraint volume when no third."
op_name.par.Forcestrength.help = "Strength of repulsion force from volume boundaries."
op_name.par.Preshrink.help = "Downsamples volume before blur for performance."
op_name.par.Filtersize.help = "Blur kernel size for smoothing volume constraint field."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Physarum parameter help text updated successfully!")
