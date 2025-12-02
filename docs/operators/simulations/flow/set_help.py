# TouchDesigner Python Script - Set Flow Parameter Help Text

op_name = target

# Page: Flow
op_name.par.Reset.help = "Pulse to clear simulation and reset to initial state."
op_name.par.Timestep.help = "Simulation speed multiplier per frame (higher = faster evolution)."
op_name.par.Maxaxisres.help = "Maximum voxel resolution for longest axis (other axes scale proportionally)."
op_name.par.Veldissipation.help = "Rate at which velocity decays over time (0 = no damping, 1 = instant decay)."
op_name.par.Pressureiters.help = "Number of iterations for pressure solve (higher = more accurate."
op_name.par.Viscosity.help = "Fluid thickness controlling resistance to flow (0 = inviscid, higher = thicker)."
op_name.par.Diffusioniters.help = "Solver iterations for viscosity diffusion (only active when viscosity > 0)."
op_name.par.Vorticity.help = "Vorticity confinement strength to restore rotational motion (creates swirling."
op_name.par.Dissipation.help = "Rate at which substance density fades over time (higher = faster fade)."

# Page: Inputs
op_name.par.Inject.help = "Enables injection of substance into the simulation."
op_name.par.Injectionpop.help = "Reference to a POP containing points to use as injection points when no first."
op_name.par.Injectscale.help = "Scale multiplier for injection area."
op_name.par.Injectgain.help = "Amount of substance added per injection point."
op_name.par.Injectstrength.help = "Strength of force applied at injection points."
op_name.par.Injecttemp.help = "Temperature value for injected substance."
op_name.par.Addsource.help = "Enables continuous source emission into simulation."
op_name.par.Substancegain.help = "Multiplier for substance density from 3D texture source."
op_name.par.Forcestrength.help = "Multiplier for force computed internally from change in density."
op_name.par.Temperaturegain.help = "Multiplier for temperature from alpha channel of 3D texture source."

# Page: Forces
op_name.par.Applybuoyancy.help = "Enables temperature-based buoyancy force (hot rises, cold sinks)."
op_name.par.Buoyancystrength.help = "Overall scale for buoyancy force magnitude."
op_name.par.Gasweight.help = "Density-based downward force (creates heavy smoke effect)."
op_name.par.Coolingrate.help = "Rate at which temperature decreases over time."
op_name.par.Expansion.help = "Volume expansion from heating (creates outward push)."
op_name.par.Applygravity.help = "Enables uniform gravity force on velocity field."
op_name.par.Gravitystrength.help = "Multiplier for gravity force magnitude."
op_name.par.Surfacelevel.help = "Y-position where gravity begins to take effect."
op_name.par.Addexternalforce.help = "Enables custom 3D vector field force from texture."
op_name.par.Externalforcetop.help = "3D texture containing RGB velocity force vectors."
op_name.par.Extforcestrength.help = "Multiplier for external force magnitude."
op_name.par.Addopticalflowforce.help = "Enables force from 3D optical flow texture."
op_name.par.Opticalflowtop.help = "3D texture input for optical flow motion vector computation."
op_name.par.Optiflowforcestrength.help = "Multiplier for optical flow force magnitude."

# Page: Collisions
op_name.par.Enablebounds.help = "Enables collision boundaries at simulation volume edges."
op_name.par.Boundstop.help = "Optional 3D texture defining custom boundary regions."
op_name.par.Showbounds.help = "Visualizes boundary regions in output."
op_name.par.Obstacletop.help = "3D texture defining solid obstacle regions (white = solid)."
op_name.par.Renderobstacle.help = "Includes obstacle visualization in output."
op_name.par.Obstacleopacity.help = "Opacity multiplier for rendered obstacles."

# Page: Advect
op_name.par.Advect.help = "Enables particle system advection by fluid velocity field."
op_name.par.Particlesupdatepop.help = "Reference to a POP node downstream in the network."
op_name.par.Advectionstep.help = "Multiplier for particle advection speed."
op_name.par.Spawn.help = "Spawns particles in regions with substance density above threshold."
op_name.par.Numparticles.help = "Maximum particles spawned."
op_name.par.Threshold.help = "Minimum substance density required for particle spawning."
op_name.par.Seed.help = "Random seed for particle spawn positions."
op_name.par.Maxattempts.help = "Maximum spawn attempts per frame before giving up."
op_name.par.Enableparticlelife.help = "Enables finite particle lifespans with automatic death."
op_name.par.Lifeseed.help = "Random seed for lifespan variance."
op_name.par.Lifespan.help = "Base lifespan in seconds before particle dies."
op_name.par.Lifevariance.help = "Random variation added to base lifespan."
op_name.par.Lookupcolor.help = "Particles inherit color from substance field at spawn position."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Flow parameter help text updated successfully!")
