import numpy
# import image_similarity_measures
from image_similarity_measures.quality_metrics import rmse, psnr, ssim, fsim, issm, sre, uiq  
        
def score(truth,pred,metric):
    match metric:
        case 'rmse':
            score = rmse(truth, pred)
        case 'psnr':
            score = psnr(truth, pred)
        case 'ssim':
            score = ssim(truth, pred)
        case 'fsim':
            score = fsim(truth, pred)
        case 'issm':
            score = issm(truth, pred)
        case 'sre':
            score = sre(truth, pred)
        case 'uiq':
            score = uiq(truth, pred)
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
        if best_score >= thresh:
            num_common +=1
            if frames:
                common.append((pred,matching,best_score))
    if frames:
        return num_common, common
    return num_common

def recall(truths,preds,metric,thresh):
    num_common = common_keyframes(truths,preds,metric,thresh)
    return num_common / len(truths)

def precision(truths,preds,metric, thresh):
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
