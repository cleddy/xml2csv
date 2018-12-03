
# -*- coding: cp936 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import os
from operator import itemgetter
import sys

folder_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/results/20181118/"
folername = ("chenshijia","yangling","zhouyilin")
print (folder_path)

# 打开csv文件并写内容
fileHandle1 = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181118/detection_five.csv', 'w' )
fileHandle1.write("Object,VideoName,FrameNum,X,Y,Width,Height\n")
fileHandle2 = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181118/reID_five.csv', 'w' )
fileHandle2.write("Labeler,Object,VideoName,FrameNum,X,Y,Width,Height\n")
table1 = []
table2 = []
for f in range(0,3):
    current_path = folder_path + folername[f] + "/"
    print (current_path)
    for name in os.listdir(current_path):
        if os.path.splitext(name)[1] == ".xml":
            print (name)
            xmldir = current_path + name
            # 使用minidom解析器打开 XML 文档
            DOMTree = xml.dom.minidom.parse(xmldir)
            annotation = DOMTree.documentElement

            # 在集合中获取行人
            objects = annotation.getElementsByTagName("object")
            cam = annotation.getElementsByTagName('filename')[0]
            frame = annotation.getElementsByTagName('filename')[0]
            # 打印每个行人的详细信息
            for object in objects:
                col1 = []
                col2 = []
                print "*****Object*****"
                name = object.getElementsByTagName('name')[0]
                objectname = name.childNodes[0].data
                print "Name: %s" % name.childNodes[0].data
                if objectname == 'bike':
                    objectname = 'bicycle'
                if objectname == 'w':
                    objectname = 'car'
                if objectname[1].isdigit()or objectname == 'personw':
                    col1.append('person')
                else:
                    col1.append(objectname)
                print "Cam: %s" % cam.childNodes[0].data[3:5]
                col1.append('cam' + str(cam.childNodes[0].data)[3:5])
                print "Frame: %s" % frame.childNodes[0].data[-10:-4]
                col1.append(frame.childNodes[0].data[-10:-4])
                xmin = object.getElementsByTagName('xmin')[0]
                print "Xmin: %s" % xmin.childNodes[0].data
                col1.append(xmin.childNodes[0].data)
                ymin = object.getElementsByTagName('ymin')[0]
                print "Ymin: %s" % ymin.childNodes[0].data
                col1.append(ymin.childNodes[0].data)
                xmax = object.getElementsByTagName('xmax')[0]
                print "Xmax: %s" % xmax .childNodes[0].data
                ymax = object.getElementsByTagName('ymax')[0]
                print "Ymax: %s" % ymax.childNodes[0].data
                width = abs(int(xmax.childNodes[0].data)-int(xmin.childNodes[0].data))
                col1.append(str(width))
                height = abs(int(ymax.childNodes[0].data)-int(ymin.childNodes[0].data))
                col1.append(str(height) + '\n')
                table1.append(col1)
                if objectname[1].isdigit():
                    col2.append(folername[f])
                    col2.append(objectname)
                    col2.append('cam' + str(cam.childNodes[0].data)[3:5])
                    col2.append(frame.childNodes[0].data[-10:-4])
                    col2.append(xmin.childNodes[0].data)
                    col2.append(ymin.childNodes[0].data)
                    col2.append(str(width))
                    col2.append(str(height) + '\n')
                    table2.append(col2)
                #print(col)
table_sorted1 = sorted(table1, key=itemgetter(0))
for row in table_sorted1:  # 遍历读取排序后的嵌套列表
    fileHandle1.write(','.join(row))
fileHandle1.close()

table_sorted2 = sorted(table2, key=itemgetter(0))
for row in table_sorted2:  # 遍历读取排序后的嵌套列表
    fileHandle2.write(','.join(row))
fileHandle2.close()