# -*- coding: utf-8 -*-

import cv2
from xml.dom.minidom import parse
import xml.dom.minidom
import os

imgpath = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/images/"
xmlpath = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/results/20181022/yangling_44/"
outpath = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/images/fivecams/20181022/yangling/"

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
        imgdir = imgpath + camID + '/' + os.path.splitext(name)[0] + '.jpg'
        print (imgdir)
        img = cv2.imread(imgdir)
        frame = annotation.getElementsByTagName('filename')[0]
        # 打印每个行人的详细信息
        for object in objects:
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
            img1 = cv2.putText(img, objectname, (int(xmin.childNodes[0].data),int(ymin.childNodes[0].data)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.rectangle(img1, (int(xmin.childNodes[0].data),int(ymin.childNodes[0].data)), (int(xmax.childNodes[0].data),int(ymax.childNodes[0].data)), (0, 255, 0), 1)
        cv2.imwrite(outpath + os.path.splitext(name)[0] + '.jpg', img1)
        #cv2.imshow("Image", img1)
        #cv2.waitKey(0)

