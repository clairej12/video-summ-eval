import numpy

def common_keyframes(truth,pred):
    common = np.multiply(truth,pred)
    return np.sum(common)

def recall(truth, pred, gt_keyframes):
    return common_keyframes(truth,pred) / gt_keyframes

def precision(truth, pred):
    return common_keyframes(truth,pred) / np.sum(pred)

def fscore(truth, pred, num_gt):
    prec = precision(truth, pred)
    rec = recall(truth,pred,num_gt)
    return 2*prec*rec / (prec+rec)
