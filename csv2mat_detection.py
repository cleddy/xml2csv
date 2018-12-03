# -*- coding: UTF-8 -*-

import scipy.io
import os
from operator import itemgetter
import sys
import numpy as np
import pandas as pd
import re

folder_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/"
foldername = ("20181118", "20181118")
filename = ("detection_all_20181118.csv", "reID_all_20181118.csv")

tabel = []
tabel_sorted = []

current_path = folder_path + foldername[0] + "/" + filename[0]
# UTF-8编码格式csv文件数据读取
file = pd.read_csv(current_path)  # 返回一个DataFrame的对象，这个是pandas的一个数据结构
file.columns = ["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]
file_value = file[["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]]  # 抽取前七列作为训练数据的各属性值
file_value = np.array(file)
print(file_value)

for i in range(len(file_value)):
    col = []
    if file_value[i][0] == 'person':
        col.append(0)
    if file_value[i][0] == 'bicycle':
        col.append(1)
    if file_value[i][0] == 'motorbike':
        col.append(2)
    if file_value[i][0] == 'car':
        col.append(3)
    if file_value[i][0] == 'van':
        col.append(4)
    if file_value[i][0] == 'truck':
        col.append(5)
    name,num = re.findall(r'[0-9]+|[a-z]+', file_value[i][1])
    col.append(int(num))
    for j in range(2, 7):
        col.append(file_value[i][j])
    tabel.append(col)
tabel_sorted = sorted(tabel, key=itemgetter(0,1))

scipy.io.savemat('detection.mat',{'detection':tabel_sorted})