# TouchDesigner Python Script - Set Infection-Falloff Parameter Help Text

op_name = target

# Page: Infection
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Infectby.help = "Method used to determine how infection spreads between points."
op_name.par.Distribution.help = "Distribution method for radius-based infection."
op_name.par.Searchradius.help = "Maximum distance for finding neighboring points to infect (radius mode only)."
op_name.par.Maxconnections.help = "Maximum number of connections each point can have for infection spreading."
op_name.par.Infectionrate.help = "Speed at which infection values spread from infected to uninfected points."
op_name.par.Distweight.help = "Enable distance-based falloff for infection spreading, creating smoother gradients."
op_name.par.Weightamount.help = "Strength of distance-based weighting (when Distance Weighted Spread is enabled)."
op_name.par.Dissipationrate.help = "Rate at which infection values decrease over time, creating decay effects."
op_name.par.Enablereinfection.help = "Allow previously infected points to be reinfected after dissipation (requires Dissipation Rate > 0)."
op_name.par.Threshold.help = "Minimum infection value required before a point can be reinfected (requires reinfection enabled)."
op_name.par.Resistance.help = "Resistance to infection spreading, slowing down the infection process."
op_name.par.Initializepulse.help = "Reset the infection simulation to initial state."
op_name.par.Startpulse.help = "Start the infection simulation from current state."
op_name.par.Play.help = "Continuously run the infection simulation."
op_name.par.Steppulse.help = "Advance the infection simulation by one step."

# Page: Seed
op_name.par.Displayseed.help = "Visualize the seed selection region for infection starting points."
op_name.par.Seedthreshold.help = "Minimum value required for a point to become a seed."
op_name.par.Useseedattr.help = "Use an existing point attribute to define seed values instead of spatial selection."
op_name.par.Seedattr.help = "Name of the attribute to use for seed values (when Use Seed Attribute is enabled)."
op_name.par.Seedpop.help = "Reference to a POP containing points to use as seeds when no second input is connected."
op_name.par.Positionx.help = "Center position of the seed selection region. Can be overridden per-seed using a P point attribute."
op_name.par.Radius.help = "Size of the seed selection region. Can be overridden per-seed using a radius point attribute."
op_name.par.Transitionrange.help = "Determines a transition range for seed fields. Can be overridden per-seed using a transitionrange point attribute."
op_name.par.Transitionalign.help = "Determines a transition offset for seed fields. Can be overridden per-seed using a transitionalign point attribute."
op_name.par.Transitiontype.help = "Determines a transition function for seed fields. Can be overridden per-seed using a transitiontype point attribute."
op_name.par.Outputseedattr.help = "Write the seed selection values to an output attribute."

# Page: Falloff
op_name.par.Combineop.help = "Mathematical operation used to combine this falloff with existing falloff values."
op_name.par.Combattrscope.help = "Specifies which falloff attribute to combine with when Combine Operation is not set to Set."
op_name.par.Swaporder.help = "Reverses the order of operands in the combine operation (A op B becomes B op A)."
op_name.par.Combstrength.help = "Blending factor for the combine operation, ranging from 0 (no effect) to 1 (full effect)."
op_name.par.Outputfalloffattr.help = "Name of the attribute where the final falloff values will be stored."
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Fallofframp.help = "Color ramp preset used for visualizing falloff values when Preview Falloff is enabled."
op_name.par.Opencustumrampeditor.help = "Opens the custom color ramp editor for defining a custom falloff visualization gradient."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Noise
op_name.par.Applynoise.help = "When enabled, adds procedural noise to the falloff values for organic variation."
op_name.par.Combineopnoise.help = "How noise values are combined with the base falloff (Add or Multiply)."
op_name.par.Type.help = "Noise algorithm type (Perlin, Simplex, etc.)."
op_name.par.Seed.help = "Numerical value that initializes the randomization."
op_name.par.Period.help = "Period (scale) of the noise field."
op_name.par.Harmon.help = "The number of higher frequency components to layer on top of the base frequency. 0 harmonics give the base shape."
op_name.par.Spread.help = "The factor by which the frequency of a harmonic increases relative to the previous harmonic."
op_name.par.Gain.help = "Amplitude of the Harmonics layered on top of the base frequency."
op_name.par.Amp.help = "The noise values amplitude (a scale on the values output)."
op_name.par.Exp.help = "Sets the exponent. The internal value is raised by the power of the exponent."
op_name.par.Offset.help = "Adds an offset to the resulting value."
op_name.par.Xordnoise.help = "Sets the overall transform order for the transformations."
op_name.par.Rordnoise.help = "Sets the order of the rotations within the overall transform order."
op_name.par.Tnoisex.help = "Translate the points through the noise space."
op_name.par.Rnoisex.help = "Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees."
op_name.par.Snoisex.help = "These three fields scale the Source geometry in the three axes."
op_name.par.Pnoisex.help = "The pivot point for the transform rotates and scales."
op_name.par.T4dnoise.help = "Translates the points through the 4th noise dimension."

# Page: Remap
op_name.par.Remap.help = "Enables remapping controls for adjusting falloff value range and distribution."
op_name.par.Clamp.help = "When enabled, constrains falloff values to the 0-1 range."
op_name.par.Fit.help = "Enables remapping of falloff values from an input range to an output range."
op_name.par.Auto.help = "Automatically determines input range from actual min/max falloff values."
op_name.par.Inputmin.help = "Minimum value of the input range for remapping."
op_name.par.Inputmax.help = "Maximum value of the input range for remapping."
op_name.par.Outputmin.help = "Minimum value of the output range for remapping."
op_name.par.Outputmax.help = "Maximum value of the output range for remapping."
op_name.par.Invert.help = "Reverses the falloff values (1 - value)."
op_name.par.Enablerampremap.help = "Applies a custom curve defined by a ramp to remap the falloff values."
op_name.par.Openrampeditor.help = "Opens the ramp editor for defining the custom remapping curve."
op_name.par.Resetramp.help = "Resets the remap ramp editor."
op_name.par.Customramptop.help = "Reference to an external TOP for remap control. When specified, overrides the internal ramp editor."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Converttoptprim.help = "Converts points to primitive points when Render Primitives is toggled off."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner instances."

print("Infection-Falloff parameter help text updated successfully!")
