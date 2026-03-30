def colorOp(rootOp, color=(1, 0.5, 0.1)):
	if not rootOp:
		return
	rootOp.color = color
	for child in rootOp.children:
		colorOp(child, color)

def deleteKeyboardShortcut(target):
	"""Delete keyboard_shortcut operator inside target's POPXExt"""
	# Find POPXExt inside the target, try POPXExt first, then POPXExt1
	popx_ext = target.op('POPXExt')
	if popx_ext is None:
		popx_ext = target.op('POPXExt1')

	if popx_ext is None:
		print(f"Warning: POPXExt or POPXExt1 not found in {target.path}")
		return

	kb_shortcut = popx_ext.op('keyboard_shortcut')
	if kb_shortcut is None:
		print(f"Warning: keyboard_shortcut not found in {popx_ext.path}")
		return

	kb_shortcut.destroy()
	print(f"Deleted keyboard_shortcut from {popx_ext.path}")

def updateToxBuild(rootOp):
	if not rootOp:
		return

	docs = rootOp.op('docsHelper')
	if docs and hasattr(docs.par, 'Settoxsavebuild'):
		docs.par.Settoxsavebuild.pulse()

	for child in rootOp.children:
		updateToxBuild(child)

def setHelp(target):
	"""Execute the set_help.py script for the operator based on its tags."""
	# Map operator tags to their set_help.py script paths
	help_scripts = {
		'Magnetize': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/magnetize/set_help.py',
		'Soft Body': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/soft-body/set_help.py',
		'Flow': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/flow/set_help.py',
		'Constraints': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/constraints/set_help.py',
		'Constraint Property': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/constraint-property/set_help.py',
		'Aim': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/aim/set_help.py',
		'Color Modifier': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/color-modifier/set_help.py',
		'Noise Modifier': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/noise-modifier/set_help.py',
		'Pivot': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/pivot/set_help.py',
		'Randomize': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/randomize/set_help.py',
		'Relax': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/relax/set_help.py',
		'Spring Modifier': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/spring-modifier/set_help.py',
		'Transform Modifier': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/transform-modifier/set_help.py',
		'Move Along Curve': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/move-along-curve/set_help.py',
		'Move Along Mesh': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/move-along-mesh/set_help.py',
		'Attribute Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/attribute-falloff/set_help.py',
		'Combine Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/combine-falloff/set_help.py',
		'Curve Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/curve-falloff/set_help.py',
		'Infection Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/infection-falloff/set_help.py',
		'Noise Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/noise-falloff/set_help.py',
		'Object Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/object-falloff/set_help.py',
		'Remap Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/remap-falloff/set_help.py',
		'Shape Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/shape-falloff/set_help.py',
		'Spread Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/spread-falloff/set_help.py',
		'Texture Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/texture-falloff/set_help.py',
		'Convert': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/generators/convert/set_help.py',
		'Explode': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/generators/explode/set_help.py',
		'Instancer': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/generators/instancer/set_help.py',
		'Subdivider': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/generators/subdivider/set_help.py',
		'Sweep': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/generators/sweep/set_help.py',
		'DLA': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/dla/set_help.py',
		'DLG': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/dlg/set_help.py',
		'Mesh Fill': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/mesh-fill/set_help.py',
		'Path Tracer': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/path-tracer/set_help.py',
		'Physarum': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/physarum/set_help.py',
		'Particle': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/particle/set_help.py',
		'Apply Attributes': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/apply-attributes/set_help.py',
		'Attribute To Index': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/attribute-to-index/set_help.py',
		'Delete': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/delete/set_help.py',
		'Extract Attributes': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/extract-attributes/set_help.py',
		'Geo': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/geometry/set_help.py',
		'Material': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/material/set_help.py',
		'Merge': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/merge/set_help.py',
		'Orient Curve': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/orient-curve/set_help.py',
		'Orient Mesh': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/orient-mesh/set_help.py',
		'POPXto': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/popx-to/set_help.py',
		'Preview Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/preview-falloff/set_help.py',
		'Reorient': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/reorient/set_help.py',
		'Unpack': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/unpack/set_help.py',
		'Visualize Frame': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/visualize-frame/set_help.py',
		'Voxelize': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/voxelize/set_help.py',
		'Constraints Config': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/constraints-config/set_help.py',
		'Advect': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/modifiers/advect/set_help.py',
		'Measure': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/measure/set_help.py',
		'SA': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/sa/set_help.py',
		'Light': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/light/set_help.py',
		'SBPP': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/sbpp/set_help.py',
		'SSFR': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/tools/ssfr/set_help.py',
		'Planar Patch': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/generators/planar-patch/set_help.py',
		'Paint Falloff': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/falloffs/paint-falloff/set_help.py',
		'Shortest Path': 'c:/Users/Admin/OneDrive/Documents/GitHub/POPX/docs/operators/simulations/shortest-path/set_help.py',

	}

	# Check each tag and execute the corresponding help script
	for tag in target.tags:
		if tag in help_scripts:
			script_path = help_scripts[tag]
			try:
				with open(script_path, 'r') as f:
					script_code = f.read()
				# Execute the script with the target operator passed as 'target'
				exec(script_code, {'target': target})
				print(f"Set help text for {target.name} using tag '{tag}'")
			except Exception as e:
				print(f"Error setting help for {target.name} with tag '{tag}': {e}")
			break  # Only execute once per operator


