# TouchDesigner Python Script - Set Orient-Curve Parameter Help Text

op_name = target

# Page: Orient Curve
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Invertn.help = "Inverts the normal direction of the orientation frame."
op_name.par.Customfirsttangent.help = "Enables custom tangent vector for the first point on the curve."
op_name.par.Twistamount.help = "Rotation amount in degrees applied along the curve length."
op_name.par.Opentwistramp.help = "Opens the twist ramp editor."
op_name.par.Resettwistramp.help = "Resets the twist ramp to default."
op_name.par.Twisttop.help = "Reference to an external TOP for twist control."
op_name.par.Twistpercurve.help = "When enabled with an external TOP, maps the texture to each curve individually."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Orient-Curve parameter help text updated successfully!")
