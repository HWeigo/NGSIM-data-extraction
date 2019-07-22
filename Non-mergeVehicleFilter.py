from MergingDetailData import *
import numpy as np
#  numpy关闭科学计数
np.set_printoptions(suppress=True)

VehicleID_Merge = np.loadtxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo_Titled.csv', delimiter=',', usecols=0)
# VehicleID_Ego = np.loadtxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo.csv', delimiter=',',  usecols=1)
data_lane67 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane67_simplification.csv', delimiter=',', skiprows=1,
                         usecols=(range(0, 17)))


def find_vehicle_frame(frame_func, data):
    idx = (data[:, 1] == frame_func)
    vehicle_id = data[idx, 0]
    local_y = data[idx, 5]
    return vehicle_id, local_y


Col_masterID = []
Col_egoID = []
Col_frame = []
for master_id in VehicleID_Merge:
    print(master_id)
    frames, master_xs, master_ys = data_extraction_vehicle(master_id, data_lane67)[:3]
    ego_ids_ori_list = []
    ego_frames_ori_list = []
    for frame in frames:
        master_y = data_extraction_vehicle_common(master_id, frame, data_lane67)[1]
        if master_y > 485:
            ids, ys = find_vehicle_frame(frame, data_lane67)
            cnt = 0
            for y in ys:
                if abs(master_y - y) < 5:
                    ego_id = ids[cnt]
                    if ego_id != master_id:
                        ego_ids_ori_list.append(ego_id)
                        ego_frames_ori_list.append(frame)
                        # print(ego_id)
                        # print("frame: " + str(frame))
                cnt += 1
        elif master_y > 860:
            continue

    # print(ego_ids_ori_list)
    # print(ego_frames_ori_list)

    ego_ids_list = []
    ego_frames_list = []
    cnt = 0

    #   对于每一id选取第一个帧数据
    for i in ego_ids_ori_list:
        if i not in ego_ids_list:
            ego_ids_list.append(int(i))
            ego_frames_list.append(int(ego_frames_ori_list[cnt]))
        cnt += 1

    #   删去汇流成功（桢id最大）的数据
    if ego_ids_list:
        idx_max = ego_frames_list.index(max(ego_frames_list))
        del ego_frames_list[idx_max]
        del ego_ids_list[idx_max]

    #   创建对应长度主车id的数列
    if ego_ids_list:
        master_id_list = [int(master_id)] * len(ego_ids_list)
        Col_masterID.extend(master_id_list)
        Col_egoID.extend(ego_ids_list)
        Col_frame.extend(ego_frames_list)
        print("master: " + str(master_id_list))
        print("ego_ids_list :" + str(ego_ids_list))
        print("ego_frames_list: " + str(ego_frames_list))

Col_masterID_array = np.array(Col_masterID)
Col_egoID_array = np.array(Col_egoID)
Col_frame_array = np.array(Col_frame)
print(Col_masterID_array)
print(Col_egoID_array)
print(Col_frame_array)
output = np.empty((Col_masterID_array.size, 3))
print(output.shape)
for i in range(Col_masterID_array.size):
    output[i][0] = Col_masterID_array[i]
    output[i][1] = Col_egoID_array[i]
    output[i][2] = Col_frame_array[i]

print(output)
#
# np.savetxt('../NGSIM_i80_1stTimePeriod_NonMerge.csv', output, delimiter=',')
