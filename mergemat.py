# -*- coding: UTF-8 -*-
import scipy.io

detection = scipy.io.loadmat('detection.mat');
detection = detection['detection']

reID = scipy.io.loadmat('reID.mat');
reID = reID['reID']
scipy.io.savemat('results_final.mat',{'detection':detection,'reID':reID},)