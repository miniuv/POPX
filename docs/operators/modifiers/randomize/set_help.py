# TouchDesigner Python Script - Set Randomize Parameter Help Text

op_name = target

# Page: General
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Localspace.help = "Applies randomization in local space when enabled, or world space when disabled."
op_name.par.Dofalloff.help = "Enables falloff-based modulation of the randomization effect."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that modulate the."

# Page: Position
op_name.par.Posrand.help = "Enables position randomization."
op_name.par.Posseed.help = "Random seed value for position randomization."
op_name.par.Posstep.help = "Quantizes random values to multiples of this step size."

# Page: Rotation
op_name.par.Rotrand.help = "Enables rotation randomization."
op_name.par.Rotseed.help = "Random seed value for rotation randomization."
op_name.par.Rotmult.help = "Multiplies the final random rotation values."
op_name.par.Rotstep.help = "Quantizes random rotation values to multiples of this step size in degrees."

# Page: Scale
op_name.par.Scalerand.help = "Enables per-axis scale randomization."
op_name.par.Scaleseed.help = "Random seed value for scale randomization."
op_name.par.Scalestep.help = "Quantizes random scale values to multiples of this step size."
op_name.par.Uniscalerand.help = "Enables uniform scale randomization across all axes."
op_name.par.Uniscaleseed.help = "Random seed value for uniform scale randomization."
op_name.par.Uniscaleminval.help = "Minimum random uniform scale value."
op_name.par.Uniscalemaxval.help = "Maximum random uniform scale value."
op_name.par.Uniscalestep.help = "Quantizes random uniform scale values to multiples of this step size."

# Page: Color
op_name.par.Colorrand.help = "Enables color randomization."
op_name.par.Colorseed.help = "Random seed value for color randomization."
op_name.par.Fromlow.help = "Lower bound of the input random range for color mapping."
op_name.par.Fromhigh.help = "Upper bound of the input random range for color mapping."
op_name.par.Tolow.help = "Lower bound of the output color range."
op_name.par.Tohigh.help = "Upper bound of the output color range."
op_name.par.Colorramp.help = "Enables color ramp for randomization instead of direct random values."
op_name.par.Opencolorramp.help = "Opens the internal ramp editor for customizing the color gradient."
op_name.par.Resetcolorramp.help = "Resets the internal ramp to default gradient values."
op_name.par.Colortop.help = "Reference to an external TOP for color palette."

# Page: Other
op_name.par.Otherrand.help = "Enables randomization of a custom float attribute."
op_name.par.Attr.help = "Specifies which float attribute to randomize."
op_name.par.Otherseed.help = "Random seed value for attribute randomization."
op_name.par.Otherminval.help = "Minimum random attribute value."
op_name.par.Othermaxval.help = "Maximum random attribute value."
op_name.par.Swaporder.help = "Reverses the order of operands in the combine operation."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Randomize parameter help text updated successfully!")
