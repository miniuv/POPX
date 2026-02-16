# TouchDesigner Python Script - Set SBPP Parameter Help Text

op_name = target

# Page: Operations
op_name.par.Bluriterations.help = "Number of smoothing iterations to apply to the mesh. Set to 0 to disable smoothing."
op_name.par.Maxneighbors.help = "Maximum number of neighboring vertices used for each smoothing step."
op_name.par.Blurstrength.help = "Blend amount between original and smoothed positions per iteration."
op_name.par.Depth.help = "Number of subdivision levels to apply to the mesh. Set to 0 to disable subdivision."
op_name.par.Creaseweight.help = "Controls edge sharpness during subdivision. Higher values preserve hard edges."
op_name.par.Simplecoeffs.help = "Uses simplified subdivision coefficients for faster computation."

# Page: Visualize
op_name.par.Simulatedgeometry.help = "Display the simulated geometry."
op_name.par.Collisions.help = "Visualize collision detection points."
op_name.par.Collisionscolorr.help = "Color for collision detection visualization."
op_name.par.Selfcollision.help = "Visualize self-collision detection points."
op_name.par.Selfcollisioncolorr.help = "Color for self-collision detection visualization."
op_name.par.Thickness.help = "Visualize point thickness values."
op_name.par.Thicknesscolorr.help = "Color for thickness visualization."
op_name.par.Distancealongedges.help = "Visualize distance constraints along mesh edges."
op_name.par.Distalongedgescolorr.help = "Color for distance along edges visualization."
op_name.par.Bendacrosstriangles.help = "Visualize bending constraints across triangle edges."
op_name.par.Bendacrosstricolorr.help = "Color for bend across triangles visualization."
op_name.par.Struts.help = "Visualize strut constraints."
op_name.par.Strutscolorr.help = "Color for struts visualization."
op_name.par.Attachtogeometry.help = "Visualize attachment constraints to collision geometry."
op_name.par.Attachtogeocolorr.help = "Color for attach to geometry visualization."
op_name.par.Pintotarget.help = "Visualize pinned points."
op_name.par.Pintotargetcolorr.help = "Color for pin to target visualization."
op_name.par.Pintotargetscale.help = "Scale of the pin to target visualization points."
op_name.par.Property.help = "Constraint property to visualize on the mesh."
op_name.par.Displayproperty.help = "Show the selected property visualization on constraints."
op_name.par.Maxvalue.help = "Maximum value for property color mapping range."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("SBPP parameter help text updated successfully!")
