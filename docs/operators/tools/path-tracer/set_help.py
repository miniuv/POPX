# TouchDesigner Python Script - Set Path-Tracer Parameter Help Text

op_name = target

# Page: Path Tracer
op_name.par.Rendermode.help = "Selects between realtime and offline rendering modes."
op_name.par.Refinesamples.help = "Enables progressive sample refinement in offline mode."
op_name.par.Maxrefinesamples.help = "Maximum number of refinement samples to accumulate in offline mode."
op_name.par.Done.help = "Read-only indicator showing refinement completion status."
op_name.par.Rendertop.help = "Reference to Render TOP providing camera and viewport settings that the path tracer will render to."
op_name.par.Reset.help = "Pulse to reset progressive accumulation and restart rendering."
op_name.par.Lockinput.help = "Freeze input geometry to prevent updates during progressive rendering."
op_name.par.Raysperpixel.help = "Number of rays cast per pixel per frame."
op_name.par.Maxbounces.help = "Maximum ray bounce depth for global illumination."
op_name.par.Renderemissives.help = "Enables rendering of emissive materials as light sources."
op_name.par.Enablefireflyclamp.help = "Clamps extremely bright samples to reduce firefly artifacts."
op_name.par.Fireflyclamp.help = "Maximum brightness value for firefly clamping."
op_name.par.Focallength.help = "Distance from camera where objects are in sharp focus."
op_name.par.Aperture.help = "Camera aperture size for depth of field."
op_name.par.Showfocalplane.help = "Displays the focal plane in the viewport for visualization."
op_name.par.Focalplanesize.help = "Size of the focal plane visualization."
op_name.par.Enablemotionblur.help = "Enables motion blur effect in realtime mode."
op_name.par.Blurstrength.help = "Motion blur intensity."
op_name.par.Blursamples.help = "Number of samples for motion blur quality."
op_name.par.Enabletonemap.help = "Apply tone mapping to convert HDR output to display range."
op_name.par.Exposure.help = "Exposure multiplier for tone mapping."
op_name.par.Gamma.help = "Gamma correction value for tone mapping output."

# Page: Denoiser
op_name.par.Denoiser.help = "Selects the denoising method."
op_name.par.Usemotionvectors.help = "Uses motion vectors for temporal reprojection accuracy."
op_name.par.Normalreject.help = "Threshold for rejecting temporal samples based on surface normal differences."
op_name.par.Depthreject.help = "Threshold for rejecting temporal samples based on depth differences."
op_name.par.Albedoreject.help = "Threshold for rejecting temporal samples based on albedo differences."
op_name.par.Diffusehistoryblend.help = "Temporal blend factor for diffuse lobe history accumulation."
op_name.par.Diffusevarianceblend.help = "Temporal blend factor for diffuse variance estimation."
op_name.par.Specularhistoryblend.help = "Temporal blend factor for specular lobe history accumulation."
op_name.par.Specularvarianceblend.help = "Temporal blend factor for specular variance estimation."
op_name.par.Diffpasses.help = "Number of a-trous wavelet filter passes for diffuse spatial denoising."
op_name.par.Diffcolor.help = "Sensitivity to color differences in diffuse spatial filtering."
op_name.par.Diffnormal.help = "Sensitivity to surface normal differences in diffuse spatial filtering."
op_name.par.Diffdepth.help = "Sensitivity to depth differences in diffuse spatial filtering."
op_name.par.Specpasses.help = "Number of a-trous wavelet filter passes for specular spatial denoising."
op_name.par.Speccolor.help = "Sensitivity to color differences in specular spatial filtering."
op_name.par.Specnormal.help = "Sensitivity to surface normal differences in specular spatial filtering."
op_name.par.Specdepth.help = "Sensitivity to depth differences in specular spatial filtering."
op_name.par.Smoothreflections.help = "Amount of specular reflection smoothing based on roughness."
op_name.par.Plugin.help = "File path to the NVIDIA OptiX denoiser plugin."
op_name.par.Optixhistoryblend.help = "Temporal history blend factor for OptiX denoiser."
op_name.par.Optixnormalreject.help = "Threshold for rejecting temporal samples based on surface normal differences for OptiX denoiser."
op_name.par.Optixdepthreject.help = "Threshold for rejecting temporal samples based on depth differences for OptiX denoiser."
op_name.par.Optixalbedoreject.help = "Threshold for rejecting temporal samples based on albedo differences for OptiX denoiser."

# Page: Common
op_name.par.Freeextragpumem.help = "Free memory that has accumulated when output memory has grown and shrunk."

print("Path-Tracer parameter help text updated successfully!")
