# -*- coding: cp936 -*-

import os
from operator import itemgetter
import sys
import numpy as np
import pandas as pd
import re

folder_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/"
foldername = ("20181118","20181126", "20181126")
filename = ("reID_all_20181118.csv","reID_five_1_washed.csv", "reID_five_2_washed.csv")

# ��csv�ļ���д����
fileHandle = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181126/reID_all.csv', 'w' )
fileHandle.write("Object,VideoName,FrameNum,X,Y,Width,Height\n")

bicycle_num = 0
car_num = 0
motorbike_num = 0
person_num = 0
truck_num = 0
van_num = 0

tabel = []
tabel_sorted = []

for f in range(0,3):
    current_path = folder_path + foldername[f] + "/" + filename[f]
    print(current_path)
    tmp_bicycle_num = 0
    tmp_car_num = 0
    tmp_motorbike_num = 0
    tmp_person_num = 0
    tmp_truck_num = 0
    tmp_van_num = 0

    # UTF-8�����ʽcsv�ļ����ݶ�ȡ
    file = pd.read_csv(current_path)  # ����һ��DataFrame�Ķ��������pandas��һ�����ݽṹ
    file.columns = ["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]
    file_value = file[["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]]  # ��ȡǰ������Ϊѵ�����ݵĸ�����ֵ
    file_value = np.array(file)

    lastname, lastnum = re.findall(r'[0-9]+|[a-z]+', file_value[0][0]) #���µ�һ����name��num��������һ���Ƚ�
    for i in range(len(file_value)):
        col = []
        name,num = re.findall(r'[0-9]+|[a-z]+', file_value[i][0])
        col.append(name)
        if i == 0:
            locals()["tmp_" + name + "_num"] += 1
            locals()[name + "_num"] += 1
        else:
            if name == lastname:
                if num <> lastnum:
                    locals()["tmp_" + name + "_num"] += 1
                    locals()[name + "_num"] += 1
            else:
                locals()["tmp_" + name + "_num"] += 1
                locals()[name + "_num"] += 1
        col.append(locals()[name + "_num"])
        for j in range(1, 6):
            col.append(file_value[i][j])
        col.append(str(file_value[i][6])+'\n')
        tabel.append(col)
        lastname, lastnum = re.findall(r'[0-9]+|[a-z]+', file_value[i][0])
        #print(file_value[i][0],locals()[name + "_num"])

    print(bicycle_num,car_num,motorbike_num,person_num,truck_num,van_num)

tabel_sorted = sorted(tabel, key=itemgetter(0,1))
for row in tabel_sorted:  # ������ȡ������Ƕ���б�
    row = [str(x) for x in row]  # ת��Ϊ�ַ�����ʽ����д���ı�
    row[0] = row[0]+row[1]
    for i in range(1,7):
        row[i] =row[i+1]
    del row[7]
    fileHandle.write(','.join(row))
fileHandle.close()





