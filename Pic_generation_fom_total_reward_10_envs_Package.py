"20250515"
# 用于生成10个并行环境中，每个环境的总奖励随着episode变化的曲线图。
# 对上述数据进行95%置信区间的计算，并画出平均奖励随episode变化的曲线图。

import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set_theme()
import csv
import numpy as np

def pic_generation_fom_total_reward_10_envs(RL_data_path):
    env_name_list = sorted(
        [envs for envs in os.listdir(RL_data_path) if re.search(r"^env\d+$", envs)]
    )
    
    env_path_list = ["/".join([RL_data_path, i]) for i in env_name_list]

    for env_path in env_path_list:

        # path_of_episode_reward = os.path.join(os.getcwd(), f"{env_path}", "total_reward.csv")
        path_of_episode_reward = os.path.join(os.getcwd(), f"{env_path}", "total_reward.csv")

        # 打开CSV文件
        with open(path_of_episode_reward, mode='r', newline='') as file:
            data = []
            # 创建CSV读取器
            csv_reader = csv.reader(file)
            
            # 逐行读取CSV文件内容
            for row in csv_reader:
                # 将每一行的数据转换为浮点数并添加到all_data中
                data.append(float(row[0]))

        plt.figure(figsize=(8, 6))
        sns.lineplot(x=range(len(data)),y=data)
        # sns.relplot(x=range(len(data)),y=data,kind="line") # 与上面一行等价
        plt.xlabel("Episode")
        plt.ylabel("Total reward")
        plt.title("Reward among episodes")
        # plt.show()
        # print(env_path)
        plt.savefig(f"{env_path}_pics/{env_path.split('/')[-1]}.png")
        plt.close()

    
    all_reward_data = pd.DataFrame()

    for i in range(len(env_path_list)):
        reward_file = os.path.join(env_path_list[i], "total_reward.csv")
        total_reward = pd.read_csv(reward_file)
        all_reward_data = pd.concat([all_reward_data, total_reward], axis=1)

    all_reward_data.to_csv("all_reward_data.csv")

    plt.figure(figsize=(8, 6))

    time = range(all_reward_data.shape[0])

    data_mean = all_reward_data.mean(axis=1)
    data_std = all_reward_data.std(axis=1)
    data_min = data_mean - 1.96 * data_std
    data_max = data_mean + 1.96 * data_std

    plt.plot(time, data_mean, color="#2F4F4F", label='Mean reward')
    plt.fill_between(time, data_min, data_max, color="#1C1C1C", alpha=0.2, label='95% confidence interval')
    plt.legend()
    plt.xlabel("Episode")
    plt.ylabel("Total reward")
    # plt.xlim(0, 500)
    plt.ylim(-100, 0)
    plt.yticks(np.arange(-100, 0, 10))
    plt.title("Reward among episodes")

    plt.savefig('reward_plots.png')  # Save the plot to a file
    # plt.show()



if __name__ == "__main__":
    RL_data_path = os.path.join(os.getcwd())
    pic_generation_fom_total_reward_10_envs(RL_data_path)

    