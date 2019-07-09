import pandas as pd
import numpy as np


# dataOri = pd.read_csv('../Next_Generation_Simulation__NGSIM__Vehicle_Trajectories_and_Supporting_Datai80.csv')
# data = dataOri[(dataOri['Location'] == 'i-80')]
# data.to_csv("../NGSIM_80_Ori.csv",index=None)

dataI80 = pd.read_csv('../NGSIM_i80_Ori_1stPeriod.csv')

Lane_x = []
for i in range(1,8):
    lane = dataI80[(dataI80['Lane_ID'] == i)]
    lane_x = lane['Local_X'].values.tolist()
    Lane_x.append(np.mean(lane_x))
print("Lanex_x:")
print(Lane_x)

Lane_boundary = []
for i in range(1,7):
    Lane_boundary.append((Lane_x[i-1]+Lane_x[i])/2)
print(Lane_boundary)

