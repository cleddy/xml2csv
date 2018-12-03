
# -*- coding: cp936 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import os
from operator import itemgetter

current_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/results/detection/allvideos/"
print (current_path)

# 打开csv文件并写内容
fileHandle = open ('E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/detection0.csv', 'w' )
fileHandle.write("Object,FrameNum,VideoName,X,Y,Width,Height\n")
table = []
for name in os.listdir(current_path):
    if os.path.splitext(name)[1] == ".xml":
        print (name)
        xmldir = current_path + name
        # 使用minidom解析器打开 XML 文档
        DOMTree = xml.dom.minidom.parse(xmldir)
        annotation = DOMTree.documentElement

        # 在集合中获取行人
        objects = annotation.getElementsByTagName("object")
        cam = annotation.getElementsByTagName('folder')[0]
        frame = annotation.getElementsByTagName('filename')[0]
        # 打印每个行人的详细信息
        for object in objects:
            col = []
            print "*****Object*****"
            name = object.getElementsByTagName('name')[0]
            objectname = name.childNodes[0].data
            print "Name: %s" % name.childNodes[0].data
            if objectname == 'bike':
                objectname = 'bicycle'
            if objectname[1].isdigit()or objectname == 'personw':
                objectname = 'person'
            col.append(objectname)
            print "Cam: %s" % cam.childNodes[0].data
            col.append('cam' + str(cam.childNodes[0].data).zfill(2))
            print "Frame: %s" % frame.childNodes[0].data[-10:-4]
            col.append(frame.childNodes[0].data[-10:-4])
            xmin = object.getElementsByTagName('xmin')[0]
            print "Xmin: %s" % xmin.childNodes[0].data
            col.append(xmin.childNodes[0].data)
            ymin = object.getElementsByTagName('ymin')[0]
            print "Ymin: %s" % ymin.childNodes[0].data
            col.append(ymin.childNodes[0].data)
            xmax = object.getElementsByTagName('xmax')[0]
            print "Xmax: %s" % xmax .childNodes[0].data
            ymax = object.getElementsByTagName('ymax')[0]
            print "Ymax: %s" % ymax.childNodes[0].data
            width = abs(int(xmax.childNodes[0].data)-int(xmin.childNodes[0].data))
            col.append(str(width))
            height = abs(int(ymax.childNodes[0].data)-int(ymin.childNodes[0].data))
            col.append(str(height)+'\n')
            table.append(col)
            #print(col)
table_sorted = sorted(table, key=itemgetter(0))
for row in table_sorted:  # 遍历读取排序后的嵌套列表
    fileHandle.write(','.join(row))
fileHandle.close()