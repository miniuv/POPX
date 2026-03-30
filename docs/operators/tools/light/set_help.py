# TouchDesigner Python Script - Set Light Parameter Help Text

op_name = target

# Page: Light
op_name.par.Type.help = "Selects the type of light source."
op_name.par.Colorr.help = "RGB color of the light."
op_name.par.Dimmer.help = "Light intensity multiplier."
op_name.par.Bidirectional.help = "Area and spot lights emit from both sides of surface."
op_name.par.Coneangle.help = "Spotlight cone angle in degrees."
op_name.par.Conedelta.help = "Spotlight falloff width at cone edge."
op_name.par.Coneroll.help = "Spotlight intensity falloff curve."
op_name.par.Volsteps.help = "Number of ray marching steps for volumetric light evaluation."
op_name.par.Voldensityscale.help = "Multiplier for volumetric light density."
op_name.par.Attenuated.help = "Enables distance-based light intensity falloff."
op_name.par.Attenuationstart.help = "Distance at which light attenuation begins."
op_name.par.Attenuationend.help = "Distance at which light attenuation reaches zero."
op_name.par.Attenuationexp.help = "Exponent controlling the attenuation falloff curve."
op_name.par.Texturemap.help = "Texture map projected from the light source, or HDR environment map for Environment Light."
op_name.par.Envlightmaprotatex.help = "Rotation of the environment map in degrees. Enabled when Light Type is Environment Light."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Light parameter help text updated successfully!")
