# TouchDesigner Python Script - Set Instancer Parameter Help Text

op_name = target

# Page: Instancing
op_name.par.Indexrandomseed.help = "Random seed for index selection."
op_name.par.Indexattr.help = "Point attribute to use for indexing."
op_name.par.Globuniscale.help = "Global uniform scale multiplier."
op_name.par.Pointsonly.help = "Output only distribution points without instancing geometry."
op_name.par.Outputtemplateattrs.help = "Include template attributes in output."
op_name.par.Centerinstances.help = "Centers all instances in world space before instancing, ensuring their origins."
op_name.par.Unityscale.help = "Normalizes the scale of all instances to a uniform size, maintaining consistent."
op_name.par.Instances.help = "Start of the Sequential Parameter Block managing the input geometry instances."
op_name.par.Instances0pop.help = "Input POP for the current instance."
op_name.par.Instances0localscale.help = "Local uniform scale multiplier for this instance."
op_name.par.Instances0probability.help = "Probability weight for selecting this instance when Indexing Mode is set to."
op_name.par.Instances0centerinstance.help = "Centers this specific instance in world space before instancing, aligning its."
op_name.par.Instances0unityscale.help = "Normalizes the scale of this specific instance to a uniform size, maintaining."

# Page: Distribution
op_name.par.Linearsettings.help = "Opens settings for linear distribution."
op_name.par.Radialsettings.help = "Opens settings for radial distribution."
op_name.par.Sphericalsettings.help = "Opens settings for spherical distribution."
op_name.par.Gridsettings.help = "Opens settings for grid distribution."
op_name.par.Honeycombsettings.help = "Opens settings for honeycomb distribution."
op_name.par.Pointcloudsettings.help = "Opens settings for point cloud distribution."
op_name.par.Meshsettings.help = "Opens settings for mesh distribution."
op_name.par.Curvesettings.help = "Opens settings for curve distribution."
op_name.par.Templateobject.help = "Template object for mesh, curve, or point cloud distribution."
op_name.par.Templategroup.help = "Group within template object to use."
op_name.par.Copytemplateattributes.help = "Copy attributes from template to instances."
op_name.par.Attrstocopy.help = "Specific attributes to copy from template."
op_name.par.Resettodefault.help = "Resets all distribution settings to default values."

# Page: Sorting
op_name.par.Pointattr.help = "Attribute to use for sorting."
op_name.par.Pointseed.help = "Seed for random number generator for randomly-ordered points."
op_name.par.Pointobj.help = "3D Object to use when sorting points relative to Object Z-axis."
op_name.par.Pointrev.help = "After sorting points, reverse their order."
op_name.par.Pointshift.help = "Enables offsetting on sorted points."
op_name.par.Pointoffset.help = "Shifts the point order by this offset."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Instancer parameter help text updated successfully!")
