import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

VehicleID_Merge = np.loadtxt('../NGSIM_I80_1stTimePeriod_MergeVehicleID_new.csv',delimiter=",")
data_lane67 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane67.csv',delimiter=',',skiprows=1,usecols=(range(0,14)))
# VehicleID_Merge = np.delete(VehicleID_Merge, np.where(VehicleID_Merge == 355))
VehicleID_Merge = np.delete(VehicleID_Merge, np.where(VehicleID_Merge == 1137))
# VehicleID_Merge = np.delete(VehicleID_Merge, np.where(VehicleID_Merge == 2055))
print(VehicleID_Merge)
# print(data_lane67)

fig = plt.figure('Scatter Fig')
ax1 = fig.add_subplot(111)

xLimit = [100, 1000]
ax1.set_title('Merging trajectory')
plt.xlabel('local_y')
plt.ylabel('local_x')
plt.xlim(xLimit[0], xLimit[1])
plt.ylim(100, 0)

plt.plot(xLimit, [60.422, 60.422], color='black')
plt.plot(xLimit, [74.421, 74.421], color='black')
for vehicleID in VehicleID_Merge:
    idx = (data_lane67[:, 0] == vehicleID)
    local_x = data_lane67[idx, 4]
    local_y = data_lane67[idx, 5]
    ax1.scatter(local_y, local_x, s=1, alpha=0.3)
# plt.legend('x1')
plt.show()
