import os
import re
import json
import numpy as np

def generation_cfd_episode_info():
    episode_nunber_list = []

    os_path = os.getcwd()

    env_name_list = sorted(
            [envs for envs in os.listdir(os_path) if re.search(r"^env\d+$", envs)]
        )

    env_path_list = [os.path.join(os_path, env_name) for env_name in env_name_list]

    cfd_episode_info_list = []

    for env_path in env_path_list:
        inner_cfd_recored_name_list = sorted(
            [recored for recored in os.listdir(env_path) if re.search(r"^cfd_record_episode.*", recored)]
        )
        # print(f"inner_cfd_recored_name_list in {env_path[-1]}:",inner_cfd_recored_name_list)
        key_info_inside = env_path.split("\\")[-1]
        episode_nunber_list = {key_info_inside:[]}
        
        for inner_cfd_recored_name in inner_cfd_recored_name_list:
            
            episode_nunber = re.findall(r"_\d+_", inner_cfd_recored_name)
            episode_reward = re.findall(r"-\d+.?\d+", inner_cfd_recored_name)
            # print("inner_cfd_recored_name:",inner_cfd_recored_name, episode_reward)
            # print(episode_reward[0][0:-1])
            episode_nunber_list[key_info_inside].append((int(episode_nunber[0][1:-1]),np.float64(episode_reward[0])))
            episode_nunber_list[key_info_inside].sort(reverse=False)

        cfd_episode_info_list.append(episode_nunber_list)

    json_path = os.path.join(os.getcwd(), "cfd_episode_info_list.json")

    json.dump(cfd_episode_info_list, open(json_path, 'w'), indent=4)

if __name__ == '__main__':
    generation_cfd_episode_info()