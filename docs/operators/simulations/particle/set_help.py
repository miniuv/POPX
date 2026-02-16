# TouchDesigner Python Script - Set Particle Parameter Help Text

op_name = target

# Page: Particle
op_name.par.Solvermode.help = "Switches between Simple and Advect modes."
op_name.par.Particlesupdatepop.help = "Reference to a POP node downstream in the network."
op_name.par.Materialmode.help = "Simulation mode: Fluids for liquids with viscosity, Grains for granular."
op_name.par.Substeps.help = "Number of solver substeps per frame."
op_name.par.Iterations.help = "Solver iterations per substep for constraint satisfaction."
op_name.par.Timescale.help = "Global time multiplier for simulation speed."
op_name.par.Timestep.help = "Read-only display of effective timestep, equal to 1/FPS of TouchDesigner."
op_name.par.Smoothingradius.help = "Interaction distance for neighbor particle forces."
op_name.par.Distribution.help = "Neighbor distribution method for particle interactions."
op_name.par.Numhashbuckets.help = "Number of hash buckets for spatial neighbor lookups."
op_name.par.Maxneighbors.help = "Maximum neighbor count per particle for force calculations."
op_name.par.Initializepulse.help = "Pulse to reset simulation and spawn initial particles."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one frame while paused."

# Page: Properties
op_name.par.Targetdensity.help = "Rest density the solver tries to maintain. Enabled in Fluids-SPH and Fluids-PBF modes."
op_name.par.Pressuremulti.help = "Scales pressure force magnitude. Enabled in Fluids-SPH mode."
op_name.par.Nearpressuremult.help = "Scales near-field pressure forces for close-range particle repulsion. Enabled in Fluids-SPH mode."
op_name.par.Viscosity.help = "Fluid thickness and resistance to flow. Enabled in Fluids-SPH and Fluids-PBF modes."
op_name.par.Cohesion.help = "Particle attraction force creating sticky fluid behavior. Enabled in Fluids-PBF mode."
op_name.par.Surfacetension.help = "Force causing droplet formation and surface smoothing. Enabled in Fluids-PBF mode."
op_name.par.Adhesion.help = "Particle sticking force to collision surfaces. Enabled in Fluids-PBF mode."
op_name.par.Repulsionweight.help = "Strength of particle-particle repulsion force for granular materials. Enabled in Grains mode."
op_name.par.Attractionweight.help = "Strength of particle-particle attraction for clumping behavior. Enabled in Grains mode."

# Page: Collisions
op_name.par.Enablegroundcollision.help = "Enables infinite ground plane collision."
op_name.par.Groundpositionx.help = "XYZ position of ground plane."
op_name.par.Displayground.help = "Visualizes ground plane in output."
op_name.par.Enablebboxcollision.help = "Enables box-shaped collision boundary from POP geometry."
op_name.par.Bbox.help = "A reference to a POP defining the bounding box collision bounds."
op_name.par.Bboxlowerbounds1.help = "Toggle to enable lower bounding planes for XYZ axes."
op_name.par.Bboxupperbounds1.help = "Toggle to enable upper bounding planes for XYZ axes."
op_name.par.Bboxmargin.help = "Extra margin distance added to the bounding box collision boundary."
op_name.par.Displaybbox.help = "Visualizes bounding box collision geometry."
op_name.par.Collisiontype.help = "Selects the collision geometry type for constraining particle movement."
op_name.par.Solid.help = "Treats the collision geometry as a solid volume, preventing particles from passing through."
op_name.par.Project.help = "Projects particles onto the surface of the collision geometry."
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

# Page: Forces
op_name.par.Gravityx.help = "Gravity force vector in world space."
op_name.par.Gravitymultiplier.help = "Scales gravity force magnitude."
op_name.par.Velocitydamping.help = "Global velocity decay per frame."
op_name.par.Collisiondamping.help = "Amount of velocity dampening applied when particles collide with collision geometry."
op_name.par.Staticthreshold.help = "Velocity threshold below which dynamic friction becomes static friction."
op_name.par.Dynamicscale.help = "Dynamic friction coefficient for moving particles."
op_name.par.Limitacc.help = "Clamps particle acceleration to prevent instability."
op_name.par.Maxacc.help = "Maximum allowed acceleration magnitude."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Particle parameter help text updated successfully!")
