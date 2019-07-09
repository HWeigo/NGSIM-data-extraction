import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 变道车ID截取
data_Lane7 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane7.csv',delimiter=",",skiprows = 1 , usecols=(range(0,14)))
data_Lane67 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane567.csv',delimiter=',',skiprows=1,usecols=(range(0,14)))

print(data_Lane7)
idx_auto = (data_Lane7[:,10] == 2) # 仅分类轿车
VehicleID_Merge_Ori = np.unique(data_Lane7[idx_auto,0])
print("VehicleID_Merge:")
print(VehicleID_Merge_Ori)
print("Number of origin merge vehicle:" + str(VehicleID_Merge_Ori.size))
# np.savetxt('../NGSIM_I80_1stTimePeriod_MergeVehicleID_Ori.csv',VehicleID_Merge_Ori, delimiter=',')


# idx = (data_Lane67[:, 0] == 186)
# vehicle_frame = data_Lane67[idx,1]-data_Lane67[idx,1].min() # 帧id从0计数
# vehicle_x = data_Lane67[idx,4]
# vehicle_y = data_Lane67[idx,5]
# vehicle_lane = data_Lane67[idx,13]
# print(vehicle_frame.size)
# print(vehicle_y.size)
# print(vehicle_lane.size)
#
# print(vehicle_frame)
# for frame in vehicle_frame:
#     frame_int = int(frame)
#     print(frame_int)
#     if vehicle_y[frame_int] > 270:
#         continue
#     else:
#         if vehicle_x[frame_int] < 75:
#             new = np.delete(VehicleID_Merge_Ori, 5)
# print(vehicle_frame[0])
# tmp =int(vehicle_frame[0])
# print(vehicle_y[tmp])
# #print(new)

# NGSIM_I80_1stTimePeriod_Lane67数据异常，误用！

# 剔除误记入汇流的数据
last_lane = 7
VehicleID_Merge = VehicleID_Merge_Ori
for vehicle_ID in VehicleID_Merge_Ori:
    # print(vehicle_ID)
    idx = (data_Lane67[:, 0] == vehicle_ID)
    vehicle_frame = data_Lane67[idx, 1] - data_Lane67[idx, 1].min()  # 帧id从0计数
    vehicle_x = data_Lane67[idx, 4]
    vehicle_y = data_Lane67[idx, 5]
    vehicle_lane = data_Lane67[idx, 13]

    for frame in vehicle_frame:
        lane = vehicle_lane[int(frame)]

        # 剔除借道车辆
        if (vehicle_y[int(frame)] < 410) and (vehicle_x[int(frame)] < 80):  # 270
            print('Delete Vehicle_ID: ' + str(vehicle_ID))
            VehicleID_Merge = np.delete(VehicleID_Merge, np.where(VehicleID_Merge == vehicle_ID))
            break

        # 剔除连续变道车辆
        if (last_lane == 7) & (lane == 6):
            mergePoint_y = vehicle_y[int(frame)]
            mergePoint_frame = frame
            # print("Vehicle " + str(vehicle_ID) + "change to lane 6.")
        if (last_lane == 6) & (lane == 5):
            leavePoint_y = vehicle_y[int(frame)]
            leavePoint_frame = frame
            print("Vehicle " + str(vehicle_ID) + "change to lane 5.")
            if (leavePoint_y - mergePoint_y < 70 ) or (leavePoint_frame - mergePoint_frame <40):
                print('Delete Vehicle_ID: (Change from 7 directly to 5) ' + str(vehicle_ID))
                VehicleID_Merge = np.delete(VehicleID_Merge, np.where(VehicleID_Merge == vehicle_ID))
                break
        last_lane = lane

print(VehicleID_Merge)

# 剔除连续变道

np.savetxt('../NGSIM_I80_1stTimePeriod_MergeVehicleID_rejectContinuousLaneChange.csv',VehicleID_Merge, delimiter=',')


# idx = (data_Lane7[:,0] == 5)
# V5_x = data_Lane7[idx,4]
# V5_y = data_Lane7[idx,5]
# print("local_x: "+ str(V5_x))
# print("local_y: "+ str(V5_y))
#
# # 绘图
# fig = plt.figure('Scatter fig')
# ax1 = fig.add_subplot(111)
#
# ax1.set_title('Scatter Plot')
# plt.xlabel('local_x')
# plt.ylabel('local_y')
# ax1.scatter(V5_y,V5_x)
# plt.legend('x1')
# plt.show()


# V233_x = data_Lane7[x,6 for x in data_Lane7[x,1] == 233 ]