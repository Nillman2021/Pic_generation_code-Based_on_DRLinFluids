import cv2
import numpy as np
import os
import glob
import math
import re
from Pic2mkv_Package import create_mkv_from_pngs_one_env


def calculate_grid_layout(num_videos):
    """计算最佳网格布局"""
    rows = int(math.sqrt(num_videos))
    cols = math.ceil(num_videos / rows)
    return rows, cols

def merge_videos_grid(input_dir='.', output_filename='merged_grid.mp4', layout=None, pic_color='black'):

    create_mkv_from_pngs_one_env(input_dir, pic_color)

    # 获取视频文件
    video_files = glob.glob(os.path.join(input_dir, '*.mkv'))
    video_files.sort(key = lambda x: int(re.findall(r'\d+', x[127:])[0]))
    # print(video_files)
    if not video_files:
        # print(f"No .mkv files found in {input_dir}")
        return
    
    # 初始化视频读取器
    readers = [cv2.VideoCapture(f) for f in video_files]
    num_videos = len(readers)
    
    # 确定网格布局
    if layout:
        rows, cols = map(int, layout.split('x'))
    else:
        rows, cols = calculate_grid_layout(num_videos)
    
    # 获取基准参数
    base_fps = readers[0].get(cv2.CAP_PROP_FPS)
    base_width = int(readers[0].get(cv2.CAP_PROP_FRAME_WIDTH))
    base_height = int(readers[0].get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 创建视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(
        output_filename,
        fourcc,
        base_fps,
        (base_width * cols, base_height * rows)
    )
    
    # 处理每一帧
    frame_count = 0
    
    # 预先提取所有视频的标题信息
    video_titles = []
    for filename in video_files:
        env_no = re.search(r'Env_No_(\d+)', filename).group(1)
        episode = re.search(r'Episode_(\d+)', filename).group(1)
        reward = re.search(r'reward_([-\d]+(?:\.\d+)?)', filename).group(1)
        video_titles.append(f"Env {env_no} Ep {episode} Reward {reward}")
    
    while True:
        grid_frames = []
        valid_frames = True
        
        # 读取所有帧
        for reader in readers:
            ret, frame = reader.read()
            if not ret:
                valid_frames = False
                break
            frame = cv2.resize(frame, (base_width, base_height))
            grid_frames.append(frame)
        
        if not valid_frames:
            break
            
        try:
            # 创建网格
            rows_list = []
            for i in range(rows):
                row_start = i * cols
                row_end = min(row_start + cols, num_videos)
                row_frames = grid_frames[row_start:row_end]
                
                # 补全最后一行的空白
                while len(row_frames) < cols:
                    blank = np.zeros((base_height, base_width, 3), dtype=np.uint8)
                    row_frames.append(blank)
                
                # 为每行视频添加标题
                row_with_titles = []
                for j, frame in enumerate(row_frames):
                    # 添加标题文本（顶部）
                    if row_start + j < len(video_titles):
                        text = video_titles[row_start + j]
                    else:
                        text = ""
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 0.5
                    thickness = 2
                    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
                    
                    # 动态计算背景高度（文字高度+20像素padding）
                    bg_height = text_size[1] + 20
                    # 添加半透明背景（顶部）
                    overlay = frame.copy()
                    cv2.rectangle(overlay, (0, 0), (base_width, bg_height), (0,0,0), -1)
                    cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)
                    
                    # 计算文字位置（垂直居中于背景）
                    text_x = int((base_width - text_size[0]) / 2)
                    text_y = int(bg_height - (bg_height - text_size[1]) / 2)
                    cv2.putText(frame, text, (text_x, text_y), 
                              font, font_scale, (255,255,255), thickness)
                    
                    row_with_titles.append(frame)
                
                rows_list.append(np.hstack(row_with_titles))
            
            merged_frame = np.vstack(rows_list)
            writer.write(merged_frame)
            
            frame_count += 1
            if frame_count % 10 == 0:
                print(f'Processed frame {frame_count}')
                
        except Exception as e:
            print(f"Error merging frame {frame_count}: {str(e)}")
            break
    
    # 释放资源
    for reader in readers:
        reader.release()
    writer.release()
    print(f"Successfully merged {num_videos} videos into {output_filename}")

if __name__ == '__main__':
    layout = "2x4"
    pic_color ='black'
    env_name = 'env10_pics'
    input_dir = os.path.join(os.getcwd(), f'{env_name}')
    output_filename = os.path.join(input_dir, f'Mkv_{pic_color}', f'{env_name}_merged.mkv')
    
    merge_videos_grid(input_dir, output_filename, layout, pic_color)

    # aa = "f:\\RL_Fluid_Parallel_data\\record_episode_500_2actions_6.0_2_512net_probes_357_10_parallel\\env10_pics\\Reward__Env_No_10_Episode_"
    # print(len(aa))