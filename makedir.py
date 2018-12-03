# -*- coding: cp936 -*-

'''
import os

for i in range(1,48):
    os.makedirs("E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/images/" + str(i) + '/')
'''
import time
time_start=time.time()
time.sleep(5)
time_elapsed = time.time() - time_start
print('The code run {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))