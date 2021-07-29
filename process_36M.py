

path = '/home/faye/Desktop/paper_fg/Human36M/'


TRAIN_SUBJECTS = [1,5,6,7,8]
TEST_SUBJECTS  = [9,11]
joint_idxs = [0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
joint_names = ['Hip','RHip','RKnee','RFoot',
               'LHip','LKnee','LFoot','Spine','Thorax',
               'Neck/Nose','Head','LShoulder','LElbow',
               'LWrist','RShoulder','RElbow','RWrist']


import cdflib
from glob import glob
import os
import pdb

folders = glob(path+"Poses_D3_Positions_*")
action_names = []

data_train = []
label_train = []
data_test = []
label_test = []
for i, folder in enumerate(folders):
    action_names.append(os.path.split(folder)[-1][19:])
    
    for subject in TRAIN_SUBJECTS:
        files = glob(folder + "/S%d"%subject + "/MyPoseFeatures/D3_Positions/*.cdf")
        for file in files:
            d3 = cdflib.CDF(file)["pose"].squeeze().reshape(-1,32,3)[:, joint_idxs]
            data_train.append(d3)
            label_train.append(i)
                     
    for subject in TEST_SUBJECTS:
        files = glob(folder + "/S%d"%subject + "/MyPoseFeatures/D3_Positions/*.cdf")
        for file in files:
            d3 = cdflib.CDF(file)["pose"].squeeze().reshape(-1,32,3)[:, joint_idxs]
            data_test.append(d3)
            label_test.append(i)
            
data = data_train + data_test
label = label_train + label_test

import numpy as np
np.save(path+"data.npy", np.array(data))
np.save(path+"label.npy", np.array(label))
#lens = [len(d) for d in data]            