def setInstancerExpressions(target):
	"""Set bypass and pop expressions on instancer1 inside target."""
	instancer = target.op('instance1/template')
	if instancer is None:
		return

	instancer.par.bypass.expr = "not parent.POPX.op('POPXExt').par.Popxmode"
	instancer.par.bypass.mode = ParMode.EXPRESSION

	instancer.par.pop.expr = "parent.POPX.op('POPX_out1')"
	instancer.par.pop.mode = ParMode.EXPRESSION

	print(f"Set instancer expressions for {target.name}")

def updateOpInfo(target):
	"""Update op_version and fam_version in FamManifest/OpInfo to match target.par.Version."""
	op_info = target.op('FamManifest/OpInfo')
	if op_info is None:
		return

	version = str(target.par.Version)
	try:
		import json
		info = json.loads(op_info.text)
		info['op_version'] = version
		info['fam_version'] = version
		op_info.text = json.dumps(info, indent=4)
		print(f"Updated OpInfo versions to {version} for {target.name}")
	except Exception as e:
		print(f"Error updating OpInfo for {target.name}: {e}")

def copyKeyboardShortcut(target):
	"""Copy keyboard_shortcut operator inside target's POPXExt"""
	source_op = op('keyboard_shortcut')

	if source_op is None:
		print("Error: keyboard_shortcut operator not found")
		return

	# Find POPXExt inside the target, try POPXExt first, then POPXExt1
	popx_ext = target.op('POPXExt')
	if popx_ext is None:
		popx_ext = target.op('POPXExt1')

	if popx_ext is None:
		print(f"Warning: POPXExt or POPXExt1 not found in {target.path}")
		return

	# Check if keyboard_shortcut already exists in POPXExt
	existing_shortcut = popx_ext.op('keyboard_shortcut')
	if existing_shortcut is not None:
		try:
			existing_shortcut.destroy()
			print(f"Destroyed existing keyboard_shortcut in {popx_ext.path}")
		except Exception as e:
			print(f"Failed to destroy existing keyboard_shortcut in {popx_ext.path}: {e}")
			return

	try:
		# Copy the keyboard_shortcut operator inside POPXExt
		copied_op = popx_ext.copy(source_op)
		print(f"Copied keyboard_shortcut to: {popx_ext.path}")
	except Exception as e:
		print(f"Failed to copy keyboard_shortcut to {popx_ext.path}: {e}")

		
def onPulse(par):
	for block in parent().seq.Ops.blocks:
		op = block.par.Op
		target = op.eval()

		if not target:
			continue

		if 'POPX' not in target.tags:
			continue

		colorOp(
			target,
			color=(
				parent().par.Colorr.eval(),
				parent().par.Colorg.eval(),
				parent().par.Colorb.eval()
			)
		)

		#deleteKeyboardShortcut(target)
		#setInstancerExpressions(target)
		updateToxBuild(target)
		copyKeyboardShortcut(target)
		setHelp(target)

		if hasattr(target.par, 'Version'):
			target.par.Version = parent().par.Version.eval()
			updateOpInfo(target)
	return
