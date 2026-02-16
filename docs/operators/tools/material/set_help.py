# TouchDesigner Python Script - Set Material Parameter Help Text

op_name = target

# Page: Material
op_name.par.Attrclass.help = "Selects which attribute class the material properties are applied to."
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Overrideifexists.help = "Override material attributes that already exist."
op_name.par.Basecolorr.help = "Diffuse albedo color."
op_name.par.Metallic.help = "Metallic appearance."
op_name.par.Roughness.help = "Surface roughness."
op_name.par.Specular.help = "Specular reflection strength for dielectrics."
op_name.par.Specularcolorr.help = "Tint specular reflection with color."
op_name.par.Anisotropic.help = "Anisotropic highlight stretching."
op_name.par.Anisotropicrot.help = "Rotation angle for anisotropic highlights."
op_name.par.Subsurface.help = "Subsurface scattering amount for translucent materials like skin or wax."
op_name.par.Sheen.help = "Soft velvet-like reflection for fabrics and cloth."
op_name.par.Sheencolorr.help = "Tint sheen reflection with color."
op_name.par.Clearcoat.help = "Secondary specular layer for car paint or lacquered surfaces."
op_name.par.Clearcoatgloss.help = "Glossiness of clearcoat layer."
op_name.par.Ior.help = "Index of refraction for dielectrics."
op_name.par.Transmission.help = "Light transmission through surface for glass and transparent materials."
op_name.par.Dispersion.help = "Chromatic dispersion amount for refractive materials."
op_name.par.Emissionr.help = "Emissive color for self-illuminating surfaces."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Material parameter help text updated successfully!")
