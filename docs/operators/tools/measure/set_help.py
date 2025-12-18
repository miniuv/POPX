# TouchDesigner Python Script - Set Measure Parameter Help Text

op_name = target

# Page: Measure
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Measure.help = "The type of geometric measurement to compute."
op_name.par.Scalarattr.help = "The scalar attribute to compute gradient from when Measure is set to Gradient."
op_name.par.Usenebrsattr.help = "When enabled, uses pre-computed neighbor attributes instead of computing them."
op_name.par.Nebrtype.help = "Method for finding neighboring points: by distance or by connectivity."
op_name.par.Maxdistance.help = "Maximum distance to search for neighboring points."
op_name.par.Distribution.help = "Method for distributing neighbor point selection."
op_name.par.Numhashbuckets.help = "Number of hash buckets for spatial acceleration structure."
op_name.par.Maxneighbors.help = "Maximum number of neighbors to consider for each point."
op_name.par.Smoothingradius.help = "Radius used for smoothing the measured values."
op_name.par.Outputmeasureattr.help = "Name of the output attribute to store the measured values."
op_name.par.Outputneighborsattrs.help = "When enabled, outputs neighbor attributes for reuse by subsequent Measure operators."

# Page: Preview Measure
op_name.par.Previewmeasure.help = "When enabled, visualizes the measured values using a color ramp."
op_name.par.Measureramp.help = "Color ramp preset used for visualizing measured values when Preview Measure is."
op_name.par.Opencustumramp.help = "Opens the custom color ramp editor for defining a custom measure visualization."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Measure parameter help text updated successfully!")
