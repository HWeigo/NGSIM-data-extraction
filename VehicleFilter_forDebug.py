import numpy as np
import pandas as pd

dataOri = pd.read_csv('../NGSIM_i80_Lane67.csv')

data_car = dataOri[(dataOri['Vehicle_ID'] == 395) | (dataOri['Vehicle_ID'] == 7)]
data_car.to_csv("../NGSIM_I80_vehicle7_vehicle395.csv",index=None)