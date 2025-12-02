# TouchDesigner Python Script - Set Orient-Mesh Parameter Help Text

op_name = target

# Page: Orient Mesh
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Visualizeupvector.help = "When enabled, displays the up vector as yellow lines for debugging orientation."
op_name.par.Lengthscale.help = "Controls the length of the visualized up vector lines."
op_name.par.Colorr.help = "Color of the visualized up vector lines."
op_name.par.Computenormals.help = "Computes surface normals when using N and Up method."
op_name.par.Autoup.help = "Automatically computes up vector when using N and Up method."
op_name.par.Upvectorx.help = "Manual up vector direction when Auto Up is disabled."
op_name.par.Attributename.help = "Attribute to use for UV or gradient-based orientation styles."
op_name.par.Makeortho.help = "Ensures the orientation frame vectors are perfectly orthogonal."
op_name.par.Invertn.help = "Inverts the normal vector direction."
op_name.par.Invertup.help = "Inverts the up vector direction."
op_name.par.Crossupvector.help = "Wraps the up vector along the surface for swirling motion effects."
op_name.par.Outputtangent.help = "Outputs tangent vector attribute in addition to normal and up vectors."

# Page: Curl Noise
op_name.par.Enablecurlnoise.help = "Applies curl noise to orientation vectors for organic swirling effects."
op_name.par.Blend.help = "Blends curl noise with original orientation from 0 (full noise) to 1 (original)."
op_name.par.Seed.help = "Numerical value that initializes the randomization."
op_name.par.Period.help = "Period (scale) of the noise field."
op_name.par.Harmon.help = "The number of higher frequency components to layer on top of the base frequency."
op_name.par.Spread.help = "The factor by which the frequency of a harmonic increases relative to the."
op_name.par.Gain.help = "Amplitude of the Harmonics layered on top of the base frequency."
op_name.par.Amp.help = "The noise values amplitude (a scale on the values output)."
op_name.par.Exp.help = "Sets the exponent. The internal value is raised by the power of the exponent."
op_name.par.T4d.help = "Translates the points through the 4th noise dimension."

# Page: Blur
op_name.par.Enableblur.help = "Applies blur to orientation vectors to smooth rough transitions."
op_name.par.Iterations.help = "Number of blur passes to apply."
op_name.par.Kernalradius.help = "Search radius for proximity-based blur influence."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Orient-Mesh parameter help text updated successfully!")
