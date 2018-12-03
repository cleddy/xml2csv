# -*- coding: UTF-8 -*-

import os
from operator import itemgetter
import re

current_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20180728/"
print (current_path)

# 打开csv文件并写内容
fileHandle = open ( current_path +'personReID_five.csv', 'w' )
fileHandle.write("personID,VideoName,FrameNum,X,Y,Width,Height\n")
labelnum = 0
for name in os.listdir(current_path):
    #if os.path.splitext(name)[1] == ".csv":
    if name == "reID_five.csv":
        print (name)
        csvfile = current_path + name
        csvHandle = open(csvfile,'r')
        table = []
        IDhead = ""
        for line in csvHandle:
            col = line.split(',')  # 每行分隔为列表，好处理列格式
            if col[0] != "Labeler":
                table.append(col)  # 嵌套列表table[[8,8][*,*],...]

        print (len(table))

        for i in range(0,len(table)):
            if table[i][0] != table[i-1][0]:
                labelnum +=1
            print (table[i][1])
            table[i][1] = (int(re.findall(r'[0-9]+|[a-z]+', table[i][1])[1])) + (10 * (labelnum-1))


        table_sorted = sorted(table, key=itemgetter(0,1))
        for row in table_sorted:  # 遍历读取排序后的嵌套列表
            row = [str(x) for x in row]  # 转换为字符串格式，好写入文本
            row[0] = row[1]
            for i in range(1,7):
                row[i] =row[i+1]
            del row[7]
            print(row)
            fileHandle.write(','.join(row))
        csvHandle.close()

fileHandle.close()
