# TouchDesigner Python Script - Set SSFR Parameter Help Text

op_name = target

# Page: SSFR
op_name.par.Rendertop.help = "Reference to the Render TOP where the fluid rendering output is displayed."
op_name.par.Resolutionscale.help = "Scale factor for the rendering resolution relative to the Render TOP."
op_name.par.Passes.help = "Number of bilateral blur passes to smooth the depth buffer."
op_name.par.Filterradius.help = "Radius of the bilateral blur filter in pixels."
op_name.par.Depththreshold.help = "Maximum depth difference allowed during bilateral blur to preserve fluid edges."
op_name.par.Materialtype.help = "Rendering material mode for the fluid surface."
op_name.par.Thicknessscale.help = "Scale factor for fluid thickness affecting absorption and refraction calculations."
op_name.par.Ior.help = "Index of refraction for the fluid surface."
op_name.par.Extinctionr.help = "Color absorbed by the fluid over distance, controlling the tint of thick regions."
op_name.par.Absorptionscale.help = "Multiplier for the absorption effect based on fluid thickness."
op_name.par.Refractionscale.help = "Strength of the refraction distortion through the fluid surface."
op_name.par.Basecolorr.help = "Base color of the fluid surface in PBR mode."
op_name.par.Specularlevel.help = "Intensity of specular reflections on the fluid surface."
op_name.par.Metallic.help = "Metallic appearance of the fluid surface. Higher values create more reflective, metal-like surfaces."
op_name.par.Roughness.help = "Surface roughness of the fluid. Lower values create sharper reflections."
op_name.par.Ambientocclusion.help = "Strength of ambient occlusion darkening in fluid crevices."
op_name.par.Emitr.help = "Emissive color added to the fluid surface."
op_name.par.Constantr.help = "Constant color added to the final rendering output."
op_name.par.Enablesurfacedetail.help = "Enable procedural surface detail on the fluid."
op_name.par.Detailresolution.help = "Resolution of the surface detail noise texture."
op_name.par.Detailperiod.help = "Spatial frequency of the surface detail pattern."
op_name.par.Detailstrength.help = "Intensity of the surface detail displacement."
op_name.par.Envmap.help = "Reference to a TOP used as the environment map for reflections."
op_name.par.Renderenvmap.help = "Render the environment map as a background behind the fluid."
op_name.par.Enabletonemap.help = "Enable tone mapping on the rendered output."
op_name.par.Gamma.help = "Gamma correction value for the tone mapped output."
op_name.par.Exposure.help = "Exposure adjustment for the tone mapped output."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("SSFR parameter help text updated successfully!")
