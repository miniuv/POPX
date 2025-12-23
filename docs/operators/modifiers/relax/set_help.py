# TouchDesigner Python Script - Set Relax Parameter Help Text

op_name = target

# Page: Relax
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause."
op_name.par.Pointsupdatepop.help = "Reference to a POP node downstream in the network when Solver Mode is set to."
op_name.par.Dofalloff.help = "Enables falloff-based modulation of the relaxation effect."
op_name.par.Falloffattr.help = "Specifies which attribute to use for falloff values that modulate the."
op_name.par.Relaxiters.help = "Number of relaxation passes to perform per frame."
op_name.par.Maxrelaxradius.help = "Maximum search distance for finding neighboring instances."
op_name.par.Maxneighbors.help = "Maximum number of neighboring instances to consider when using Neighbor method."
op_name.par.Maxaxisres.help = "Maximum voxel resolution along the longest axis when using Field method."
op_name.par.Kernelsize.help = "Size of the convolution kernel used for field-based relaxation."
op_name.par.Relaxstrength.help = "Overall intensity of the relaxation effect."
op_name.par.Initializepulse.help = "Resets the Advect solver to initial state."
op_name.par.Startpulse.help = "Begins Advect solver simulation from the current state."
op_name.par.Play.help = "Toggles playback of the Advect solver simulation."
op_name.par.Steppulse.help = "Advances the Advect solver by one frame."

# Page: Constraints
op_name.par.Constrainttogeo.help = "Enables constraint to a surface geometry, keeping instances from flying off."
op_name.par.Constraintgeo.help = "Reference to a POP geometry to use as constraint surface when no second input."
op_name.par.Displaygeo.help = "Shows the constraint geometry in the viewport for visualization."
op_name.par.Constrainttovolume.help = "Enables constraint to a 2D/3D texture volume, keeping instances confined within."
op_name.par.Constraintvolume.help = "Reference to a 2D/3D texture TOP to use as constraint volume when no third."
op_name.par.Forcestrength.help = "Intensity of the constraining force applied to keep instances within the volume."
op_name.par.Preshrink.help = "Number of pre-shrink iterations applied to the volume before constraint."
op_name.par.Size.help = "Size of the filter kernel applied to the constraint volume."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner."

print("Relax parameter help text updated successfully!")
