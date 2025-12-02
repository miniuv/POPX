# TouchDesigner Python Script - Set Path-Tracer Parameter Help Text

op_name = target

# Page: Path Tracing
op_name.par.Enable.help = "Master toggle for path tracing rendering."
op_name.par.Reset.help = "Pulse to reset progressive accumulation and restart rendering."
op_name.par.Lockinput.help = "Freeze input geometry to prevent updates during progressive rendering."
op_name.par.Progressiverendering.help = "Accumulate samples over time for noise-free convergence."
op_name.par.Temporalsmoothing.help = "Frame blending amount for temporal coherence."
op_name.par.Rendertop.help = "Reference to Render TOP providing camera and viewport settings that the path."
op_name.par.Raysperpixel.help = "Number of rays cast per pixel per frame."
op_name.par.Maxbounces.help = "Maximum ray bounce depth for global illumination."
op_name.par.Rayoffset.help = "Offset distance for ray origins to prevent self-intersection artifacts."
op_name.par.Aperture.help = "Camera aperture size for depth of field."
op_name.par.Focallength.help = "Distance from camera where objects are in sharp focus."
op_name.par.Enabletonemap.help = "Apply tone mapping to convert HDR output to display range."
op_name.par.Exposure.help = "Exposure multiplier for tone mapping."

# Page: Material
op_name.par.Overrideifexists.help = "Apply material parameters even when geometry has existing material attributes."
op_name.par.Metallic.help = "Metallic appearance."
op_name.par.Roughness.help = "Surface roughness."
op_name.par.Specular.help = "Specular reflection strength for dielectrics."
op_name.par.Speculartint.help = "Tint specular reflection with base color."
op_name.par.Anisotropic.help = "Anisotropic highlight stretching."
op_name.par.Anisotropicrot.help = "Rotation angle for anisotropic highlights."
op_name.par.Subsurface.help = "Subsurface scattering amount for translucent materials like skin or wax."
op_name.par.Sheen.help = "Soft velvet-like reflection for fabrics and cloth."
op_name.par.Sheentint.help = "Tint sheen with base color."
op_name.par.Clearcoat.help = "Secondary specular layer for car paint or lacquered surfaces."
op_name.par.Clearcoatgloss.help = "Glossiness of clearcoat layer."
op_name.par.Ior.help = "Index of refraction for dielectrics."
op_name.par.Transmission.help = "Light transmission through surface for glass and transparent materials."

# Page: Lights
op_name.par.Enableenv.help = "Enable image-based lighting from environment map."
op_name.par.Renderenv.help = "Show environment map in background when rays miss geometry."
op_name.par.Envmapintensity.help = "Multiplier for environment light contribution."
op_name.par.Environmentmap.help = "HDR environment texture."
op_name.par.Enabledirectlight.help = "Enable direct lighting."
op_name.par.Renderlights.help = "Show light geometry in render."
op_name.par.Lights.help = "Sequence of light sources with individual properties."
op_name.par.Lights0dimmer.help = "Light intensity multiplier."
op_name.par.Lights0xord.help = "Order of transformation operations."
op_name.par.Lights0rord.help = "Rotation axis order."
op_name.par.Lights0scale.help = "Uniform scale multiplier for all axes for area lights."
op_name.par.Lights0bidirectional.help = "Area and spot lights emit from both sides of surface."
op_name.par.Lights0coneangle.help = "Spotlight cone angle in degrees."
op_name.par.Lights0conedelta.help = "Spotlight falloff width at cone edge."
op_name.par.Lights0coneroll.help = "Spotlight intensity falloff curve."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Path-Tracer parameter help text updated successfully!")
