import matplotlib
import matplotlib.pyplot as plt 
from load_mvnx import load_mvnx
import matplotlib.animation as animation
import numpy as np

data = load_mvnx(r"C:\Users\stcr3\Desktop\Data\baran_walking-001.mvnx")
frame_count = data.frame_count
frame_rate = data.frame_rate
segment_name = []
segment_pos = []
i = 0
for i in range(23):
    segment_name.append(data.segment_name_from_index(i))
    segment_pos.append(data.get_segment_pos(i))
joint_angle = []
joint_angle_xzy = []
j = 0
for j in range(22):
    joint_angle.append(data.get_joint_angle(j))
    joint_angle_xzy.append(data.get_joint_angle_xzy(j))
    
body_parts_x = []
body_parts_y = []
body_parts_z = []

body_x = []
body_y = []
body_z = []

figr_x = []

a=0
k=0
for a in range(6151):
    for k in range(23):
        body_parts_x.append(segment_pos[k][a][0])
        body_parts_y.append(segment_pos[k][a][1])
        body_parts_z.append(segment_pos[k][a][2])

    body_x.append([body_parts_x[14], body_parts_x[13], body_parts_x[12], body_parts_x[11], body_parts_x[5], body_parts_x[6], body_parts_x[5], body_parts_x[7], body_parts_x[8], body_parts_x[9], body_parts_x[10], body_parts_x[9], body_parts_x[8], body_parts_x[7], body_parts_x[4], body_parts_x[11], body_parts_x[4], body_parts_x[3], body_parts_x[2], body_parts_x[1], body_parts_x[0], body_parts_x[15], body_parts_x[16], body_parts_x[17], body_parts_x[18], body_parts_x[17], body_parts_x[16], body_parts_x[15], body_parts_x[0], body_parts_x[19], body_parts_x[20], body_parts_x[21], body_parts_x[22]])

    body_y.append([body_parts_y[14], body_parts_y[13], body_parts_y[12], body_parts_y[11], body_parts_y[5], body_parts_y[6], body_parts_y[5], body_parts_y[7], body_parts_y[8], body_parts_y[9], body_parts_y[10], body_parts_y[9], body_parts_y[8], body_parts_y[7], body_parts_y[4], body_parts_y[11], body_parts_y[4], body_parts_y[3], body_parts_y[2], body_parts_y[1], body_parts_y[0], body_parts_y[15], body_parts_y[16], body_parts_y[17], body_parts_y[18], body_parts_y[17], body_parts_y[16], body_parts_y[15], body_parts_y[0], body_parts_y[19], body_parts_y[20], body_parts_y[21], body_parts_y[22]])

    body_z.append([body_parts_z[14], body_parts_z[13], body_parts_z[12], body_parts_z[11], body_parts_z[5], body_parts_z[6], body_parts_z[5], body_parts_z[7], body_parts_z[8], body_parts_z[9], body_parts_z[10], body_parts_z[9], body_parts_z[8], body_parts_z[7], body_parts_z[4], body_parts_z[11], body_parts_z[4], body_parts_z[3], body_parts_z[2], body_parts_z[1], body_parts_z[0], body_parts_z[15], body_parts_z[16], body_parts_z[17], body_parts_z[18], body_parts_z[17], body_parts_z[16], body_parts_z[15], body_parts_z[0], body_parts_z[19], body_parts_z[20], body_parts_z[21], body_parts_z[22]])

    figr_x.append([body_x[a], body_y[a], body_z[a]])
plt.axes(projection="3d")
plt.plot(figr_x[1000][0], figr_x[1000][1], figr_x[1000][2])
plt.show()