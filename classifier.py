# 用于提取车道数据，注意：NGSIM.csv文件当中包含多段时间的数据，选先区分时间段

import pandas as pd
import numpy as np

dataOri = pd.read_csv('../NGSIM_I80.csv')

# # 提取i80数据
# data = dataOri[(dataOri['Location'] == 'i-80')]
# data.to_csv("../NGSIM_I80.csv",index=None)

# 提取车道6,7数据

data = dataOri[(dataOri['Lane_ID'] == 5 ) | (dataOri['Lane_ID'] == 6 ) |(dataOri['Lane_ID'] == 7 )  ]
data.to_csv("../NGSIM_i80_1stTimePeriod_Lane567.csv",index=None)

# # 提取车道6,7数据
# data = dataOri[(dataOri['Lane_ID'] == 6) | (dataOri['Lane_ID'] == 7) ]
# data.to_csv("../NGSIM_i80_1stTimePeriod_Lane67.csv",index=None)
#
# # 提取车道7数据
# data = dataOri[(dataOri['Lane_ID'] == 7)]
# data.to_csv("../NGSIM_i80_1stTimePeriod_Lane7.csv",index=None)

