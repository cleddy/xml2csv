# -*- coding: cp936 -*-
import cv2
import os
import time

input_path1_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/1һ���� 10.8.0.2/2018_1_19_11_00_01--2018_1_19_13_00_01.mp4"
input_path1_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/1һ���� 10.8.0.2/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path2_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/2�����Ŷ��������·������ 10.0.0.34/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path2_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/2�����Ŷ��������·������ 10.0.0.34/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path3_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/3�����Ŷ������·����10.0.0.39/2018_1_19_11_00_00--1601_1_1_08_00_00.mp4"
input_path3_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/3�����Ŷ������·����10.0.0.39/2018_1_19_11_06_14--1601_1_1_08_00_00.mp4"
input_path3_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/3�����Ŷ������·����10.0.0.39/2018_1_19_11_54_29--2018_1_19_13_54_29.mp4"
input_path3_4 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/3�����Ŷ������·����10.0.0.39/2018_1_19_13_54_33--2018_1_19_14_00_00.mp4"
input_path4_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/4������·�ڿ���-10.0.0.38/2018_1_19_11_00_05--2018_1_19_13_00_05.mp4"
input_path4_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/4������·�ڿ���-10.0.0.38/2018_1_19_13_00_06--2018_1_19_13_00_05.mp4"
input_path4_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/4������·�ڿ���-10.0.0.38/2018_1_19_13_03_08--2018_1_19_14_00_00.mp4"
input_path5_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/5����·���������10.0.0.21/2018_1_19_11_00_00--1601_1_1_08_00_00.mp4"
input_path5_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/5����·���������10.0.0.21/2018_1_19_12_11_38--1601_1_1_08_00_00.mp4"
input_path5_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/5����·���������10.0.0.21/2018_1_19_13_23_17--2018_1_19_14_00_00.mp4"
input_path6_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/6����·ת�̱����� 10.9.0.6/2018_1_19_11_00_00--1601_1_1_08_00_00.mp4"
input_path6_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/6����·ת�̱����� 10.9.0.6/2018_1_19_11_01_52--2018_1_19_13_01_52.mp4"
input_path6_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/6����·ת�̱����� 10.9.0.6/2018_1_19_13_01_54--2018_1_19_14_00_00.mp4"
input_path7_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/7����·ת�̶�����10.9.0.17/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path7_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/7����·ת�̶�����10.9.0.17/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path8_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/8����·ת�̶����� 10.9.0.3/2018_1_19_11_00_01--2018_1_19_13_00_01.mp4"
input_path8_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/8����·ת�̶����� 10.9.0.3/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path9_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/9����·ת�������10.0.0.170/2018_1_19_11_00_08--1601_1_1_08_00_00.mp4"
input_path9_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/9����·ת�������10.0.0.170/2018_1_19_11_55_36--1601_1_1_08_00_00.mp4"
input_path9_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/9����·ת�������10.0.0.170/2018_1_19_13_06_16--2018_1_19_14_00_00.mp4"
input_path10_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/10����·ת��������10.0.0.25/2018_1_19_11_00_02--2018_1_19_13_00_02.mp4"
input_path10_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/10����·ת��������10.0.0.25/2018_1_19_13_00_04--2018_1_19_14_00_00.mp4"
input_path11_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/11����·ת��������10.0.0.24/2018_1_19_11_00_05--2018_1_19_13_00_05.mp4"
input_path11_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/11����·ת��������10.0.0.24/2018_1_19_13_00_04--2018_1_19_14_00_00.mp4"
input_path12_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/12����·ת�������� 10.0.0.77/2018_1_19_11_00_04--2018_1_19_13_00_04.mp4"
input_path12_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/12����·ת�������� 10.0.0.77/2018_1_19_13_00_07--2018_1_19_14_00_00.mp4"
input_path13_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/13�����Ž�����-10.9.0.2/2018_1_19_11_00_00--1601_1_1_08_00_00.mp4"
input_path13_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/13�����Ž�����-10.9.0.2/2018_1_19_12_11_49--2018_1_19_12_54_18.mp4"
input_path13_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/13�����Ž�����-10.9.0.2/2018_1_19_12_54_31--2018_1_19_14_00_00.mp4"
input_path14_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/14������������-10.9.0.8/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path14_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/14������������-10.9.0.8/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path15_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/15�ߺ��Ž���-10.0.0.26/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path15_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/15�ߺ��Ž���-10.0.0.26/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path16_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/16����·����·�ڿ���-10.5.0.17/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path16_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/16����·����·�ڿ���-10.5.0.17/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path17_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/17����·��Сͣ������ 10.3.0.6/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path17_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/17����·��Сͣ������ 10.3.0.6/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path18_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/18����·����������10.5.0.170/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path18_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/18����·����������10.5.0.170/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path19_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/19����·���������� _10.5.0.20/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path19_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/19����·���������� _10.5.0.20/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path20_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/20����·��԰С��ǰ·�� 10.3.0.13/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path20_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/20����·��԰С��ǰ·�� 10.3.0.13/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path21_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/21����·��԰С��ǰ·������ 10.3.0.14/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path21_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/21����·��԰С��ǰ·������ 10.3.0.14/2018_1_19_13_00_01--2018_1_19_14_00_01.mp4"
input_path22_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/22������-10.3.0.23/2018_1_19_11_00_00--1601_1_1_08_00_00.mp4"
input_path23_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/23������������ 10.3.0.12/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path23_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/23������������ 10.3.0.12/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path24_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/24������������ 10.4.0.3/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path24_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/24������������ 10.4.0.3/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path25_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/25�ĺ���10.5.0.2/2018_1_23_15_43_09--1601_1_1_08_00_00.mp4"
input_path26_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/26�ĺ��ſ�ˮ�������� 10.5.0.10/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path26_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/26�ĺ��ſ�ˮ�������� 10.5.0.10/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path27_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/27�ĺ���������10.5.0.8/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path27_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/27�ĺ���������10.5.0.8/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path28_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/28�ĺ���һ��ͨ 10.5.0.6/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path28_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/28�ĺ���һ��ͨ 10.5.0.6/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path29_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/29�ĺ���һ��ͨ��·�� 10.5.0.13/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path29_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/29�ĺ���һ��ͨ��·�� 10.5.0.13/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path30_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/30ͼ��ݺ��濴�� 10.4.0.15/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path30_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/30ͼ��ݺ��濴�� 10.4.0.15/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path31_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/31ͼ������� 10.4.0.13/2018_1_19_11_30_00--2018_1_19_13_30_00.mp4"
input_path31_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/31ͼ������� 10.4.0.13/2018_1_19_13_30_01--2018_1_19_14_00_00.mp4"
input_path32_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/32ͼ�����ʮ��·������ 10.4.0.12/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path33_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/33ͼ�����ʮ��·������ 10.4.0.14/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path33_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/33ͼ�����ʮ��·������ 10.4.0.14/2018_1_19_13_00_02--2018_1_19_14_00_00.mp4"
input_path34_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/34������� 10.7.0.23/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path34_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/34������� 10.7.0.23/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path35_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/35����������� 10.7.0.22/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path35_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/35����������� 10.7.0.22/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path36_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/36һ��·����ѧԺ���� 10.7.0.10/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path37_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/37һ��··��ͣ��������10.8.0.11/2018_1_19_07_30_00--2018_1_19_08_28_23.mp4"
input_path38_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/38һ��·����ѧԺ·�ڿ��� 10.7.0.13/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path38_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/38һ��·����ѧԺ·�ڿ��� 10.7.0.13/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path39_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/39һ��·һС���ſڿ���  10.8.0.8/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path39_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/39һ��·һС���ſڿ���  10.8.0.8/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path40_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/40һ��·һС���ſڿ���  10.8.0.7/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path40_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/40һ��·һС���ſڿ���  10.8.0.7/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path41_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/41�����·�ϲ��񴦿���  10.0.0.37/2018_1_19_11_00_05--2018_1_19_11_10_30.mp4"
input_path42_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/42�����·�ϲ��񴦿���-10.0.0.36/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path42_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/42�����·�ϲ��񴦿���-10.0.0.36/2018_1_19_13_00_01--2018_1_19_14_00_00.mp4"
input_path43_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/43�����·ѧ������·�ڿ��� 10.0.0.35/2018_1_19_11_00_01--1601_1_1_08_00_00.mp4"
input_path43_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/43�����·ѧ������·�ڿ��� 10.0.0.35/2018_1_19_12_31_33--2018_1_19_14_00_00.mp4"
input_path44_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/44�����·�������� 10.0.0.30/2018_1_19_11_00_04--1601_1_1_08_00_00.mp4"
input_path44_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/44�����·�������� 10.0.0.30/2018_1_19_11_06_40--2018_1_19_13_06_40.mp4"
input_path45_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/45�����·�������� 10.0.0.29/2018_1_19_11_00_05--2018_1_19_13_00_05.mp4"
input_path45_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/45�����·�������� 10.0.0.29/2018_1_19_13_00_07--2018_1_19_14_00_00.mp4"
input_path46_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/46�������¥·�ڿ��� 10.7.0.17/2018_1_19_11_00_00--2018_1_19_13_00_00.mp4"
input_path46_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/46�������¥·�ڿ��� 10.7.0.17/2018_1_19_13_00_00--2018_1_19_14_00_00.mp4"
input_path47_1 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/47���������¥·�ڿ���-10.7.0.15/2018_1_19_11_00_00--1601_1_1_08_00_00.mp4"
input_path47_2 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/47���������¥·�ڿ���-10.7.0.15/2018_1_19_12_12_39--1601_1_1_08_00_00.mp4"
input_path47_3 = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/47���������¥·�ڿ���-10.7.0.15/2018_1_19_13_25_35--2018_1_19_14_00_00.mp4"

