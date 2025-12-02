# TouchDesigner Python Script - Set Magnetize Parameter Help Text

op_name = target

# Page: Magnetize
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Magnetspop.help = "Reference to a POP containing points that define magnet positions and."
op_name.par.Displaymagents.help = "Enables visual display of magnet positions in the viewport."
op_name.par.Dofalloff.help = "Enables falloff-based magnetic force intensity control."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that modulate magnetic."
op_name.par.Searchradius.help = "Maximum distance from magnets within which instances are affected by magnetic."
op_name.par.Relaxfactor.help = "Controls the smoothness and damping of magnetic force application over time."
op_name.par.Radius.help = "Radius of influence for each magnet."
op_name.par.Strength.help = "Intensity of magnetic forces applied to instances."
op_name.par.Spindir.help = "Reverses the spin rotation direction."
op_name.par.Affectrot.help = "Enables rotation changes based on magnetic force direction."
op_name.par.Aimweight.help = "Controls how quickly instances rotate toward their direction of motion when."
op_name.par.Outputweightattr.help = "Outputs a weight attribute showing the strength of magnetic influence on each instance."
op_name.par.Initializepulse.help = "Resets the simulation state to initial conditions."
op_name.par.Startpulse.help = "Begins the simulation from the current state."
op_name.par.Play.help = "Toggles simulation playback on or off."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Magnetize parameter help text updated successfully!")
