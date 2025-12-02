# TouchDesigner Python Script - Set Pivot Parameter Help Text

op_name = target

# Page: Pivot
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Dofalloff.help = "Enables falloff-based modulation of pivot adjustments."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that modulate pivot."
op_name.par.Pivotonly.help = "When enabled, adjusts only the pivot point without transforming the instance."
op_name.par.Localspace.help = "When enabled, pivot adjustments are calculated in local space relative to each."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Pivot parameter help text updated successfully!")
