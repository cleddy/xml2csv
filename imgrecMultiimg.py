# -*- coding: utf-8 -*-

import cv2
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import re

imgpath = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181022/examples-origin/"
xmlpath = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181022/examples-origin/xml/"
outpath = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/final/20181022/examples-colored/"

for name in os.listdir(xmlpath):
    if os.path.splitext(name)[1] == ".xml":
        print (name)
        xmldir = xmlpath + name
        # 使用minidom解析器打开 XML 文档
        DOMTree = xml.dom.minidom.parse(xmldir)
        annotation = DOMTree.documentElement

        # 在集合中获取行人
        objects = annotation.getElementsByTagName("object")
        if objects == []:
            continue
        cam = annotation.getElementsByTagName('folder')[0]
        camID = cam.childNodes[0].data
        if len(camID)>2:
            camID = camID[0:2]
        imgdir = imgpath + os.path.splitext(name)[0] + '.jpg'
        print (imgdir)
        img = cv2.imread(imgdir)
        frame = annotation.getElementsByTagName('filename')[0]
        # 打印每个行人的详细信息
        for object in objects:
            color = (255,255,1)
            print "*****Object*****"
            obname = object.getElementsByTagName('name')[0]
            objectname = obname.childNodes[0].data
            print "Name: %s" % objectname
            print "Cam: %s" % camID
            print "Frame: %s" % frame.childNodes[0].data[-10:-4]
            xmin = object.getElementsByTagName('xmin')[0]
            print "Xmin: %s" % xmin.childNodes[0].data
            ymin = object.getElementsByTagName('ymin')[0]
            print "Ymin: %s" % ymin.childNodes[0].data
            xmax = object.getElementsByTagName('xmax')[0]
            print "Xmax: %s" % xmax .childNodes[0].data
            ymax = object.getElementsByTagName('ymax')[0]
            print "Ymax: %s" % ymax.childNodes[0].data
            originobjectname = objectname
            if originobjectname[-1].isdigit():
                objectname = re.sub(r'[^A-Za-z]', '', originobjectname)
                # ob = re.findall("\d+",objectname)[0]
                # color = (255-int(ob)*50/100,255-int(ob)*50/10,255-int(ob)%100)
            if objectname == "bicycle":
                color = (0,255,0)
            if objectname == "car":
                color = (255,0,0)
            if objectname == "motorbike":
                color = (125,100,0)
            if objectname == "person":
                color = (0,0,255)
            if objectname == "truck":
                color = (0,125,125)
            if objectname == "van":
                color = (125,0,125)



            img1 = cv2.putText(img, originobjectname, (int(xmin.childNodes[0].data),int(ymin.childNodes[0].data)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            cv2.rectangle(img1, (int(xmin.childNodes[0].data),int(ymin.childNodes[0].data)), (int(xmax.childNodes[0].data),int(ymax.childNodes[0].data)), color, 2)
        cv2.imwrite(outpath + os.path.splitext(name)[0] + '.jpg', img1)
        #cv2.imshow("Image", img1)
        #cv2.waitKey(0)

