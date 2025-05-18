"20250518"
# 导入paraview库,并使用其进行某caseC场的批量生成，这个文件会生成counter_line图文件

from paraview.simple import *
import os

def pic_generation_openfoam(env_name, episode_no, episode_reward):
    """
    生成OpenFOAM数据可视化图片
    :param env_name: 环境名称
    :param episode_no: 回合编号 
    :param episode_reward: 回合奖励
    """
    # 创建视图
    renderView1 = GetActiveViewOrCreate('RenderView')
    renderView1.Background = [0,0,0]  # 纯黑色背景
    renderView1.OrientationAxesVisibility = 0  # 禁用方向指示器

    # 设置路径
    base_path = os.getcwd()
    case_path = os.path.join(base_path, f"{env_name}/cfd_record_episode_{episode_no}_episodic_reward_{episode_reward}/")
    output_path = os.path.join(base_path, f"{env_name}_pics/Reward__Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}/black/")

    # 创建OpenFOAM reader并获取所有区域
    openfoam = OpenFOAMReader(FileName=case_path)
    openfoam.MeshRegions = ['internalMesh', 'boundary']
    openfoam.CellArrays = ['C']

    # 创建边界表示
    boundary = ExtractBlock(Input=openfoam)
    boundary.Selectors = ['/boundary']
    boundaryDisplay = Show(boundary, renderView1)
    boundaryDisplay.Representation = 'Wireframe'
    boundaryDisplay.LineWidth = 2.0
    boundaryDisplay.AmbientColor = [1.0, 1.0, 1.0]
    boundaryDisplay.DiffuseColor = [1.0, 1.0, 1.0]

    # 获取所有时间步
    timesteps = openfoam.TimestepValues

    # 创建C场的完整contour表示 (保留counter line特有部分)
    contour = Contour(Input=openfoam)
    contour.ContourBy = ['POINTS', 'C']
    contour.ComputeNormals = 1
    contour.ComputeScalars = 1
    contour.Isosurfaces = [i/5.0 for i in range(6)]  # 保留多等值面设置

    contourDisplay = Show(contour, renderView1)
    contourDisplay.Representation = 'Surface'
    contourDisplay.ColorArrayName = ['POINTS', 'C']
    contourDisplay.LookupTable = GetColorTransferFunction('C')

    # 获取数据边界
    bounds = GetActiveSource().GetDataInformation().GetBounds()
    data_height = bounds[3] - bounds[2]
    data_width = bounds[1] - bounds[0]

    # 图像尺寸
    image_width = 600
    image_height = 500

    # 计算精确缩放比例（优先高度方向填充）
    scale_factor = (image_height/data_height) * 1.5  # 增加10%额外缩放

    # 计算视图尺寸
    view_height = data_height * scale_factor
    view_width = data_width * scale_factor

    # 确保宽度不超出图像边界
    if view_width > image_width:
        scale_factor = scale_factor * (image_width/view_width)
        view_height = data_height * scale_factor
        view_width = data_width * scale_factor

    # 计算中心点
    center = [(bounds[0]+bounds[1])/2, (bounds[2]+bounds[3])/2, (bounds[4]+bounds[5])/2]

    # 重置视图并统一视图设置
    ResetCamera()
    
    # 统一视图设置(与Counter_Package.py完全一致)
    renderView1.CenterAxesVisibility = 0
    renderView1.CenterOfRotation = center
    renderView1.ViewSize = [int(view_width), int(view_height)]
    renderView1.LockBounds = 1
    
    # 确保视图方向一致
    renderView1.CameraViewUp = [0, 1, 0]
    renderView1.CameraParallelProjection = 0

    # 配置颜色条
    cLUT = GetColorTransferFunction('C')
    cLUT.ApplyPreset('Cool to Warm', True)
    cLUT.RescaleTransferFunction(0.0,1.0)

    cLUTColorBar = GetScalarBar(cLUT, renderView1)
    cLUTColorBar.Title = 'Concentration'
    cLUTColorBar.TitleFontSize = 10
    cLUTColorBar.LabelFontSize = 10
    cLUTColorBar.ScalarBarThickness = 10
    cLUTColorBar.ScalarBarLength = 0.4
    cLUTColorBar.AutomaticLabelFormat = 1
    cLUTColorBar.CustomLabels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    cLUTColorBar.RangeLabelFormat = '%-#6.1f'
    cLUTColorBar.TitleColor = [1.0, 1.0, 1.0]
    cLUTColorBar.LabelColor = [1.0, 1.0, 1.0]


    # 遍历所有时间步并保存截图
    for i, t in enumerate(timesteps):
        animationScene = GetAnimationScene()
        animationScene.AnimationTime = t
        Render()
        SaveScreenshot(os.path.join(output_path, f"Pic.{i:04d}_Counter_line.png"), 
                     TransparentBackground=1,
                     ImageResolution=[550, 500],
                     CompressionLevel='0')

if __name__ == '__main__':
    # 初始化参数
    env_name = "env02"
    episode_no = "1"
    episode_reward = "-69.70362876230624"
    pic_generation_openfoam(env_name, episode_no, episode_reward)