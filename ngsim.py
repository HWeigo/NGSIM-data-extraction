import pandas as pd

#dataOri = pd.read_csv('../Next_Generation_Simulation__NGSIM__Vehicle_Trajectories_and_Supporting_Datai80.csv')
# data = dataOri[(dataOri['Lane_ID']>5) & (dataOri['Lane_ID']<9) & (dataOri['Location'] == 'i-80')]
#  data.to_csv("../NGSIM_80.csv",index=None)

dataI80 = pd.read_csv('../NGSIM_i80.csv')

id_2007 = dataI80[ dataI80['Vehicle_ID'] == 2007]

#print(dataI80.head())
#print(id_2007[::10])
list = id_2007[::10].values.tolist()
#Frames = list[:,2]
print(list)
print(type(id_2007))
print(type(list))
id_2007[::10].to_csv("../NGSIM_I80_Id2007.csv",index=None)