camNums = (2,2,4,3,3,3,2,2,3,2,2,2,3,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,2,1,1,2,2,2,1,2,2,2,2,2,3)

time_start=time.time()

for i in xrange(1,48):
    output_path = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/images/"+ str(i) + "/"
    camID = output_path.split('/')[-2].zfill(2)

    # if output_path doesn't exist, create it
    file_dir = os.path.split(output_path)[0]
    if not os.path.isdir(file_dir):
        print("dir doesn't exist")
        os.makedirs(file_dir)

    start_frame = 0 #every new cam strats from 0
    for j in range(1, camNums[i-1]+1):
        input_path = locals()["input_path" + str(i) + "_" + str(j)]
        print(input_path)

        vc = cv2.VideoCapture(input_path)  # read video

        if vc.isOpened():  # if video can be opened
            rval, frame = vc.read()
            print ("success")
        else:
            print ("failed")
            rval = False
        timeF = 30  # frame count gap
        while rval:  # read video until video is over
            rval, frame = vc.read()
            if (start_frame % timeF == 0):  #  save image for every timeF frame
                print (start_frame)
                cv2.imwrite(output_path + 'cam' + camID + '_' + str(start_frame).zfill(6) + '.jpg', frame)  # save as images
            start_frame = start_frame + 1
            cv2.waitKey(1)
        vc.release()

time_elapsed = time.time() - time_start
print('The code run {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))


