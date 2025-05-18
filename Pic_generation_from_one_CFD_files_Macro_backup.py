"20250515"
# 用于生成某一case中各时间步C场图的paraview宏

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# get active source.
cfd_record_episode_1_episodic_reward_7983257301808048foam = GetActiveSource()


# set active source
SetActiveSource(cfd_record_episode_1_episodic_reward_7983257301808048foam)


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1423, 795]


# get layout
layout1 = GetLayout()


# Properties modified on renderView1
renderView1.UseGradientBackground = 0



# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]


# show data in view
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay = Show(cfd_record_episode_1_episodic_reward_7983257301808048foam, renderView1, 'UnstructuredGridRepresentation')


# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')


# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')


# trace defaults for the display properties.
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.Representation = 'Surface'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ColorArrayName = ['POINTS', 'p']
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.LookupTable = pLUT
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.OSPRayScaleArray = 'p'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SelectOrientationVectors = 'U'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ScaleFactor = 0.10399999618530274
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SelectScaleArray = 'p'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.GlyphType = 'Arrow'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.GlyphTableIndexArray = 'p'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.GaussianRadius = 0.005199999809265137
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SetScaleArray = ['POINTS', 'p']
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.OpacityArray = ['POINTS', 'p']
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.PolarAxes = 'PolarAxesRepresentation'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ScalarOpacityFunction = pPWF
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ScalarOpacityUnitDistance = 0.0832266165341263
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ExtractedBlockIndex = 1


# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.OSPRayScaleFunction.Points = [2.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 10.707599639892578, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 10.707599639892578, 1.0, 0.5, 0.0]


# show color bar/color legend
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SetScalarBarVisibility(renderView1, True)


# reset view to fit data
renderView1.ResetCamera()


# show data in view
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay = Show(cfd_record_episode_1_episodic_reward_7983257301808048foam, renderView1, 'UnstructuredGridRepresentation')


# reset view to fit data
renderView1.ResetCamera()


# show color bar/color legend
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# set scalar coloring
ColorBy(cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay, ('POINTS', 'C'))


# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)


# rescale color and/or opacity maps used to include current data range
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'C'
cLUT = GetColorTransferFunction('C')


# get opacity transfer function/opacity map for 'C'
cPWF = GetOpacityTransferFunction('C')


#Enter preview mode
layout1.PreviewMode = [800, 600]


# Hide orientation axes
renderView1.OrientationAxesVisibility = 0


# get color legend/bar for cLUT in view renderView1
cLUTColorBar = GetScalarBar(cLUT, renderView1)


# Properties modified on cLUTColorBar
cLUTColorBar.Title = 'Concentration'
cLUTColorBar.TitleFontSize = 14
cLUTColorBar.LabelFontSize = 14


# Properties modified on cLUTColorBar
cLUTColorBar.ScalarBarThickness = 14


# Properties modified on cLUTColorBar
cLUTColorBar.ScalarBarLength = 0.4


# Properties modified on cLUTColorBar
cLUTColorBar.RangeLabelFormat = '%-#6.1f'


# hide color bar/color legend
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SetScalarBarVisibility(renderView1, False)


# show color bar/color legend
cfd_record_episode_1_episodic_reward_7983257301808048foamDisplay.SetScalarBarVisibility(renderView1, True)


# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cLUT.ApplyPreset('Cool to Warm', True)


# current camera placement for renderView1
renderView1.CameraPosition = [0.5199999809265137, 0.5199999809265137, 1.9892984677157224]
renderView1.CameraFocalPoint = [0.5199999809265137, 0.5199999809265137, 0.04500000178813934]
renderView1.CameraParallelScale = 0.7367665576613001


# save animation
SaveAnimation('F:/RL_Fluid_Parallel_data/record_episode_500_2actions_6.0_2_256net_probes_126_10_parallel/env02_pics/Reward__Env_No_02_Episode_389_Total_reward_-34.9197247226127/black/Pic.png', layout1, ImageResolution=[800, 600],
    TransparentBackground=1,
    FrameWindow=[0, 98], 
    # PNG options
    CompressionLevel='0')


# get animation scene
animationScene1 = GetAnimationScene()


# get the time-keeper
timeKeeper1 = GetTimeKeeper()


#### saving camera placements for all active views


# current camera placement for renderView1
renderView1.CameraPosition = [0.5199999809265137, 0.5199999809265137, 1.9892984677157224]
renderView1.CameraFocalPoint = [0.5199999809265137, 0.5199999809265137, 0.04500000178813934]
renderView1.CameraParallelScale = 0.7367665576613001


#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).