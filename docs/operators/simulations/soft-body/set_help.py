# TouchDesigner Python Script - Set Soft-Body Parameter Help Text

op_name = target

# Page: Solver
op_name.par.Targetupdatepop.help = "POP operator providing target geometry updates for the simulation."
op_name.par.Timescale.help = "Global time scale multiplier for the simulation speed."
op_name.par.Timestep.help = "Read-only display of effective timestep, equal to 1/FPS of TouchDesigner."
op_name.par.Pressureconst.help = "Enable volume-preserving pressure constraints for closed meshes."
op_name.par.Substeps.help = "Number of simulation substeps per frame for improved stability."
op_name.par.Iterations.help = "Number of constraint solver iterations."
op_name.par.Initializepulse.help = "Pulse to initialize or reset the simulation."
op_name.par.Startpulse.help = "Pulse to start the simulation from its initial state."
op_name.par.Play.help = "Toggle to play or pause the simulation."
op_name.par.Steppulse.help = "Pulse to advance the simulation by one frame when paused."

# Page: Collisions
op_name.par.Enablecollisions.help = "Master toggle for all collision detection and response."
op_name.par.Enablegroundcollision.help = "Enable collision with an infinite ground plane."
op_name.par.Displayground.help = "Visualize the ground plane in the viewport."
op_name.par.Enablebboxcollision.help = "Enable collision with a bounding box volume."
op_name.par.Bbox.help = "A reference to a POP defining the bounding box collision bounds."
op_name.par.Displaybbox.help = "Visualize the bounding box in the viewport."
op_name.par.Enablegeocollision.help = "Enable collision with external geometry from the collision geometry input."
op_name.par.Displaycollider.help = "Visualize the collision geometry in the viewport."
op_name.par.Enableselfcollision.help = "Enable collision detection between different parts of the same soft body as."
op_name.par.Selfcollisionpasses.help = "Number of self-collision detection passes per substep."
op_name.par.Normalcorrection.help = "Use surface normals to improve collision response accuracy."
op_name.par.Maxneighbors.help = "Maximum number of neighbors to consider for self-collision per point."
op_name.par.Maxdistance.help = "Maximum distance for neighbor search when using distance-based neighbors."

# Page: Forces
op_name.par.Gravitymultiplier.help = "Multiplier for the gravity force."
op_name.par.Velocitydamping.help = "Global velocity damping to reduce motion over time. Range 0-1."
op_name.par.Staticthreshold.help = "Velocity threshold below which static friction is applied."
op_name.par.Dynamicscale.help = "Scale factor for dynamic friction forces."
op_name.par.Enableexternal.help = "Enable friction with external collision geometry."
op_name.par.Enableself.help = "Enable friction for self-collisions."
op_name.par.Groundstaticscale.help = "Static friction scale for ground collisions."
op_name.par.Grounddynamicscale.help = "Dynamic friction scale for ground collisions."
op_name.par.Enablegrabber.help = "Enable interactive grabber tool for manipulating points."
op_name.par.Grab.help = "Momentary button to activate grabbing."
op_name.par.Grabpositionx.help = "Position of the grabber in world space."
op_name.par.Grabradiusx.help = "Radius of the grabber influence sphere."
op_name.par.Grabstrength.help = "Strength of the grabber force applied to particles."
op_name.par.Transitionrange.help = "Range of the transition falloff from the grabber edge."
op_name.par.Transitionalign.help = "Alignment offset for the transition falloff."
op_name.par.Transitiontype.help = "Interpolation curve type for the transition falloff."
op_name.par.Displaygrabber.help = "Visualize the grabber sphere in the viewport."
op_name.par.Visgrabbedpoints.help = "Highlight points currently affected by the grabber."

# Page: Advanced
op_name.par.Enablemaxacc.help = "Enable maximum acceleration limiting to prevent instability."
op_name.par.Maxacceleration.help = "Maximum allowed acceleration magnitude."
op_name.par.Limitaccel.help = "Apply acceleration limiting during velocity update step."
op_name.par.Fallbackcollision.help = "Use first order integration when collisions are detected for improved stability."

# Page: Post Process
op_name.par.Postsmoothp.help = "Apply position smoothing after simulation step."

# Page: Visualize
op_name.par.Simulatedgeometry.help = "Display the simulated geometry."
op_name.par.Viscollisions.help = "Visualize collision detection points."
op_name.par.Visselfcollision.help = "Visualize self-collision detection points."
op_name.par.Visthickness.help = "Visualize point thickness values."
op_name.par.Distancealongedges.help = "Visualize distance constraints along mesh edges."
op_name.par.Bendacrosstriangles.help = "Visualize bending constraints across triangle edges."
op_name.par.Struts.help = "Visualize strut constraints."
op_name.par.Attachtogeometry.help = "Visualize attachment constraints to collision geometry."
op_name.par.Pinned.help = "Visualize pinned points."
op_name.par.Displayproperty.help = "Show the selected property visualization on constraints."
op_name.par.Maxvalue.help = "Maximum value for property color mapping range."

print("Soft-Body parameter help text updated successfully!")
