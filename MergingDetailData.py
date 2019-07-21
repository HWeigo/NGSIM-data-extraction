import numpy as np
import matplotlib.pyplot as plt

VehicleID_Merge = np.loadtxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo.csv', delimiter=',', skiprows=1, usecols=0)
VehicleID_Ego = np.loadtxt('../NGSIM_i80_1stTimePeriod_MergeAndEgo.csv', delimiter=',', skiprows=1, usecols=0)
data_lane567 = np.loadtxt('../NGSIM_i80_1stTimePeriod_Lane567_simplification.csv', delimiter=',', skiprows=1,
                          usecols=(range(0, 17)))

print(VehicleID_Merge.size)
print(VehicleID_Ego.size)


#  输入（车号， 数据集） 提取对应车号的桢数据， x坐标， y坐标， 速度， 加速度
def data_extraction_vehicle(vehicle_id, data):
    idx = (data[:, 0] == vehicle_id)
    frame = data[idx, 1]
    local_x = data[idx, 4]
    local_y = data[idx, 5]
    v_vel = data[idx, 11]
    v_acc = data[idx, 12]
    return frame, local_x, local_y, v_vel, v_acc


def data_extraction_vehicle_master(vehicle_id, frame, data):
    frames = data_extraction_vehicle(vehicle_id, data)[0]
    y_coordinates = data_extraction_vehicle(vehicle_id, data)[2]
    velocities = data_extraction_vehicle(vehicle_id, data)[3]
    accelerations = data_extraction_vehicle(vehicle_id, data)[4]
    idx_frame = np.argwhere(frames == frame)
    y_coordinate = y_coordinates[int(idx_frame[0])]
    velocity = velocities[int(idx_frame[0])]
    acceleration = accelerations[int(idx_frame[0])]
    print(y_coordinate)
    print(velocity)
    print(acceleration)


def plot_frame_x(vehicle_id, data):
    v_frame = data_extraction_vehicle(vehicle_id, data)[0]
    v_x = data_extraction_vehicle(vehicle_id, data)[1]
    v_y = data_extraction_vehicle(vehicle_id, data)[2]
    x = np.array(v_frame)
    y = np.array(v_x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Vehicle %s's trajectory" % int(vehicle_id))
    plt.xlabel('v_frame')
    plt.ylabel('v_x')
    plt.ylim(90, 55)
    ax1.scatter(x, y, c='r', alpha=0.7, s=1)
    plt.hlines(60.422, np.min(v_frame), np.max(v_frame))
    plt.hlines(74.421, np.min(v_frame), np.max(v_frame))
    # plt.legend('v_x')
    plt.savefig("../frame_x_fig/v%s.png" % int(vehicle_id))
    plt.close()
    # plt.show()


def calc_vel_acc_x(frames, x):
    dt = 0.1
    frames = frames - np.min(frames)
    vel_x = np.empty(frames.size)
    acc_x = np.empty(frames.size)
    for frame_f in frames[1:-1]:
        frame = int(frame_f)
        vel_x[frame] = (x[frame - 1] - x[frame + 1]) / 2 / dt
        acc_x[frame] = -(x[frame + 1] - x[frame - 1]) / 2 / pow(dt, 2)
    vel_x[0] = vel_x[1]
    vel_x[-1] = vel_x[-2]
    acc_x[0] = acc_x[1]
    acc_x[-1] = acc_x[-2]
    return vel_x, acc_x


def plot_frame_x_v(vehicle_id, data):
    v_frame = data_extraction_vehicle(vehicle_id, data)[0]
    v_x = data_extraction_vehicle(vehicle_id, data)[1]
    x = np.array(v_frame)
    y1 = np.array(v_x)
    y2 = np.array(calc_vel_acc_x(v_frame, v_x)[0])

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Vehicle %s's trajectory" % int(vehicle_id))
    ax1.plot(x, y1, label="x", color='red')
    ax1.set_ylabel('local_x')
    ax1.set_ylim(90, 55)
    ax1.hlines(60.422, np.min(v_frame), np.max(v_frame), linestyles='-.')
    ax1.hlines(74.421, np.min(v_frame), np.max(v_frame), linestyles='-.')
    ax1.legend(loc=1)
    plt.xlabel('v_frame')

    ax2 = ax1.twinx()
    ax2.plot(x, y2, label="v", color='blue')
    # ax2.scatter(x, y2, s=2, alpha=0.6)
    ax2.legend(loc=2)
    ax2.set_ylabel('velocity')

    # plt.savefig("../Fig/x,v_frame/v%s.png" % int(vehicle_id))
    # plt.close()
    plt.show()
    plt.pause(0.1)
    # plt.close()


# for vehicle in VehicleID_Merge:
#     plot_frame_x_v(vehicle, data_lane567)
# plot_frame_x_v(124, data_lane567)
data_extraction_vehicle_master(124, 825, data_lane567)
