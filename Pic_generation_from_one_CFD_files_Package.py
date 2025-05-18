"20250515"
# 这个代码本来准备用于读取openFoam的流场文件，使用paraView进行可视化并生成C场的动态图，但是失败了
# paraview模块的使用，在一天时间内估计难以解决，但手动一个小时也能画出一张图，所以暂时放弃这个功能
# 所以在此生成手动过程中所需的文件夹
# paraView操作过程中，可以使用本地中的black和white宏文件进行操作，即以_Macro结尾的文件，具体操作方法如下：
# 1. 打开ParaView，点击菜单栏中的Tools-Macros-Record，开始录制宏。
# 2. 打开black和white的流场文件，点击菜单栏中的File-Open，选择流场文件。
# 3. 点击菜单栏中的Tools-Macros-Stop，停止录制宏。
# 4. 点击菜单栏中的Tools-Macros-Play，播放宏。
# 5. 点击菜单栏中的Tools-Macros-Save，保存宏。
# 6. 打开ParaView，点击菜单栏中的Tools-Macros-Open，选择保存好的宏文件。
# 7. 点击菜单栏中的Tools-Macros-Execute，执行宏。

import os

def pic_generation_from_cfd_record_episode_files_openfoam(env_name, episode_no, episode_reward):

    os.makedirs(f'{env_name}_pics/Reward__Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}/black', exist_ok=True)
    
    os.makedirs(f'{env_name}_pics/Mkv_black', exist_ok=True)


if __name__ == '__main__':
    env_name = 'env10'
    episode_no = 1
    episode_reward = -79.83257301808048
    pic_generation_from_cfd_record_episode_files_openfoam(env_name, episode_no, episode_reward)