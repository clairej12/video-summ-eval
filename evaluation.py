import numpy
# import image_similarity_measures
from image_similarity_measures.quality_metrics import rmse, psnr, ssim, fsim, issm, sre, uiq  

LESS = "smaller is better"
GREATER = "larger is better"
direction = {
    "rmse": LESS, 
    "psnr": GREATER, 
    "ssim": GREATER, 
    "fsim": GREATER, 
    # "issm":, 
    "sre": GREATER, 
    "uiq": GREATER
}

def score(truth,pred,metric):
    if metric == 'rmse': # absolute error
        score = rmse(truth, pred)
    elif metric == 'psnr': # absolute error
        score = psnr(truth, pred)
    elif metric == 'ssim': # ranges from [0,1]
        score = ssim(truth, pred)
    elif metric == 'fsim': # ranges from [0,1]
        score = fsim(truth, pred)
    elif metric == 'issm':
        score = issm(truth, pred)
    elif metric == 'sre':
        score = sre(truth, pred)
    elif metric == 'uiq': # ranges from [-1,1]
        score = uiq(truth, pred)
    else:
        score = None
        print('Unknown metric')
    return score 

def common_keyframes(truths,preds,metric,thresh,frames = False):
    num_common = 0
    if frames:
        common = []
    for pred in preds:
        best_score = 0
        matching = None
        for truth in truths:
            if score(truth,pred,metric) > best_score:
                best_score = score(truth,pred,metric)
                matching = truth
        if (direction[metric] == GREATER and best_score >= thresh) \
        or (direction[metric] == LESS and best_score <= thresh):
            num_common +=1
            if frames:
                common.append((pred,matching,best_score))
    if frames:
        return num_common, common
    return num_common

def recall(truths,preds,metric,thresh):
    num_common = common_keyframes(truths,preds,metric,thresh)
    return num_common / len(truths)

def precision(truths,preds,metric,thresh):
    num_common = common_keyframes(truths,preds,metric,thresh)
    return num_common / len(preds)

def fscore(truths,preds,metric,thresh):
    num_common = common_keyframes(truths,preds,metric,thresh)
    prec = num_common / len(preds)
    rec = num_common / len(truths)
    return 2*prec*rec / (prec+rec)

# Indices:
#     def common_ind(truth,pred):
#         common = np.multiply(truth,pred)
#         return np.sum(common)

#     def common_keyframes(truth,pred):
#         return common_ind(truth,pred)

#     def recall(truth, pred, gt_keyframes):
#         return common_keyframes(truth,pred) / gt_keyframes

#     def precision(truth, pred):
#         return common_keyframes(truth,pred) / np.sum(pred)

#     def fscore(truth, pred, num_gt):
#         prec = precision(truth, pred)
#         rec = recall(truth,pred,num_gt)
#         return 2*prec*rec / (prec+rec)
