"20250518"
# 如果在main部分使用循环，可以在每次实验后生成所有env的的所有case的C场在各个时间步的图
# 但我建议还是一个个环境来操作，不然会发生不知名卡顿，或许使内存爆了

import os
from glob import glob
from Multi_pic_generation_openfoam_with_paraview_Counter_Package import pic_generation_openfoam

def process_episodes(base_dir, env_name, color):
    # 查找所有episode目录
    episode_dirs = glob(os.path.join(base_dir, f"{env_name}/cfd_record_episode_*"))
    for episode_dir in episode_dirs:
        print(os.path.basename(episode_dir).split('_')[-4])
    
    for episode_dir in episode_dirs:
        # 解析episode编号和奖励值
        dir_name = os.path.basename(episode_dir)
        parts = dir_name.split('_')
        episode_no = parts[-4]
        episode_reward = parts[-1]
        
        # 创建输出目录
        output_dir = os.path.join(base_dir, f"{env_name}_pics", f"Reward__Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}", f"{color}")
        os.makedirs(output_dir, exist_ok=True)

        pic_generation_openfoam(env_name, episode_no, episode_reward)
        

if __name__ == "__main__":
    base_dir = os.getcwd()
    
    # 处理所有环境
    # for env_num in range(1, 11):
    #     env_name = f"env{env_num:02d}"  # 格式化为env01, env02等
    env_name = "env10"
    if os.path.exists(os.path.join(base_dir, env_name)):
        process_episodes(base_dir, env_name, color = "black")
