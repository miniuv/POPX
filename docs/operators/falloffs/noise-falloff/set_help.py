# TouchDesigner Python Script - Set Noise-Falloff Parameter Help Text

op_name = target

# Page: Noise
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Userestattr.help = "When enabled, evaluates noise using rest positions instead of current."
op_name.par.Seed.help = "Numerical value that initializes the randomization."
op_name.par.Period.help = "Period (scale) of the noise field."
op_name.par.Harmon.help = "The number of higher frequency components to layer on top of the base frequency."
op_name.par.Spread.help = "The factor by which the frequency of a harmonic increases relative to the."
op_name.par.Gain.help = "Amplitude of the Harmonics layered on top of the base frequency."
op_name.par.Normalizednoise.help = "When enabled, automatically normalizes noise output to 0-1 range."
op_name.par.Amp.help = "The noise values amplitude (a scale on the values output)."
op_name.par.Exp.help = "Sets the exponent. The internal value is raised by the power of the exponent."
op_name.par.Offset.help = "Adds an offset to the resulting value."

# Page: Transform
op_name.par.T4d.help = "Translates the points through the 4th noise dimension."

# Page: Falloff
op_name.par.Combattrscope.help = "Specifies which falloff attribute to combine with when Combine Operation is not."
op_name.par.Swaporder.help = "Reverses the order of operands in the combine operation (A op B becomes B op A)."
op_name.par.Combstrength.help = "Blending factor for the combine operation, ranging from 0 (no effect) to 1."
op_name.par.Outputfalloffattr.help = "Name of the attribute where the final falloff values will be stored."
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Opencustumramp.help = "Opens the custom color ramp editor for defining a custom falloff visualization."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Remap
op_name.par.Clamp.help = "When enabled, constrains falloff values to the 0-1 range."
op_name.par.Fit.help = "Enables remapping of falloff values from an input range to an output range."
op_name.par.Auto.help = "Automatically determines input range from actual min/max falloff values."
op_name.par.Inputmin.help = "Minimum value of the input range for remapping."
op_name.par.Inputmax.help = "Maximum value of the input range for remapping."
op_name.par.Outputmin.help = "Minimum value of the output range for remapping."
op_name.par.Outputmax.help = "Maximum value of the output range for remapping."
op_name.par.Invert.help = "Reverses the falloff values (1 - value)."
op_name.par.Enableremapramp.help = "Applies a custom curve defined by a ramp to remap the falloff values."
op_name.par.Openremapramp.help = "Opens the ramp editor for defining the custom remapping curve."
op_name.par.Resetremapramp.help = "Resets the remap ramp editor."
op_name.par.Remaptop.help = "Reference to an external TOP for remap control."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Noise-Falloff parameter help text updated successfully!")
