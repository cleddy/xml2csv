# -*- coding: UTF-8 -*-

import os
from operator import itemgetter
import re

current_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/"
print (current_path)

# 打开csv文件并写内容
fileHandle = open ( current_path +'final/personReIDCSJ.csv', 'w' )
fileHandle.write("personID,FrameNum,VideoName,X,Y,Width,Height\n")

for name in os.listdir(current_path):
    #if os.path.splitext(name)[1] == ".csv":
    if name == "personReIDCSJ.csv":
        print (name)
        csvfile = current_path + name
        csvHandle = open(csvfile,'r')
        table = []
        IDhead = ""
        for line in csvHandle:
            col = line.split(',')  # 每行分隔为列表，好处理列格式
            IDhead = col[0][0]
            colwithnum = []
            #col[0] = int(col[0][1:])
            colwithnum.append(re.findall(r'[0-9]+|[a-z]+', col[0])[0])
            colwithnum.append(int(re.findall(r'[0-9]+|[a-z]+', col[0])[1]))
            for i in range(1,7):
                colwithnum.append(col[i])
            table.append(colwithnum)  # 嵌套列表table[[8,8][*,*],...]

        table_sorted = sorted(table, key=itemgetter(0,1))
        for row in table_sorted:  # 遍历读取排序后的嵌套列表
            row = [str(x) for x in row]  # 转换为字符串格式，好写入文本
            row[0] = row[0]+row[1]
            for i in range(1,7):
                row[i] =row[i+1]
            del row[7]
            print(row)
            fileHandle.write(','.join(row))
        csvHandle.close()

fileHandle.close()
