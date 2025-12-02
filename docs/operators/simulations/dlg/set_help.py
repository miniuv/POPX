# TouchDesigner Python Script - Set Dlg Parameter Help Text

op_name = target

# Page: DLG
op_name.par.Lineupdatepop.help = "Reference to a POP node downstream in the network. This reference will cause a feedback loop and re-injects the line geometry next frame."
op_name.par.Growthstrength.help = "Rate of edge subdivision and line growth per iteration."
op_name.par.Usecurvature.help = "Influences growth direction based on line curvature for varied branching."
op_name.par.Maxdistance.help = "Search radius for neighbor proximity checks (smaller = denser growth)."
op_name.par.Maxneighbors.help = "Maximum neighbor count before edge subdivision triggers."
op_name.par.Maxverts.help = "Vertex limit to prevent infinite growth and control complexity."
op_name.par.Linestrips.help = "Close (connected loops) or Open (line segments with endpoints)."
op_name.par.Filtertype.help = "Smoothing filter algorithm (gaussian, box, etc.) for line curves."
op_name.par.Filterdist.help = "Smoothing kernel size along edges (larger = smoother curves)."
op_name.par.Effect.help = "Blend amount between original and smoothed positions (0-1)."
op_name.par.Initializepulse.help = "Pulse to reset simulation with initial line geometry."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one iteration while paused."

# Page: Bounds
op_name.par.Min1.help = "Lower bound for XYZ position limits."
op_name.par.Max1.help = "Upper bound for XYZ position limits."

# Page: Constraint Geometry
op_name.par.Constrainttogeo.help = "Projects line vertices onto collision geometry surface."
op_name.par.Constraintgeo.help = "Reference to a POP geometry to use as constraint surface when no second input."
op_name.par.Displaygeo.help = "Visualizes constraint geometry in output."

# Page: Constraint Volume
op_name.par.Constrainttovolume.help = "Confines line growth within 2D/3D texture-defined volume."
op_name.par.Constraintvolume.help = "Reference to a 2D/3D texture TOP to use as constraint volume when no third."
op_name.par.Forcestrength.help = "Strength of repulsion force from volume boundaries."
op_name.par.Preshrink.help = "Downsamples volume before blur for performance."
op_name.par.Size.help = "Blur kernel size for smoothing volume constraint field."

# Page: Noise
op_name.par.Applynoise.help = "Applies perlin noise to the PointScale attribute to create varied growth."
op_name.par.Seed.help = "Numerical value that initializes the randomization."
op_name.par.Period.help = "Period (scale) of the noise field."
op_name.par.Harmon.help = "The number of higher frequency components to layer on top of the base frequency."
op_name.par.Spread.help = "The factor by which the frequency of a harmonic increases relative to the."
op_name.par.Gain.help = "Amplitude of the Harmonics layered on top of the base frequency."
op_name.par.Amp.help = "The noise values amplitude (a scale on the values output)."
op_name.par.Exp.help = "Sets the exponent. The internal value is raised by the power of the exponent."
op_name.par.Offset.help = "Constant added to noise output for bias adjustment."
op_name.par.Animate.help = "Time-based noise evolution speed for animated variation."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Dlg parameter help text updated successfully!")
