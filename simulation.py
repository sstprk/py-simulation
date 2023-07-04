import matplotlib.pyplot as plt 
import argparse
import os
from load_mvnx import load_mvnx

data = load_mvnx(r"C:\Users\stcr3\Desktop\Data\baran_jumping1.1-001.mvnx")
frame_rate = data.frame_count
segment_name = []
segment_pos = []
i = 0
for i in range(22):
    segment_name.append(data.segment_name_from_index(i))
    segment_pos.append(data.get_segment_pos(i))
joint_angle = []
joint_angle_xzy = []
j = 0
for j in range(21):
    joint_angle.append(data.get_joint_angle(j))
    joint_angle_xzy.append(data.get_joint_angle_xzy(j))
print(frame_rate)
