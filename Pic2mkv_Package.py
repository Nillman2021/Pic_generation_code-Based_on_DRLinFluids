"20250515"
# create_mkv_from_pngs
# 将某一文件夹内的png图片转换为mkv视频文件，当然这里要注意帧率问题，我的仿真文件每秒保存20张，所以设置为fps=20
# create_mkv_from_pngs_one_env
# 遍历env**_pics的所有目标文件夹，将期内的图片转换为mkv文件，存储到env**_pics文件夹目录下
# 切记保证文件夹组织结构的正确性，否则会报错

import cv2
import os
import re
from pathlib import Path

def create_mkv_from_pngs_one_env(input_dir, pic_color):
    # 遍历保存的episode子目录，并将其中的图片转化为mkv文件，存储到对应文件夹
    input_dir_Path = Path(input_dir)
    file_list = [e for e in input_dir_Path.iterdir() if e.is_dir()]
    cfd_pic_file_list = file_list[2:]

    output_dir = os.path.join(os.getcwd(), f'{input_dir.split("/")[-1]}')

    for inner_file in cfd_pic_file_list:
        inner_file_path = os.path.join(inner_file, pic_color)
        
        # print("inner_file_path:",output_dir)

        create_mkv_from_pngs(inner_file_path, output_dir)


def create_mkv_from_pngs(input_png_path, output_mkv_path, fps=20):
# 其它格式的图片也可以
    img_array = []
    path = input_png_path  # 图片文件路径
    filelist = os.listdir(path)  # 获取该目录下的所有文件名
    for filename in filelist:
        #挨个读取图片
        img = cv2.imread(path+"/"+filename)
        #获取图片高，宽，通道数信息
        height, width, channel = img.shape

        #设置尺寸
        size = (width, height)
        #将图片添加到一个大“数组中”
        img_array.append(img)

    # avi：视频类型，mp4也可以
    # cv2.VideoWriter_fourcc(*'DIVX')：编码格式，不同的编码格式有不同的视频存储类型
    # fps：视频帧率
    # size:视频中图片大小
    fps=fps
    mkv_name = re.findall(r'Reward__Env_No.*\d+', input_png_path)[0]
    print("mkv_name:",mkv_name)
    videopath= os.path.join(output_mkv_path,f"{mkv_name}.mkv")
    
    out1 = cv2.VideoWriter(videopath,cv2.VideoWriter_fourcc(*'DIVX'),fps, size)
    for i in range(len(img_array)):
        out1.write(img_array[i])
    out1.release()


# 使用示例
if __name__ == "__main__":
    # 输入 PNG 文件路径
    input_png_path = os.path.join(os.getcwd(),"env02_pics")

    pic_color = "black"

    # 我的仿真文件要求20fps
    create_mkv_from_pngs_one_env(input_png_path, pic_color)