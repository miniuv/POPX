# TouchDesigner Python Script - Set SA Parameter Help Text

op_name = target

# Page: SA
op_name.par.Solvermode.help = "Switches between Simple and Advect modes."
op_name.par.Pointsupdatepop.help = "Reference to a POP node downstream in the network when Solver Mode is set to Advect."
op_name.par.Strangeattractor.help = "Selects the type of strange attractor to simulate."
op_name.par.Customsa.help = "Reference to a DAT containing custom attractor equations."
op_name.par.Generatedat.help = "Pulse to generate a template script DAT for defining custom attractors."
op_name.par.Ua.help = "Scale factor for coefficient A in attractor equations."
op_name.par.Ub.help = "Scale factor for coefficient B in attractor equations."
op_name.par.Uc.help = "Scale factor for coefficient C in attractor equations."
op_name.par.Ud.help = "Scale factor for coefficient D in attractor equations."
op_name.par.Ue.help = "Scale factor for coefficient E in attractor equations."
op_name.par.Uf.help = "Scale factor for coefficient F in attractor equations."
op_name.par.Timescale.help = "Global time multiplier for simulation speed."
op_name.par.Initializepulse.help = "Pulse to reset simulation and spawn initial particles."
op_name.par.Startpulse.help = "Pulse to begin simulation from initialized state."
op_name.par.Play.help = "Toggle continuous simulation playback."
op_name.par.Steppulse.help = "Pulse to advance simulation by one frame while paused."

# Page: Bounds
op_name.par.Mintype1.help = "Behavior when particles reach minimum bounds on each axis."
op_name.par.Maxtype1.help = "Behavior when particles reach maximum bounds on each axis."
op_name.par.Min1.help = "Lower bound for XYZ position limits."
op_name.par.Max1.help = "Upper bound for XYZ position limits."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("SA parameter help text updated successfully!")
