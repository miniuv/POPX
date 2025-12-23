# TouchDesigner Python Script - Set Advect Parameter Help Text

op_name = target

# Page: Advect
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Dofalloff.help = "Enables falloff-based advection intensity control."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that attenuate advection strength."
op_name.par.Advectsource.help = "Determines whether to read advection vectors from point attributes or reference geometry."
op_name.par.Advectattr.help = "Name of the vector attribute to use for advection direction and speed."
op_name.par.Maxdistance.help = "Maximum distance to search for nearest neighbor points on reference geometry."
op_name.par.Distribution.help = "Method for selecting neighbor points when using reference geometry."
op_name.par.Lookupmode.help = "Determines how advection vectors are sampled from reference geometry."
op_name.par.Maxptsavg.help = "Maximum number of points to include when averaging vectors in Average lookup mode."
op_name.par.Timestep.help = "Controls the integration step size for advection movement."
op_name.par.Rotateto.help = "Enables automatic rotation of instances to align with the advection vector direction."
op_name.par.Feedbackpop.help = "Reference to the feedback POP that drives the advection simulation."
op_name.par.Passthroughattrs.help = "Attributes to pass through from the initial POP connected to the feedback POP."
op_name.par.Enablelife.help = "Enables lifespan-based particle death when using feedback loop advection."
op_name.par.Lifeseed.help = "Numerical value that initializes the randomization for life variance."
op_name.par.Lifespan.help = "Base duration in seconds that particles exist before being removed."
op_name.par.Lifevariance.help = "Random variation added to the life span for each particle."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Advect parameter help text updated successfully!")
