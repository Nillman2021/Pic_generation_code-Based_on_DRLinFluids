

# Pic_generation_code-Based_in_DRLinFluids
This code is made to draw some pics, which use the data generaterd in the DRLinFluids simulation process.

We donot need care about the code that end with "Package", what only useful is the code end with "Run", yes, just run it. 

But what shoud care about is that, there should have the files in /env01(or /env02 or /env03 ...) named like "cfd_record_episode_1_episodic_reward_-57.35210136077975" or "cfd_record_episode_283_episodic_reward_-46.807446563400276", in which, 1(or 283) mean that, until now, the episode 1(283) is best episode that have the highest total reward.

需要在DRLinFluids中环境文件的reset模块中，对目前的episode总奖励与之前的最最高奖励做对比，若当前episode的奖励为目前最高，则保存当前的全部仿真文件到env01文件夹下(以"cfd_record_episode_283_episodic_reward_-46.807446563400276"模式命名，其内存贮了当前episode的openfoam运行结果文件)，当然如果是10个环境用不同的种子学习的话，会有十个env文件，如env01,env02....env10。每个env**文件夹下都应有以"cfd_record_episode_283_episodic_reward_-46.807446563400276"模式命名的文件夹。

![image](https://github.com/Nillman2021/Pic_generation_code-Based_on_DRLinFluids/blob/main/env01_pics_merged.gif)

# 1 Generation_cfd_episode_info_Package:
which was uesd to generate one json file, in which total reward and No. of best episode till now will be shown.

# 2 Pic_generation_fom_total_reward_10_envs_Package #
which was used to generate 10+1 pics, in which the change of total reward among 10 env files was shown, and also, the pic of mean total reward among episodes was shown in the "1" another pic.

# 3 Pic_generation_from_one_info_list_files_Package #
which was used to shown the reward data among trajectory in the episode (that we have mentioned before) that have the best total reward until now. But here we just use the "info_list_*"files in the /env01(or /env02 or /env03 ...)

# 4 Pic_generation_for_all_info_list_files_Run #
which use all the three code mentioned before to generate picsss that what we need (or not). Let the code work and then we can plat BF1.

# 5 Pic_generation_from_one_CFD_files_Macro_backup #
The mocro can be used to generate pics of phied C in the simulation case, but it should be edited everytime u generate pics of different cases, which is prcetty time-wasting.

# 6 Multi_pic_generation_openfoam_with_paraview_Counter_line_Package #
This code can be used to generate pics automatically, maybe other guys in your research group have codes like this, so u can get it when u say:"Bro! help me!", but, people may not always be so lucky like that. So this codes can help u (but forgive me, this codes was kind of seems like noodles, u know that)

# 7 Multi_pic_generation_openfoam_with_paraview_Counter_Package #
Just like #6, but this will generate different kind of pics.

# 8 Multi_pic_generation_openfoam_with_paraview_Run #
uee above #6/7 codes to generate all pics in all your simulation files(like env01, env02, env03...)

# 9 Pic2mkv_Package #
transfer the pics generated in different times to videos, in fact u can done this process use paraview, but there may have 100 simulation cases, and I want play BF1 now.

# 10 Pics2mkv2mkvs_Run #
combine the videos generated in #9 to 1 visdes, and there may show some infomation of different videos on the top, especially.
