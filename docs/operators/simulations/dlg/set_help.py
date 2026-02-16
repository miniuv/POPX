# TouchDesigner Python Script - Set Dlg Parameter Help Text

op_name = target

# Page: DLG
op_name.par.Lineupdatepop.help = "Reference to a POP node downstream in the network. This reference will cause a feedback loop and re-injects the line geometry next frame."
op_name.par.Maxverts.help = "Vertex limit to prevent infinite growth and control complexity."
op_name.par.Growthstrength.help = "Rate of edge subdivision and line growth per iteration."
op_name.par.Mass.help = "Per-vertex mass controlling resistance to growth forces."
op_name.par.Maxdistance.help = "Search radius for neighbor proximity checks (smaller = denser growth)."
op_name.par.Distribution.help = "Distribution method for neighbor search queries."
op_name.par.Numhashbuckets.help = "Number of hash buckets for spatial neighbor lookups."
op_name.par.Maxneighbors.help = "Maximum neighbor count before edge subdivision triggers."
op_name.par.Linestrips.help = "Close (connected loops) or Open (line segments with endpoints)."
op_name.par.Filtertype.help = "Smoothing filter algorithm (gaussian, box, etc.) for line curves."
op_name.par.Filterdist.help = "Smoothing kernel size along edges (larger = smoother curves)."
op_name.par.Effect.help = "Blend amount between original and smoothed positions (0-1)."
op_name.par.Initializepulse.help = "Pulse to reset simulation with initial line geometry."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one iteration while paused."

# Page: Collisions
op_name.par.Mintype1.help = "Method for enforcing the minimum position limit per axis."
op_name.par.Maxtype1.help = "Method for enforcing the maximum position limit per axis."
op_name.par.Min1.help = "Lower bound for XYZ position limits."
op_name.par.Max1.help = "Upper bound for XYZ position limits."
op_name.par.Collisiontype.help = "Selects the collision geometry type for constraining line growth."
op_name.par.Collisiondamping.help = "Amount of velocity dampening applied when vertices collide with the collision geometry."
op_name.par.Solid.help = "Treats the collision geometry as a solid volume, preventing vertices from passing through."
op_name.par.Project.help = "Projects vertices onto the surface of the collision geometry."
op_name.par.Collisionpop.help = "Reference to a POP containing the collision geometry when using POP collision type."
op_name.par.Collisionoffset.help = "Offset distance from the collision surface to prevent z-fighting artifacts."
op_name.par.Sizex.help = "Size of the box collision geometry."
op_name.par.Radiusx.help = "Radius of the collision geometry per axis."
op_name.par.Cornerradius.help = "Radius of rounded corners on the box collision geometry."
op_name.par.Collisontop.help = "Reference to a TOP texture used as the collision field for SDF and texture collision types."
op_name.par.Usecustombounds.help = "Enables custom bounding box for the collision texture instead of using the texture's native bounds."
op_name.par.Lowerboundsx.help = "Lower bounds of the collision volume in world space."
op_name.par.Upperboundsx.help = "Upper bounds of the collision volume in world space."
op_name.par.Xord.help = "Sets the order of scale, rotate, and translate operations for the collision geometry transform."
op_name.par.Rord.help = "Sets the order of rotation operations for the collision geometry transform."
op_name.par.Tx.help = "Translation of the collision geometry in world space."
op_name.par.Rx.help = "Rotation of the collision geometry in degrees."
op_name.par.Sx.help = "Scale of the collision geometry per axis."
op_name.par.Px.help = "Pivot point for the collision geometry transform."
op_name.par.Scale.help = "Uniform scale factor applied to the collision geometry."
op_name.par.Displaygeo.help = "Shows the collision geometry in the viewport for visualization."
op_name.par.Displaycolorr.help = "Display color for the collision geometry visualization."

# Page: Noise
op_name.par.Applynoise.help = "Replaces the Mass attribute with noise to create varied growth."
op_name.par.Type.help = "Noise algorithm type and dimensionality."
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
