import numpy as np
import matplotlib.pyplot as plt


#  输入（车号， 数据集） 提取对应车号的桢数据， x坐标， y坐标， 速度， 加速度
def data_extraction_vehicle(vehicle_id, data):
    idx = (data[:, 0] == vehicle_id)
    frame = data[idx, 1]
    local_x = data[idx, 4]
    local_y = data[idx, 5]
    v_vel = data[idx, 11]
    v_acc = data[idx, 12]
    precedings = data[idx, 14]
    followings = data[idx, 15]
    return frame, local_x, local_y, v_vel, v_acc, precedings, followings


def data_extraction_vehicle_common(vehicle_id, frame, data):
    frames, x_coordinates, y_coordinates, velocities, accelerations = data_extraction_vehicle(vehicle_id, data)[:5]
    idx_frame = np.argwhere(frames == frame)
    x_coordinate = x_coordinates[int(idx_frame[0])]
    y_coordinate = y_coordinates[int(idx_frame[0])]
    velocity = velocities[int(idx_frame[0])]
    acceleration = accelerations[int(idx_frame[0])]
    # print("x_coordinate: " + str(x_coordinate))
    # print("y_coordinate: " + str(y_coordinate))
    # print("velocity: " + str(velocity))
    # print("acceleration: " + str(acceleration))
    return x_coordinate, y_coordinate, velocity, acceleration


def data_extraction_vehicle_master(vehicle_id, frame, data):
    frames, x_coordinates, y_coordinates, velocities, accelerations = data_extraction_vehicle(vehicle_id, data)[:5]
    idx_frame = np.argwhere(frames == frame)
    x_coordinate = x_coordinates[int(idx_frame[0])]
    y_coordinate = y_coordinates[int(idx_frame[0])]
    gap2end = 859 - y_coordinate

    velocity = 0
    for i in range(-2, 3):
        velocity += velocities[int(idx_frame[0] + i)] / 5
    acceleration = 0
    for i in range(-2, 3):
        print(i)
        acceleration += accelerations[int(idx_frame[0] + i)] / 5

    print("x_coordinate: " + str(x_coordinate))
    print("y_coordinate: " + str(y_coordinate))
    print("velocity: " + str(velocity))
    print("acceleration: " + str(acceleration))
    print("gap to the end: " + str(gap2end))
    return x_coordinate, y_coordinate, velocity, acceleration, gap2end


def data_extraction_vehicle_ego(vehicle_id, frame, data):
    frames, x_coordinates, y_coordinates, velocities, accelerations, precedings, followings = data_extraction_vehicle(
        vehicle_id, data)
    idx_frame = np.argwhere(frames == frame)
    x_coordinate = x_coordinates[int(idx_frame[0])]
    y_coordinate = y_coordinates[int(idx_frame[0])]

    velocity = 0
    for i in range(-2, 3):
        velocity += velocities[int(idx_frame[0] + i)] / 5
    acceleration = 0
    for i in range(-2, 3):
        acceleration += accelerations[int(idx_frame[0] + i)] / 5

    preceding_id, following_id = find_proceeding_following(precedings, followings, frames, frame)

    if preceding_id != 0:
        precding_y = data_extraction_vehicle_common(preceding_id, frame, data)[1]
        gap_front = precding_y - y_coordinate
    else:
        gap_front = 500

    if following_id != 0:
        following_y = data_extraction_vehicle_common(following_id, frame, data)[1]
        gap_behind = y_coordinate - following_y
    else:
        gap_behind = 500

    if acceleration < 0:
        label_ego = 0  # 减速
    else:
        label_ego = 1  # 加速

    print("x_coordinate: " + str(x_coordinate))
    print("y_coordinate: " + str(y_coordinate))
    print("velocity: " + str(velocity))
    print("acceleration: " + str(acceleration))
    print("preceding_id: " + str(preceding_id))
    print("following_id: " + str(following_id))
    print("gap_front: " + str(gap_front))
    print("gap_behind: " + str(gap_behind))

    return x_coordinate, y_coordinate, velocity, acceleration, gap_front, gap_behind, label_ego


def find_proceeding_following(precedings, followings, frames, frame):
    idx_frame = np.argwhere(frames == frame)
    preceding_id = precedings[int(idx_frame[0])]
    following_id = followings[int(idx_frame[0])]
    return preceding_id, following_id


def calc_gap(vehicle_front, vehicle_behind, frame):
    y_coodinate_front = data_extraction_vehicle(vehicle_front, frame)[1]
    y_coodinate_behind = data_extraction_vehicle(vehicle_behind, frame)[1]


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
