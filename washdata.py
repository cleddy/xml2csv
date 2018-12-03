# -*- coding: cp936 -*-

import os
from operator import itemgetter
import sys
import numpy as np
import pandas as pd
import re

folder_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/"
foldername = ("20181126", "20181126")
filename = ("reID_five_1.csv", "reID_five_2.csv")

# ��csv�ļ���д����
fileHandle0 = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181126/reID_five_1_washed.csv', 'w' )
fileHandle0.write("Object,VideoName,FrameNum,X,Y,Width,Height\n")
fileHandle1 = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181126/reID_five_2_washed.csv', 'w' )
fileHandle1.write("Object,VideoName,FrameNum,X,Y,Width,Height\n")

tabel0 = []
tabel1 = []
tabel_sorted0 = []
tabel_sorted1 = []
for f in range(0,2):
    current_path = folder_path + foldername[f] + "/" + filename[f]
    # UTF-8�����ʽcsv�ļ����ݶ�ȡ
    file = pd.read_csv(current_path)  # ����һ��DataFrame�Ķ��������pandas��һ�����ݽṹ
    file.columns = ["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]
    file_value = file[["Object", "VideoName", "FrameNum", "X", "Y", "Width", "Height"]]  # ��ȡǰ������Ϊѵ�����ݵĸ�����ֵ
    file_value = np.array(file)

    for i in range(len(file_value)):
        col = []
        name,num = re.findall(r'[0-9]+|[a-z]+', file_value[i][0])
        if name == "cara":
            name = "car20"
        num = int(num)
        col.append(name)
        col.append(num)
        for j in range(1, 6):
            col.append(file_value[i][j])
        col.append(str(file_value[i][6])+'\n')
        locals()["tabel" + str(f)].append(col)
    print(locals()["tabel" + str(f)])
    locals()["tabel_sorted" + str(f)] = sorted(locals()["tabel" + str(f)], key=itemgetter(0, 1))
    for row in locals()["tabel_sorted" + str(f)]:  # ������ȡ������Ƕ���б�
        row = [str(x) for x in row]  # ת��Ϊ�ַ�����ʽ����д���ı�
        row[0] = row[0] + row[1]
        for i in range(1, 7):
            row[i] = row[i + 1]
        del row[7]
        print(row)
        locals()["fileHandle" + str(f)].write(','.join(row))
    locals()["fileHandle" + str(f)].close()