# TouchDesigner Python Script - Set Constraint-Property Parameter Help Text

op_name = target

# Page: Geometry
op_name.par.Scale.help = "Uniform scale multiplier applied to all axes."

# Page: Constraints
op_name.par.Constraintgroup.help = "Primitive group containing constraints to modify."
op_name.par.Enablestiff.help = "Enable modification of stiffness values."
op_name.par.Stiffness.help = "Multiplier for stiffness value."
op_name.par.Enabledampratio.help = "Enable modification of damping ratio values."
op_name.par.Dampingratio.help = "Damping ratio value (0-1). Higher values reduce oscillation."
#op_name.par.Restlengthscale.help = "Modify constraint rest length scale values."
op_name.par.Enablerestscale.help = "Enable modification of rest length scale values."
op_name.par.Restscale.help = "Multiplier for rest length. Values above 1.0 create pre-stretched constraints."
op_name.par.Enableplasticthreshold.help = "Enable modification of plastic threshold values."
op_name.par.Plasticthreshold.help = "Strain threshold before plastic deformation begins."
op_name.par.Enableplasticrate.help = "Enable modification of plastic rate values."
op_name.par.Plasticrate.help = "Rate of plastic deformation per frame once threshold is exceeded."
op_name.par.Enableplastichardening.help = "Enable modification of plastic hardening values."
op_name.par.Plastichardening.help = "Increase in stiffness as plastic deformation accumulates."

# Page: Map
op_name.par.Enablestiffmap.help = "Enable attribute-based stiffness mapping."
op_name.par.Stiffattr.help = "Primitive attribute to modify stiffness with."
op_name.par.Enabledampratiomap.help = "Enable attribute-based damping ratio mapping."
op_name.par.Dampratioattr.help = "Primitive attribute to modify damping ratio with."
op_name.par.Enablerestscalemap.help = "Enable attribute-based rest length scale mapping."
op_name.par.Restscaleattr.help = "Primitive attribute to modify rest length scale with."
op_name.par.Enableplasticthresholdmap.help = "Enable attribute-based plastic threshold mapping."
op_name.par.Plasticthresholdattr.help = "Primitive attribute to modify plastic threshold with."
op_name.par.Enableplasticratemap.help = "Enable attribute-based plastic rate mapping."
op_name.par.Plasticrateattr.help = "Primitive attribute to modify plastic rate with."
op_name.par.Enableplastichardeningmap.help = "Enable attribute-based plastic hardening mapping."
op_name.par.Plastichardeningattr.help = "Primitive attribute to modify plastic hardening with."

print("Constraint-Property parameter help text updated successfully!")
