import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 变道车ID截取
dataLane7 = np.loadtxt('../NGSIM_I80_Lane7.csv',delimiter=",",skiprows = 1 , usecols=(range(0,14)))

print(dataLane7)
VehicleID_Merge = np.unique(dataLane7[:,0])
print("VehicleID_Merge:")
print(VehicleID_Merge)
np.savetxt('../NGSIM_I80_MergeVehicleID.csv',VehicleID_Merge, delimiter=',')


idx = (dataLane7[:,0] == 5)
V5_x = dataLane7[idx,4]
V5_y = dataLane7[idx,5]
print("local_x: "+ str(V5_x))
print("local_y: "+ str(V5_y))

# 绘图
fig = plt.figure('Scatter fig')
ax1 = fig.add_subplot(111)

ax1.set_title('Scatter Plot')
plt.xlabel('local_x')
plt.ylabel('local_y')
ax1.scatter(V5_y,V5_x)
plt.legend('x1')
plt.show()


# V233_x = dataLane7[x,6 for x in dataLane7[x,1] == 233 ]