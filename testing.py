import numpy
import cv2
import os
import sys
from evaluation import *

# metrics: 
gt_path = '/home/jielin/claire/video-summ/keyframes/category/subcategory/test/kfs_per_scene/4/46.jpg'
pred_path = '/home/jielin/claire/video-summ/keyframes/category/subcategory/test/kfs_per_scene/4/15.jpg'
metrics = ["rmse","psnr","ssim","fsim","sre","uiq"] # "issm"

truth = cv2.imread(gt_path)
pred = cv2.imread(pred_path)

for metric in metrics:
    print(metric + ": ", score(truth,pred,metric))

# print("issm: ", score(truth,pred,"issm"))