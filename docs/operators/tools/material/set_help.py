# TouchDesigner Python Script - Set Material Parameter Help Text

op_name = target

# Page: Material
op_name.par.Attrclass.help = "Selects which attribute class the material properties are applied to."
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Overrideifexists.help = "Override material attributes that already exist."
op_name.par.Basecolorr.help = "Diffuse albedo color."
op_name.par.Metallic.help = "Metallic appearance."
op_name.par.Roughness.help = "Surface roughness."
op_name.par.Specularlevel.help = "Specular reflection strength for dielectrics."
op_name.par.Speculartintr.help = "Tint specular reflection with color."
op_name.par.Anisotropiclevel.help = "Anisotropic highlight stretching level."
op_name.par.Anisotropicangle.help = "Rotation angle for anisotropic highlights."
op_name.par.Sheenlevel.help = "Soft velvet-like reflection for fabrics and cloth."
op_name.par.Sheentintr.help = "Tint sheen reflection with color."
op_name.par.Clearcoatlevel.help = "Secondary specular layer for car paint or lacquered surfaces."
op_name.par.Clearcoatroughness.help = "Roughness of the clearcoat layer."
op_name.par.Clearcoattintr.help = "Tint clearcoat reflection with color."
op_name.par.Ior.help = "Index of refraction for dielectrics."
op_name.par.Thickness.help = "Thickness of the surface for thin-walled materials."
op_name.par.Transmission.help = "Light transmission through surface for glass and transparent materials."
op_name.par.Dispersion.help = "Chromatic dispersion amount for refractive materials."
op_name.par.Absorptioncolorr.help = "Color absorbed by the volume as light passes through."
op_name.par.Emissionlevel.help = "Emission intensity for self-illuminating surfaces."
op_name.par.Emissioncolorr.help = "Emissive color for self-illuminating surfaces."

# Page: Maps
op_name.par.Substance.help = "Reference to a Substance TOP for automatic PBR texture assignment."
op_name.par.Basecolormap.help = "Texture map for base color."
op_name.par.Metallicmap.help = "Texture map for metallic values."
op_name.par.Roughnessmap.help = "Texture map for roughness values."
op_name.par.Specularmap.help = "Texture map for specular values."
op_name.par.Anisotropiclevelmap.help = "Texture map for anisotropic level values."
op_name.par.Anisotropicanglemap.help = "Texture map for anisotropic angle values."
op_name.par.Sheenmap.help = "Texture map for sheen values."
op_name.par.Clearcoatmap.help = "Texture map for clearcoat values."
op_name.par.Transmissionmap.help = "Texture map for transmission values."
op_name.par.Emissionmap.help = "Texture map for emission values."
op_name.par.Normalmap.help = "Normal map for surface bump detail."
op_name.par.Bumpscale.help = "Scale factor for normal map bump intensity."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Material parameter help text updated successfully!")
