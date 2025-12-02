# TouchDesigner Python Script - Set Spring-Modifier Parameter Help Text

op_name = target

# Page: Spring
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Dofalloff.help = "Enables falloff-based attenuation of spring effects."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that attenuate spring."
op_name.par.Position.help = "Applies spring physics to instance position."
op_name.par.Rotation.help = "Applies spring physics to instance rotation."
op_name.par.Scale.help = "Applies spring physics to instance scale."
op_name.par.Other.help = "Enables spring physics for a custom float attribute."
op_name.par.Attr.help = "Specifies which float attribute to apply spring physics to when Other is."
op_name.par.Usemassattr.help = "Uses a per-instance mass attribute instead of the global Mass parameter."
op_name.par.Massattr.help = "Specifies which attribute to use for per-instance mass values."
op_name.par.Mass.help = "Mass value used in spring physics calculations."
op_name.par.Springconst.help = "Stiffness of the spring."
op_name.par.Dampingcoef.help = "Controls how quickly spring motion decays."
op_name.par.Initializepulse.help = "Resets the spring simulation state to initial conditions."
op_name.par.Startpulse.help = "Begins the spring simulation from the current state."
op_name.par.Play.help = "Toggles spring simulation playback on or off."

# Page: Falloff
op_name.par.Previewfalloff.help = "Visualizes the Other float attribute as colors when Other is enabled."
op_name.par.Opencustumramp.help = "Opens the custom ramp editor for creating custom visualization gradients for."
op_name.par.Resetcustomramp.help = "Resets the custom ramp to default gradient values."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Spring-Modifier parameter help text updated successfully!")
