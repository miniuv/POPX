# TouchDesigner Python Script - Set Paint Falloff Parameter Help Text

op_name = target

# Page: Paint
op_name.par.Group.help = "If there are input groups, specifying a group name in this field will cause this POPX to act only upon the group specified."
op_name.par.Showgroup.help = "Highlights non-group instances in red to indicate areas that cannot be painted."
op_name.par.Paintmode.help = "Enables interactive paint mode for direct falloff editing in the viewport."
op_name.par.Home.help = "Resets the viewport camera to frame all geometry."
op_name.par.Autorotate.help = "Automatically rotates the viewport camera around the geometry."
op_name.par.Paint.help = "Hold to paint falloff values onto POPX or POP Geometry."
op_name.par.Paintkey.help = "Keyboard key used to activate painting."
op_name.par.Erase.help = "Hold to erase painted falloff values from instances."
op_name.par.Erasekey.help = "Keyboard key used to activate erasing."
op_name.par.Eraseall.help = "Clears all painted falloff values."
op_name.par.Eraseallkey.help = "Keyboard key used to erase all painted values."
op_name.par.Displaybrush.help = "Displays the brush as a sphere in the viewport."
op_name.par.Brushsize1.help = "Size of the paint and erase brush."
op_name.par.Transitionrange.help = "Width of the soft transition zone at the edge of painted regions."
op_name.par.Transitionalign.help = "Shifts the transition zone inward or outward relative to the paint boundary."
op_name.par.Transitiontype.help = "Interpolation curve used for the transition zone falloff."

# Page: Falloff
op_name.par.Combineop.help = "Mathematical operation used to combine this falloff with existing falloff values."
op_name.par.Combattrscope.help = "Specifies which falloff attribute to combine with when Combine Operation is not set to Set."
op_name.par.Swaporder.help = "Reverses the order of operands in the combine operation (A op B becomes B op A)."
op_name.par.Combstrength.help = "Blending factor for the combine operation, ranging from 0 (no effect) to 1 (full effect)."
op_name.par.Outputfalloffattr.help = "Name of the attribute where the final falloff values will be stored."
op_name.par.Previewfalloff.help = "When enabled, visualizes falloff values using a color ramp."
op_name.par.Fallofframp.help = "Color ramp preset used for visualizing falloff values when Preview Falloff is enabled."
op_name.par.Opencustumrampeditor.help = "Opens the custom color ramp editor for defining a custom falloff visualization gradient."
op_name.par.Resetcustomramp.help = "Resets the custom color ramp to its default state."

# Page: Remap
op_name.par.Remap.help = "Enables remapping controls for adjusting falloff value range and distribution."
op_name.par.Clamp.help = "When enabled, constrains falloff values to the 0-1 range."
op_name.par.Fit.help = "Enables remapping of falloff values from an input range to an output range."
op_name.par.Auto.help = "Automatically determines input range from actual min/max falloff values."
op_name.par.Inputmin.help = "Minimum value of the input range for remapping."
op_name.par.Inputmax.help = "Maximum value of the input range for remapping."
op_name.par.Outputmin.help = "Minimum value of the output range for remapping."
op_name.par.Outputmax.help = "Maximum value of the output range for remapping."
op_name.par.Invert.help = "Reverses the falloff values (1 - value)."
op_name.par.Enablerampremap.help = "Applies a custom curve defined by a ramp to remap the falloff values."
op_name.par.Openrampeditor.help = "Opens the ramp editor for defining the custom remapping curve."
op_name.par.Resetramp.help = "Resets the remap ramp editor."
op_name.par.Customramptop.help = "Reference to an external TOP for remap control. When specified, overrides the internal ramp editor."

# Page: Common
op_name.par.Bypass.help = "Pass through the first input to the output unchanged."
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."
op_name.par.Renderprimitives.help = "Toggles rendering of POPX Geometry or shows it as point instances only."
op_name.par.Converttoptprim.help = "Converts points to primitive points when Render Primitives is toggled off."
op_name.par.Srtrst.help = "Sets the transform order when using POPX Geometry as built-in TouchDesigner instances."

print("Paint Falloff parameter help text updated successfully!")
