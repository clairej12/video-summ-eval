import numpy
import cv2
import os
import sys
from evaluation import *

# metrics: 
gt_path = '/mnt/data1/jielin/msmo/keyframe/animals/amphibians/ANIAMP0021/keyframe_1.jpg'
pred_path = '/mnt/data1/claire/video-summ/sift/animals/amphibians/ANIAMP0021/_keyframes_/frame10.jpg'
metrics = ["rmse","psnr","ssim","fsim","sre","uiq"] # "issm"

truth = cv2.imread(gt_path)
pred = cv2.imread(pred_path)
dim = (truth.shape[1],truth.shape[0])
pred = cv2.resize(pred, dim, interpolation = cv2.INTER_AREA)

# for metric in metrics:
#     print(metric + ": ", score(truth,pred,metric))

print("ssim: ", score(truth,pred,"ssim"))