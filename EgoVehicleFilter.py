import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

VehicleID_Merge = np.loadtxt('../NGSIM_I80_1stTimePeriod_MergeVehicleID_2rejectContinuousLaneChange.csv',delimiter=",")
data_lane567 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane567_simplification.csv',delimiter=',',skiprows=1,usecols=(range(0,17)))

last_lane = 7
VehicleID_Ego_list = []
for vehicleID in VehicleID_Merge:
    idx = (data_lane567[:, 0] == vehicleID)
    vehicle_frame = data_lane567[idx, 1] - data_lane567[idx, 1].min()  # 帧id从0计数
    vehicle_lane = data_lane567[idx, 13]
    PrecedingVehicle = data_lane567[idx, 14]
    FollowingVehicle = data_lane567[idx, 15]

    isFirstCount = 0
    for frame in vehicle_frame:
        lane = vehicle_lane[int(frame)]
        if lane == 6 and last_lane == 7:
            if isFirstCount == 0:
                isFirstCount = 1
                if FollowingVehicle[int(frame)] != 0:
                    VehicleID_Ego_list.append(FollowingVehicle[int(frame)])
                else:
                    print("Vehicle " + str(vehicleID) + " didn't encounter ego vehicle.")
                    VehicleID_Merge = np.delete(VehicleID_Merge, np.where(VehicleID_Merge == vehicleID))
            else:
                print("Vehicle " + str(vehicleID) + " merged morn than one time.")
        last_lane = lane

print(VehicleID_Ego_list)

VehicleID_Ego = np.array(VehicleID_Ego_list)
# VehicleID_Merge_list = VehicleID_Merge.tolist()

print(type(VehicleID_Ego))
print(type(VehicleID_Merge))

VehicleID = np.empty((VehicleID_Ego.size, 2))
print(VehicleID.shape)
for vehicle in range(VehicleID_Ego.size):
    VehicleID[vehicle][0] = VehicleID_Merge[vehicle]
    VehicleID[vehicle][1] = VehicleID_Ego[vehicle]

print(VehicleID)

# np.savetxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo.csv', VehicleID, delimiter=',')

