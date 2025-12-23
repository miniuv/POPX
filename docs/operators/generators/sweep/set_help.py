# TouchDesigner Python Script - Set Sweep Parameter Help Text

op_name = target

# Page: Orient Curve
op_name.par.Reorientcurve.help = "Enables curve reorientation."
op_name.par.Invertn.help = "Inverts the normal vector direction."
op_name.par.Customfirsttangent.help = "Enables custom first tangent vector."
op_name.par.Twistamount.help = "Amount of twist to apply along the curve."
op_name.par.Opentwistramp.help = "Opens the twist ramp editor."
op_name.par.Resettwistramp.help = "Resets the twist ramp to default."
op_name.par.Twisttop.help = "Reference to an external TOP for twist control."
op_name.par.Twistpercurve.help = "When enabled with an external TOP, maps the texture to each curve individually."
op_name.par.Twistbyattribute.help = "Enables twist control via a point attribute instead of the ramp or TOP."
op_name.par.Twistattr.help = "Name of the point attribute to use for twist values when Twist by Attribute is enabled."

# Page: Surface
op_name.par.Width.help = "Width of the swept surface. Can be overridden by a LineWidth point attribute."
op_name.par.Columbs.help = "Number of columns for round tube cross-section."
op_name.par.Roundcorners.help = "Enables rounded corners for square tubes."
op_name.par.Cornerradius.help = "Radius of rounded corners."
op_name.par.Cornersides.help = "Number of sides for rounded corners."
op_name.par.Scalecrosssections.help = "Scale factor for input cross-sections."
op_name.par.Inc.help = "N value when skinning groups of N input primitives or every N input primitives."
op_name.par.Closedsurface.help = "The last vertex is connected to the first vertex."
op_name.par.Outputquads.help = "Whether to output quad primitives instead of triangle primitives."
op_name.par.Applyscale.help = "Enables scale variation along the curve."
op_name.par.Openscaleramp.help = "Opens the scale ramp editor."
op_name.par.Resetscaleramp.help = "Resets the scale ramp to default."
op_name.par.Scaletop.help = "Reference to an external Ramp TOP for scale control."
op_name.par.Scalepercurve.help = "When enabled with an external TOP, maps the texture to each curve individually."
op_name.par.Scalebyattr.help = "Enables scale control via a point attribute instead of the ramp or TOP."
op_name.par.Scaleattr.help = "Name of the point attribute to use for scale values when Scale by Attribute is enabled."
op_name.par.Applycolor.help = "Enables color variation along the curve."
op_name.par.Opencolorramp.help = "Opens the color ramp editor."
op_name.par.Resetcolorramp.help = "Resets the color ramp to default."
op_name.par.Colortop.help = "Reference to an external Ramp TOP for color control."
op_name.par.Colorpercurve.help = "When enabled with an external TOP, maps the texture to each curve individually."
op_name.par.Generatevertexnormals.help = "Generates vertex normals for the output geometry."
op_name.par.Maxprimsperpoint.help = "Maximum number of primitives a point can be part of in the input geometry."
op_name.par.Anglenormal.help = "For vertex normals, the threshold angle between faces above which the shared."

# Page: Attributes
op_name.par.Frombackbonecurves.help = "Attributes to transfer from backbone curves."
op_name.par.Fromcrosssections.help = "Attributes to transfer from cross-sections."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Sweep parameter help text updated successfully!")
