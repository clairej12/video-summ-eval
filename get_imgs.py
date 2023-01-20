import numpy
import cv2 as cv
import os
import sys
from evaluation import *

thresholds = {
    "rmse":, 
    "psnr":, 
    "ssim":, 
    "fsim":, 
    "issm":, 
    "sre":, 
    "uiq": 
}

def main(gt_path, pred_path,metrics == None):
    truths = []
    preds = []
    for file in os.walk(gt_path)
        if '.jpg' in file:
            im = cv2.imread(gt_path+'/'+file,mode='RGB')
            truths.append(im)
    for file in os.walk(pred_path)
        if '.jpg' in file:
            im = cv2.imread(pred_path+'/'+file,mode='RGB')
            preds.append(im)
    print(f"{len(truths)} gt keyframes and {len(preds)} pred keyframes for {gt_path.split('/')[-1]}")
    
    if not metric_list:
        metric_list = ["rmse","psnr","ssim","fsim","issm","sre","uiq"]
    else:
        metric_list = metric_list.split(",")
    for metric in metric_list:
        thresh = thresholds[metric]
        prec = precision(truths,preds,metric,thresh)
        rec = recall(truths,preds,metric,thresh)
        f = fscore(truths,preds,metric, thresh)
        print("Precision: {prec}, Recall: {rec}, F-score: {f} using {metric} with threshold {thresh}")
    # save to file next

if __name__ == 'main':
    gt_path = sys.argv[1]
    pred_path = sys.argv[2]
    metrics = sys.argv[3] if len(sys.argv) > 3 else None
    main(gt_path,pred_path,metrics)
