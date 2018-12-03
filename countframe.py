
# -*- coding: cp936 -*-

import os
from operator import itemgetter
import sys

folder_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/results/20180719/"
folername = ("chenshijia","cuiyanchao","cuireID","yangling","yinghaihan","zhouyilin")
print (folder_path)

table = []
for f in range(0,6):
    current_path = folder_path + folername[f] + "/"
    print (current_path)
    for name in os.listdir(current_path):
        if os.path.splitext(name)[1] == ".xml":
            print (name)
            table.append(name)
print (len(table))
table_sorted = sorted(set(table), key=table.index)
print (len(table_sorted))
