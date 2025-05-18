"20250515"
# 生成json文件某一episode的reward&action分布图

import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set_theme()
import csv

def pic_generation_from_cfd_record_episode_files_line(env_name, episode_no, episode_reward):

    episode_no_path = os.path.join(os.getcwd(), env_name, f"info_list_{episode_no}.csv")

    with open(episode_no_path, 'r') as f:
        reader = csv.reader(f)
        episode_info_list = list(reader)

    current_trajectory_reward_list = []
    episode_reward_list = []
    actions_x_list = []
    actions_y_list = []

    for i in range(len(episode_info_list)):
        if i == 0:
            pass
        else:
            current_trajectory_reward_list.append(float(episode_info_list[i][7]))
            episode_reward_list.append(float(episode_info_list[i][8]))
            actions_list_inside = re.findall(r'\d+\.[0-9a-z-+]{0,}', episode_info_list[i][9])
    
            for action in actions_list_inside:
                if action[-4:] == 'e+00':
                    print("action before:",action)
                    action = action[:-4]
                    print("action after:",action)

            actions_x_list.append(pd.to_numeric(actions_list_inside[0]))
            actions_y_list.append(pd.to_numeric(actions_list_inside[1]))
            # actions_x_list.append(pd.to_numeric((re.findall(r'\d+\.[0-9a-z-]{0,}', episode_info_list[i][9]))[0]))
            # actions_y_list.append(pd.to_numeric((re.findall(r'\d+\.[0-9a-z-]{0,}', episode_info_list[i][9]))[1]))
    
    plt.rcParams["figure.figsize"] = (8,6)

    plt.figure(1)
    fig, ax1 = plt.subplots(1)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax1.set_xlabel('Trajectory')
    ax1.set_ylabel('Current trajectory reward', color=color)
    ax1.set_ylim(-2.5, 0.125)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.plot(current_trajectory_reward_list, label='Current trajectory reward', color=color)
    
    # 创建第二个y轴，共享x轴
    color = 'tab:green'
    ax2.set_ylabel('Episode reward', color=color)
    ax2.set_ylim(-100, 5)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot(episode_reward_list, label='Episode reward', color=color)

    ax1.grid(1)
    ax2.grid()
    # 添加图例
    # fig.tight_layout()  # 调整子图参数，使之填充整个图像区域

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()

    ax1.legend(lines + lines2, labels + labels2, loc='lower left')

    # 设置标题
    plt.title(f'Reward: Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}')
    # 保存并显示图表
    plt.savefig(f'{env_name}_pics/Reward__Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}.png')
    # plt.show()
    plt.close()

    plt.figure(2)
    plt.plot(actions_x_list, label='actions_x')
    plt.plot(actions_y_list, label='actions_y')
    plt.legend()
    plt.xlabel('Trajectory')
    plt.ylabel('Actions (m/s)')
    # plt.xlim(0, 100)
    plt.ylim(0.0, 6.0)
    plt.title(f'X-Y_Actions: Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}')
    plt.savefig(f'{env_name}_pics/X-Y_Actions__Env_No_{env_name[-2:]}_Episode_{episode_no}_Total_reward_{episode_reward}.png')
    # plt.show()
    plt.close()

    current_trajectory_reward_list.clear()
    episode_reward_list.clear()
    actions_x_list.clear()
    actions_y_list.clear()

if __name__ == '__main__':
    env_name = 'env01'
    episode_no = 1
    episode_reward = -31.842497510855882
    pic_generation_from_cfd_record_episode_files_line(env_name, episode_no, episode_reward)