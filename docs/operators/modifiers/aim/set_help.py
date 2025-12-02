# TouchDesigner Python Script - Set Aim Parameter Help Text

op_name = target

# Page: General
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Dofalloff.help = "Enables falloff-based aim intensity control."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that attenuate aim rotation."

# Page: Aim
op_name.par.Displayaimguide.help = "Visualizes aim target positions in the viewport."
op_name.par.Aimguidescale.help = "Controls the display size of aim guide visualization."

# Page: Up
op_name.par.Displayupguide.help = "Visualizes up target positions in the viewport."
op_name.par.Upguidescale.help = "Controls the display size of up guide visualization."

# Page: Orientation
op_name.par.Invertaim.help = "Reverses the aim direction by 180 degrees."
op_name.par.Invertup.help = "Reverses the up direction by 180 degrees."
op_name.par.Constrainaroundup.help = "Limits rotation to occur only around the up axis, preventing roll."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Aim parameter help text updated successfully!")
