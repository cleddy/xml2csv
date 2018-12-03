#! /usr/bin/env python
# coding=utf-8
import os
import shutil
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def copy_and_rename(fpath_input, fpath_output):
    for i in range(1,48):
        newname = os.path.join(fpath_output,'videotoimage' + str(i) + ".py")
        print(newname)
        shutil.copyfile(fpath_input, newname)


if __name__ == '__main__':
    print('start ...')
    t1 = time.time() * 1000
    #time.sleep(1) #1s
    fpath_input = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/videotoimage.py"
    fpath_output = "E:/dataset/NJUST-MainRoad/Record/NJUST-MainRoad/code/"
    copy_and_rename(fpath_input, fpath_output)
    t2 = time.time() * 1000
    print('take time:' + str(t2 - t1) + 'ms')
    print('end.')