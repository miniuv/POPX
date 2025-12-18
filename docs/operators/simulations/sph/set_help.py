# TouchDesigner Python Script - Set Sph Parameter Help Text

op_name = target

# Page: SPH
op_name.par.Particlesupdatepop.help = "Reference to a POP node downstream in the network."
op_name.par.Solvermode.help = "Simulation mode: Fluids for liquids with viscosity, Grains for granular."
op_name.par.Substeps.help = "Number of solver substeps per frame."
op_name.par.Iterations.help = "Solver iterations per substep for constraint satisfaction."
op_name.par.Timescale.help = "Global time multiplier for simulation speed."
op_name.par.Timestep.help = "Read-only display of effective timestep, equal to 1/FPS of TouchDesigner."
op_name.par.Numparticles.help = "Particle count when no input connected."
op_name.par.Smoothingradius.help = "Interaction distance for neighbor particle forces."
op_name.par.Maxneighbors.help = "Maximum neighbor count per particle for force calculations."
op_name.par.Initializepulse.help = "Pulse to reset simulation and spawn initial particles."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one frame while paused."

# Page: Properties
op_name.par.Targetdensity.help = "Rest density the solver tries to maintain."
op_name.par.Viscosity.help = "Fluid thickness and resistance to flow."
op_name.par.Cohesion.help = "Particle attraction force creating sticky fluid behavior."
op_name.par.Surfacetension.help = "Force causing droplet formation and surface smoothing."
op_name.par.Adhesion.help = "Particle sticking force to collision surfaces."
op_name.par.Repulsionweight.help = "Strength of particle-particle repulsion force for granular materials."
op_name.par.Attractionweight.help = "Strength of particle-particle attraction for clumping behavior."

# Page: Collisions
op_name.par.Enablegroundcollision.help = "Enables infinite ground plane collision."
op_name.par.Groundpositionx.help = "XYZ position of ground plane."
op_name.par.Displayground.help = "Visualizes ground plane in output."
op_name.par.Enablebbox.help = "Enables box-shaped collision boundary from POP geometry."
op_name.par.Bbox.help = "A reference to a POP defining the bounding box collision bounds."
op_name.par.Displaybbox.help = "Visualizes bounding box collision geometry."
op_name.par.Enablecollisiongeo.help = "Enables collision with arbitrary POP geometry."
op_name.par.Collisiongeo.help = "A reference to a POP defining the collision geometry for surface collision."
op_name.par.Displaycollisiongeo.help = "Visualizes collision geometry in output."
op_name.par.Enablecontainergeo.help = "Enables volumetric container collision using voxelized geometry."
op_name.par.Containertype.help = "Source type for container collision volume."
op_name.par.Containergeo.help = "Reference to a POP geometry to voxelize into collision container."
op_name.par.Maxaxisres.help = "Voxel resolution for container geometry."
op_name.par.Raydirmode.help = "Method for determining ray direction when voxelizing container geometry."
op_name.par.Raydirx.help = "Constant ray direction vector when Ray Direction Mode is set to Constant."
op_name.par.Displaycontainergeo.help = "Visualizes container geometry in output."
op_name.par.Containertop.help = "Reference to a 3D texture containing SDF or T3D volume for container collision."
op_name.par.Toplowerboundsx.help = "Minimum XYZ coordinates of the SDF/T3D volume bounds."
op_name.par.Topupperboundsx.help = "Maximum XYZ coordinates of the SDF/T3D volume bounds."
op_name.par.Forcecollision.help = "Aggressively keeps particles inside container."
op_name.par.Preshrink.help = "Downsamples container volume before blur for performance."
op_name.par.Size.help = "Blur kernel size for smoothing container voxel field."

# Page: Forces
op_name.par.Gravityx.help = "Gravity force vector in world space."
op_name.par.Gravitymultiplier.help = "Scales gravity force magnitude."
op_name.par.Velocitydamping.help = "Global velocity decay per frame."
op_name.par.Staticthreshold.help = "Velocity threshold below which dynamic friction becomes static friction."
op_name.par.Dynamicscale.help = "Dynamic friction coefficient for moving particles."
op_name.par.Limitacc.help = "Clamps particle acceleration to prevent instability."
op_name.par.Maxacc.help = "Maximum allowed acceleration magnitude."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Sph parameter help text updated successfully!")
