import matplotlib
import matplotlib.pyplot as plt 
from load_mvnx import load_mvnx
from mpl_toolkits.mplot3d import Axes3D

#Loading mvnx file
#load_mvnx("file_path")
data = load_mvnx(r"C:\Users\stcr3\Desktop\Data\baran_walking-001.mvnx")

#Reading data from the mvnx file
frame_count = data.frame_count
frame_rate = data.frame_rate
segment_name = []
segment_pos = []

for i in range(23):
    segment_name.append(data.segment_name_from_index(i))
    segment_pos.append(data.get_segment_pos(i))
joint_angle = []
joint_angle_xzy = []

for j in range(22):
    joint_angle.append(data.get_joint_angle(j))
    joint_angle_xzy.append(data.get_joint_angle_xzy(j))

min_x = 0
max_x = 0
    
body_x = []
body_y = []
body_z = []

figr = []

#Organising data
for a in range(frame_count):
    body_parts_x = []
    body_parts_y = []
    body_parts_z = []

    for k in range(23):
        body_parts_x.append(segment_pos[k][a][0])
        body_parts_y.append(segment_pos[k][a][1])
        body_parts_z.append(segment_pos[k][a][2])

    #Drawing the figure in each axis
    body_x.append([body_parts_x[14], body_parts_x[13], body_parts_x[12], body_parts_x[11], body_parts_x[5], body_parts_x[6], body_parts_x[5], body_parts_x[7], body_parts_x[8], body_parts_x[9], body_parts_x[10], body_parts_x[9], body_parts_x[8], body_parts_x[7], body_parts_x[4], body_parts_x[11], body_parts_x[4], body_parts_x[3], body_parts_x[2], body_parts_x[1], body_parts_x[0], body_parts_x[15], body_parts_x[16], body_parts_x[17], body_parts_x[18], body_parts_x[17], body_parts_x[16], body_parts_x[15], body_parts_x[0], body_parts_x[19], body_parts_x[20], body_parts_x[21], body_parts_x[22]])

    body_y.append([body_parts_y[14], body_parts_y[13], body_parts_y[12], body_parts_y[11], body_parts_y[5], body_parts_y[6], body_parts_y[5], body_parts_y[7], body_parts_y[8], body_parts_y[9], body_parts_y[10], body_parts_y[9], body_parts_y[8], body_parts_y[7], body_parts_y[4], body_parts_y[11], body_parts_y[4], body_parts_y[3], body_parts_y[2], body_parts_y[1], body_parts_y[0], body_parts_y[15], body_parts_y[16], body_parts_y[17], body_parts_y[18], body_parts_y[17], body_parts_y[16], body_parts_y[15], body_parts_y[0], body_parts_y[19], body_parts_y[20], body_parts_y[21], body_parts_y[22]])

    body_z.append([body_parts_z[14], body_parts_z[13], body_parts_z[12], body_parts_z[11], body_parts_z[5], body_parts_z[6], body_parts_z[5], body_parts_z[7], body_parts_z[8], body_parts_z[9], body_parts_z[10], body_parts_z[9], body_parts_z[8], body_parts_z[7], body_parts_z[4], body_parts_z[11], body_parts_z[4], body_parts_z[3], body_parts_z[2], body_parts_z[1], body_parts_z[0], body_parts_z[15], body_parts_z[16], body_parts_z[17], body_parts_z[18], body_parts_z[17], body_parts_z[16], body_parts_z[15], body_parts_z[0], body_parts_z[19], body_parts_z[20], body_parts_z[21], body_parts_z[22]])

    #Organised data for plotting
    figr.append([body_x[a], body_y[a], body_z[a]])

#Finding the limits of each axis
t=1
for t in range(frame_count):
    if min(figr[t][0]) >= min(figr[t-1][0]):
        min_x = min(figr[t-1][0])
    else:
        min_x = min(figr[t][0])
    if max(figr[t][0]) <= max(figr[t-1][0]):
        max_x = max(figr[t-1][0])
    else:
        max_x = max(figr[t][0])
    
    if min(figr[t][1]) >= min(figr[t-1][1]):
        min_y = min(figr[t-1][1])
    else:
        min_y = min(figr[t][1])
    if max(figr[t][1]) <= max(figr[t-1][1]):
        max_y = max(figr[t-1][1])
    else:
        max_y = max(figr[t][1])
    
    if min(figr[t][2]) >= min(figr[t-1][2]):
        min_z = min(figr[t-1][2])
    else:
        min_z = min(figr[t][2])
    if min(figr[t][2]) <= min(figr[t-1][2]):
        max_z = max(figr[t-1][2])
    else:
        max_z = max(figr[t][2])

#Ploting the figure
fig = plt.figure()
for l in range(frame_count):
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=10, azim=-120, roll=0)
    ax.set_xlim3d(min_x-2, max_x+1)
    ax.set_ylim3d(min_y-1, max_y+1)
    ax.set_zlim3d(min_z, max_z+1)
    ax.plot(figr[l][0], figr[l][1], figr[l][2], lw=2, color="black", marker="H", ms=2, mfc="red")
    plt.draw()
    plt.pause(0.000003)
    plt.clf()
    if l >= 700:
        break
    
plt.show()
plt.close()