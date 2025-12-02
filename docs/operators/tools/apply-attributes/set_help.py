# TouchDesigner Python Script - Set Apply-Attributes Parameter Help Text

op_name = target

# Page: Transformation
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Dofalloff.help = "When enabled, uses a falloff attribute to blend transformations smoothly."
op_name.par.Falloffattr.help = "Name of the falloff attribute to use for blending transformations (default:."
op_name.par.Dotranslate.help = "Enables translation transformations from template points."
op_name.par.Dorotate.help = "Enables rotation transformations from template points using slerp interpolation."
op_name.par.Doscale.help = "Enables scale transformations from template points."
op_name.par.Dopivot.help = "Enables pivot point transformations from template points."
op_name.par.Localspace.help = "When enabled, applies transformations relative to the instance's current."

# Page: Attributes
op_name.par.Copyattrs.help = "When enabled, copies point attributes from template geometry to instances."
op_name.par.Attrstocopy.help = "Space-separated list of attribute names to copy from template points."
op_name.par.Createid.help = "Automatically creates unique popxId attributes for instances that don't have."
op_name.par.Outputorientattr.help = "Outputs orientation data as an attribute for downstream operators."
op_name.par.Outputscaleattr.help = "Outputs scale data as an attribute for downstream operators."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Apply-Attributes parameter help text updated successfully!")
