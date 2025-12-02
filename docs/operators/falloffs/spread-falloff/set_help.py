# TouchDesigner Python Script - Set Spread-Falloff Parameter Help Text

op_name = target

# Page: Spread
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Searchradius.help = "The maximum distance within which points are considered neighbors for spread."
op_name.par.Maxconnections.help = "Limits the maximum number of neighboring connections each point can have."
op_name.par.Falloffwidth.help = "Controls how quickly the falloff strength diminishes as it spreads from the."
op_name.par.Spreadamount.help = "Adds randomization to the spread pattern, creating more organic and varied."

# Page: Seed
op_name.par.Displayseed.help = "Visualize the seed selection region for infection starting points."
op_name.par.Seedthreshold.help = "Minimum value required for a point to become a seed."
op_name.par.Useseedattr.help = "Use an existing point attribute to define seed values instead of spatial."
op_name.par.Seedattr.help = "Name of the attribute to use for seed values (when Use Seed Attribute is."
op_name.par.Seedpop.help = "Reference to a POP containing points to use as seeds when no second input is."
op_name.par.Radius.help = "Size of the seed selection region."
op_name.par.Transitionrange.help = "Determines a transition range for seed fields."
op_name.par.Transitionalign.help = "Determines a transition offset for seed fields."
op_name.par.Outputseedattr.help = "Write the seed selection values to an output attribute."

# Page: Falloff
op_name.par.Combattrscope.help = "Specifies which falloff attribute to combine with when Combine Operation is not."
op_name.par.Swaporder.help = "Reverses the order of operands in the combine operation (A op B becomes B op A)."
op_name.par.Combstrength.help = "Blending factor for the combine operation, ranging from 0 (no effect) to 1."
op_name.par.Outputfalloffattr.help = "Name of the attribute where the final falloff values will be stored."
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Opencustumramp.help = "Opens the custom color ramp editor for defining a custom falloff visualization."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Noise
op_name.par.Applynoise.help = "When enabled, adds procedural noise to the falloff values for organic variation."
op_name.par.Seed.help = "Numerical value that initializes the randomization."
op_name.par.Period.help = "Period (scale) of the noise field."
op_name.par.Harmon.help = "The number of higher frequency components to layer on top of the base frequency."
op_name.par.Spread.help = "The factor by which the frequency of a harmonic increases relative to the."
op_name.par.Gain.help = "Amplitude of the Harmonics layered on top of the base frequency."
op_name.par.Amp.help = "The noise values amplitude (a scale on the values output)."
op_name.par.Exp.help = "Sets the exponent. The internal value is raised by the power of the exponent."
op_name.par.Offset.help = "Adds an offset to the resulting value."
op_name.par.Tnoisex.help = "Translate the points through the noise space."
op_name.par.Rnoisex.help = "Rotate the points around the corresponding X, Y and Z axes."
op_name.par.Snoisex.help = "These three fields scale the Source geometry in the three axes."
op_name.par.Pnoisex.help = "The pivot point for the transform rotates and scales."
op_name.par.T4dnoise.help = "Translates the points through the 4th noise dimension."
op_name.par.Xordnoise.help = "Sets the overall transform order."
op_name.par.Rordnoise.help = "Sets the order of rotations within the overall transform order.."


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

print("Spread-Falloff parameter help text updated successfully!")
