# -*- coding: cp936 -*-

import os
from operator import itemgetter
import sys
import numpy as np
import pandas as pd
import re

folder_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/"
foldername = ("20181111", "20181118")
filename = ("detection_all.csv", "detection_five .csv")

tabel = []
tabel_sorted = []

# 打开csv文件并写内容
fileHandle = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181118/detection_all_20181118.csv', 'w' )
fileHandle.write("Object,VideoName,FrameNum,X,Y,Width,Height\n")

for f in range(0,2):
    current_path = folder_path + foldername[f] + "/" + filename[f]
    # UTF-8编码格式csv文件数据读取
    file = pd.read_csv(current_path)  # 返回一个DataFrame的对象，这个是pandas的一个数据结构
    file.columns = ["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]
    file_value = file[["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]]  # 抽取前七列作为训练数据的各属性值
    file_value = np.array(file)

    for i in range(len(file_value)):
        col = []
        col.append(file_value[i][0])
        name,num = re.findall(r'[0-9]+|[a-z]+', file_value[i][1])
        col.append(name)
        col.append(int(num))
        for j in range(2, 6):
            col.append(file_value[i][j])
        col.append(str(file_value[i][6])+'\n')
        tabel.append(col)

tabel_sorted = sorted(tabel, key=itemgetter(0,2))
for row in tabel_sorted:  # 遍历读取排序后的嵌套列表
    row = [str(x) for x in row]  # 转换为字符串格式，好写入文本
    row[1] = row[1]+row[2]
    for i in range(2,7):
        row[i] =row[i+1]
    del row[7]
    fileHandle.write(','.join(row))
fileHandle.close()