from MergingDetailData import *
import numpy as np
import matplotlib.pyplot as plt

# VehicleID_Merge = np.loadtxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo.csv', delimiter=',', usecols=0)
# VehicleID_Ego = np.loadtxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo.csv', delimiter=',', usecols=1)
Data_lane567 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane567_simplification.csv', delimiter=',', skiprows=1,
                          usecols=(range(0, 17)))
DataSheet_Merge = np.loadtxt('../NGSIM_i80_DataSheet_Merge.csv', delimiter=',', skiprows=1, usecols=(range(0, 4)))
DataSheet_NonMerge = np.loadtxt('../NGSIM_i80_DataSheet_NonMerge.csv', delimiter=',', skiprows=1, usecols=(range(0, 4)))

print(DataSheet_Merge.shape)
print(DataSheet_NonMerge.shape)

#   主旁车ID
# MasterID_Merged = DataSheet_Merge[:, 0]
# EgoID_Merged = DataSheet_Merge[:, 1]
# Frames_Merged = DataSheet_Merge[:, 2]
MasterID_NonMerged = DataSheet_NonMerge[:, 0]
EgoID_NonMerged = DataSheet_NonMerge[:, 1]
Frames_NonMerged = DataSheet_NonMerge[:, 2]

# print(MasterID_Merged)
Col_master_vel = []
Col_master_acc = []
Col_master_gap = []
for i in range(MasterID_NonMerged.size):
    print(i)
    print(MasterID_NonMerged[i])
    vel, acc, gap_master = data_extraction_vehicle_master(MasterID_NonMerged[i], Frames_NonMerged[i], Data_lane567)[2:]
    Col_master_vel.append(vel)
    Col_master_acc.append(acc)
    Col_master_gap.append(gap_master)

Col_master_vel = np.array(Col_master_vel)
Col_master_acc = np.array(Col_master_acc)
Col_master_gap = np.array(Col_master_gap)
output_m = np.empty((Col_master_vel.size, 3))
print(output_m.shape)
for i in range(Col_master_vel.size):
    output_m[i][0] = Col_master_vel[i]
    output_m[i][1] = Col_master_acc[i]
    output_m[i][2] = Col_master_gap[i]
np.savetxt('../NGSIM_i80_NonMerge_Master_Parameters.csv', output_m, delimiter=',')

Col_ego_vel = []
Col_ego_acc = []
Col_ego_gap_front = []
Col_ego_gap_behind = []
Col_ego_label = []
for i in range(EgoID_NonMerged.size):
    print(EgoID_NonMerged[i])
    vel, acc, gap_front, gap_behind, label = data_extraction_vehicle_ego(EgoID_NonMerged[i], Frames_NonMerged[i],
                                                                         Data_lane567)[2:]
    Col_ego_vel.append(vel)
    Col_ego_acc.append(acc)
    Col_ego_gap_front.append(gap_front)
    Col_ego_gap_behind.append(gap_behind)
    Col_ego_label.append(label)

Col_ego_vel = np.array(Col_ego_vel)
Col_ego_acc = np.array(Col_ego_acc)
Col_ego_gap_front = np.array(Col_ego_gap_front)
Col_ego_gap_behind = np.array(Col_ego_gap_behind)
Col_ego_label = np.array(Col_ego_label)
output_e = np.empty((Col_ego_vel.size, 5))
print(output_e.shape)
for i in range(Col_ego_vel.size):
    output_e[i][0] = Col_ego_vel[i]
    output_e[i][1] = Col_ego_acc[i]
    output_e[i][2] = Col_ego_gap_front[i]
    output_e[i][3] = Col_ego_gap_behind[i]
    output_e[i][4] = Col_ego_label[i]
np.savetxt('../NGSIM_NonMerge_Ego_Parameters.csv', output_e, delimiter=',')
