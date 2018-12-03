# -*- coding: cp936 -*-
import os
import zipfile

root_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/images/"

for i in range(3,48):
    startdir = root_path + str(i)
    file_news = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/images/zipimages/" + str(i) + '.zip'  # ѹ�����ļ��е�����
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED,allowZip64=True)  # ����һ���ļ�����
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # ��һ�����Ҫ����replace�Ļ����ʹӸ�Ŀ¼��ʼ����
        fpath = fpath and fpath + os.sep or ''  # ��仰�����Ҳ�����ƣ�ʵ�ֵ�ǰ�ļ����Լ������������ļ���ѹ��
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            print (filename)
        z.close()

