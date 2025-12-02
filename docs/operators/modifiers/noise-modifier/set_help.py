# TouchDesigner Python Script - Set Noise-Modifier Parameter Help Text

op_name = target

# Page: Noise
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Dofalloff.help = "Enables falloff-based noise intensity control."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values."
op_name.par.Userestattr.help = "Uses the rest attribute to stabilize the noise reference space."
op_name.par.Enabledirattr.help = "Reads direction values from a point attribute for scalar noise."
op_name.par.Directionattr.help = "Name of the attribute to use for direction vectors."
op_name.par.Curlnoise.help = "Generates divergence-free curl noise for fluid-like motion."
op_name.par.Seed.help = "Numerical value that initializes the randomization."
op_name.par.Period.help = "Period (scale) of the noise field."
op_name.par.Harmon.help = "The number of higher frequency components to layer on top of the base frequency."
op_name.par.Spread.help = "The factor by which the frequency of a harmonic increases relative to the."
op_name.par.Gain.help = "Amplitude of the Harmonics layered on top of the base frequency."

# Page: Transform
op_name.par.T4d.help = "Translates the instances through the 4th noise dimension."

# Page: Affect
op_name.par.Affectposition.help = "Enables noise-based position displacement."
op_name.par.Positionamount.help = "Controls the intensity of position displacement."
op_name.par.Affectrotation.help = "Enables noise-based rotation changes."
op_name.par.Rotationamount.help = "Controls the intensity of rotation changes."
op_name.par.Aimweight.help = "Defines how fast instances rotate toward their direction of motion."
op_name.par.Affectscale.help = "Enables noise-based scale changes."
op_name.par.Scaleamount.help = "Controls the intensity of scale changes."
op_name.par.Initializepulse.help = "Resets advection simulation state."
op_name.par.Startpulse.help = "Begins advection simulation from the current state."
op_name.par.Play.help = "Toggles advection simulation playback."
op_name.par.Steppulse.help = "Advances advection simulation by one frame."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Noise-Modifier parameter help text updated successfully!")
