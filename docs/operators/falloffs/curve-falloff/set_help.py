# TouchDesigner Python Script - Set Curve-Falloff Parameter Help Text

op_name = target

# Page: Curve
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Curvegeometry.help = "Reference to curve geometry. Used when Input 1 is not connected."
op_name.par.Displaycurve.help = "When enabled, renders a visual representation of the curve in the viewport for reference."
op_name.par.Displaycolorr.help = "Color used to display the curve when Display Curve is enabled."
op_name.par.Mode.help = "Calculation method for generating falloff values from the curve."
op_name.par.Mindistance.help = "Minimum distance value for falloff calculation range."
op_name.par.Maxdistance.help = "Maximum distance value for falloff calculation range."
op_name.par.Resamplemethod.help = "Line strip resample method."
op_name.par.Resampledivs.help = "The number of divisions."
op_name.par.Resamplemaxdist.help = "Maximum distance between points."
op_name.par.Maxverts.help = "Sets the number of vertices to be allocated."
op_name.par.Maxtries.help = "Max number of iterations for binary search when linearly resampling."
op_name.par.Xord.help = "Order in which Scale, Rotate, and Translate operations are applied to the curve."
op_name.par.Rord.help = "Order in which rotations around the X, Y, and Z axes are applied."
op_name.par.Tx.help = "Translation offset applied to the curve in world space."
op_name.par.Rx.help = "Rotation angles in degrees around the X, Y, and Z axes."
op_name.par.Sx.help = "Scale factors applied to the curve along each axis."
op_name.par.Scale.help = "Uniform scaling factor applied equally across all axes."
op_name.par.Px.help = "Pivot point around which rotations and scaling are performed."

# Page: Falloff
op_name.par.Combineop.help = "Mathematical operation used to combine this falloff with existing falloff values."
op_name.par.Combattrscope.help = "Specifies which falloff attribute to combine with when Combine Operation is not set to Set."
op_name.par.Swaporder.help = "Reverses the order of operands in the combine operation (A op B becomes B op A)."
op_name.par.Combstrength.help = "Blending factor for the combine operation, ranging from 0 (no effect) to 1 (full effect)."
op_name.par.Outputfalloffattr.help = "Name of the attribute where the final falloff values will be stored."
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Fallofframp.help = "Color ramp preset used for visualizing falloff values when Preview Falloff is enabled."
op_name.par.Opencustumramp.help = "Opens the custom color ramp editor for defining a custom falloff visualization gradient."
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
op_name.par.Enableremapramp.help = "Applies a custom curve defined by a ramp to remap the falloff values."
op_name.par.Openremapramp.help = "Opens the ramp editor for defining the custom remapping curve."
op_name.par.Resetremapramp.help = "Resets the remap ramp editor."
op_name.par.Remaptop.help = "Reference to an external TOP for remap control. When specified, overrides the internal ramp editor."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Converttoptprim.help = "Converts points to primitive points when Render Primitives is toggled off."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner instances."

print("Curve-Falloff parameter help text updated successfully!")
