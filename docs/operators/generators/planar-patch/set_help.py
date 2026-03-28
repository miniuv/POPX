# TouchDesigner Python Script - Set Planar Patch Parameter Help Text

op_name = target

# Page: Planar Patch
op_name.par.Shape.help = "Base shape of the planar mesh."
op_name.par.Edgelength.help = "Target edge length for generated triangles."
op_name.par.Relaxiters.help = "Number of relaxation iterations to improve triangle quality and uniformity."
op_name.par.Seed.help = "Random seed for point scattering variation."
op_name.par.Orient.help = "Orientation plane for the generated mesh."
op_name.par.Centerx.help = "Center position of the planar mesh in world space."
op_name.par.Scalex.help = "Scale of the planar mesh per axis."
op_name.par.Uniformscale.help = "Uniform scale factor applied to the entire mesh."
op_name.par.Roundcorners.help = "Rounds the corners of the rectangle shape. Enabled when Shape is Rectangle."
op_name.par.Cornerradius.help = "Radius of the rounded corners. Enabled when Round Corners is on and Shape is Rectangle."
op_name.par.Side.help = "Which side of the trapezoid is tapered. Enabled when Shape is Trapezoid."
op_name.par.Taper.help = "Amount of tapering applied to the selected side. Enabled when Shape is Trapezoid."
op_name.par.Skew.help = "Shifts the tapered side along its axis. Enabled when Shape is Trapezoid."
op_name.par.Innersizex.help = "Size of the inner hole for the ring shape. Enabled when Shape is Ring."
op_name.par.Openarc1.help = "Start and end angles in degrees for an open arc on the ring shape. Enabled when Shape is Ring."


# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Planar Patch parameter help text updated successfully!")
