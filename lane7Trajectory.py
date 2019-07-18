import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

VehicleID_Merge = np.loadtxt('../NGSIM_I80_1stTimePeriod_MergeVehicleID_2rejectContinuousLaneChange.csv',delimiter=",")
data_lane67 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane567.csv',delimiter=',',skiprows=1,usecols=(range(0,14)))
print(VehicleID_Merge)
print("Number of merge vehicle: " + str(VehicleID_Merge.size))
# print(data_lane67)

fig = plt.figure('Scatter Fig')
ax1 = fig.add_subplot(111)

xLimit = [100, 930]
ax1.set_title('Merging trajectory')
plt.xlabel('local_y')
plt.ylabel('local_x')
plt.xlim(xLimit[0], xLimit[1])
plt.ylim(100, 0)

plt.plot(xLimit, [47.699, 47.699], color='black',linestyle="--")
plt.plot(xLimit, [60.422, 60.422], color='black',linestyle="--")
plt.plot(xLimit, [74.421, 74.421], color='black',linestyle="--")
plt.plot([859, 357.43], [74.421, 100], color='black',linestyle="--")
plt.annotate('...', (210,33))
plt.annotate('Lane 4', (200,41))
plt.annotate('Lane 5', (200,55))
plt.annotate('Lane 6', (200,68.4))
plt.annotate('Lane 7', (200,81))
# 显示图片时不暂停程序
plt.ion()
for vehicleID in VehicleID_Merge:
    idx = (data_lane67[:, 0] == vehicleID)
    local_x = data_lane67[idx, 4]
    local_y = data_lane67[idx, 5]
    ax1.scatter(local_y, local_x, s=1, alpha=0.3)
    plt.show()
    plt.pause(0.1)
# plt.legend('x1')

