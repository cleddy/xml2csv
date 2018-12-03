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

# ��csv�ļ���д����
fileHandle = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181118/detection_all_20181118.csv', 'w' )
fileHandle.write("Object,VideoName,FrameNum,X,Y,Width,Height\n")

for f in range(0,2):
    current_path = folder_path + foldername[f] + "/" + filename[f]
    # UTF-8�����ʽcsv�ļ����ݶ�ȡ
    file = pd.read_csv(current_path)  # ����һ��DataFrame�Ķ��������pandas��һ�����ݽṹ
    file.columns = ["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]
    file_value = file[["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]]  # ��ȡǰ������Ϊѵ�����ݵĸ�����ֵ
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
for row in tabel_sorted:  # ������ȡ������Ƕ���б�
    row = [str(x) for x in row]  # ת��Ϊ�ַ�����ʽ����д���ı�
    row[1] = row[1]+row[2]
    for i in range(2,7):
        row[i] =row[i+1]
    del row[7]
    fileHandle.write(','.join(row))
fileHandle.close()