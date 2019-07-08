import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data
dataI80 = pd.read_csv('../NGSIM_i80_forVisualization.csv')

# pandas.core.frame.DataFrame to List
list = dataI80.values.tolist()
print(list)

sectionLimits = [100, 800]
xLimit = [sectionLimits[0] - 5, sectionLimits[1] + 5]
yLimit = [-100, 200]

Frames = list[:,1]
print(Frames)

fig = plt.figure()
ax = fig.add_subplot(111)

rect = plt.Rectangle((0.1,0.1),0.5,0.3)
ax.add_patch(rect)

# plt.show()
