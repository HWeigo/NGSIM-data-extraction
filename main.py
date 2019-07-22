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
MasterID_Merged = DataSheet_Merge[:, 0]
EgoID_Merged = DataSheet_Merge[:, 1]
Frames_Merged = DataSheet_Merge[:, 2]

