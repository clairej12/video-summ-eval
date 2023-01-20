import numpy
import cv2
import os
import sys
from evaluation import *
import pdb

thresholds = {
    "rmse":0.01, 
    "psnr":40, 
    "ssim":0.9, 
    "fsim":0.45, 
    # "issm":, 
    "sre":42, 
    "uiq":0.1
}

def main(gt_path, pred_path,metric_list = None):
    truths = []
    preds = []

    for (root, dirs, gt_files) in os.walk(gt_path):
        for file in gt_files:
            if '.jpg' in file:
                im = cv2.imread(root+'/'+file)
                truths.append(im)
    # pdb.set_trace()
    for (root, dirs, pred_files) in os.walk(pred_path):
        for file in pred_files:
            if '.jpg' in file:
                im = cv2.imread(root+'/'+file)
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

if __name__ == '__main__':
    gt_path = sys.argv[1]
    pred_path = sys.argv[2]
    metrics = sys.argv[3] if len(sys.argv) > 3 else None
    main(gt_path,pred_path,metrics)
