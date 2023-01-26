import os
import sys
import re
import pdb

metris = ["rmse","psnr","ssim","fsim","sre","uiq"]

class Video:
    def __init__(self):
        self.rmse = None # [precision, recall, fscore, average]
        self.psnr = None
        self.ssim = None
        # self.fsim = None
        self.sre = None
        # self.uiq = None

def get_metrics(line):
    if 'nan' in line:
        return [0,0,0,0]
    nums = [float(x) for x in re.findall(r"[-+]?(?:\d*\.*\d+)", line)]
    # if nums[0] == None:
    #     print(line)
    return nums[:-1]

def parse(file):
    f = open(file,'r')
    print(file)
    vid = Video()
    for line in f:
        # if line == None:
        #     print(file)
        if 'rmse' in line:
            vid.rmse = get_metrics(line)
            # if len(vid.rmse) < 4:
            #     print(file, line)
        elif 'psnr' in line:
            vid.psnr = get_metrics(line)
        elif 'ssim' in line:
            vid.ssim = get_metrics(line)
        # elif 'fsim' in line:
        #     vid.fsim = get_metrics(line)
        elif 'sre' in line:
            vid.sre = get_metrics(line)
            # if len(vid.sre) < 4:
            #     print(file, line)
        # elif 'uiq' in line:
        #     vid.uiq = get_metrics(line)
            # if len(vid.uiq) < 4:
            #     print(file, line)
        # else:
        #     print(file)
    return vid

def make_str(mlist):
    return ','.join([str(x) for x in mlist])

def main(path):
    # pdb.set_trace()
    videos = []
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if 'evaluation.txt' in file:
                vid = parse(root+'/'+file)
                # if vid.rmse == None:
                #     print(root+"/"+file)
                videos.append(vid)
    # denom = len(videos)
    print(len(videos))
    # pdb.set_trace()
    rmse = [vid.rmse for vid in videos if vid.rmse != None]
    denom = len(rmse)
    print(denom)
    # pdb.set_trace()
    rmse = make_str([sum(x)/denom for x in zip(*rmse)])

    psnr = [vid.psnr for vid in videos if vid.psnr!=None]
    psnr = make_str([sum(x)/denom for x in zip(*psnr)])

    ssim = [vid.ssim for vid in videos if vid.ssim!=None]
    ssim = make_str([sum(x)/denom for x in zip(*ssim)])

    # fsim = [vid.fsim for vid in videos if vid.fsim!=None]
    # fsim = make_str([sum(x)/denom for x in zip(*fsim)])

    sre = [vid.sre for vid in videos if vid.sre!=None and len(vid.sre)==4]
    sre = make_str([sum(x)/denom for x in zip(*sre)])
    
    # pdb.set_trace()
    # uiq = [vid.uiq for vid in videos if vid.uiq!=None and len(vid.uiq)==4]
    # uiq = make_str([sum(x)/denom for x in zip(*uiq)])
    
    write_list = ['Avg precision, avg recall, avg fscore, avg score\n']
    write_list.append('rmse: '+rmse+'\n')
    write_list.append('psnr: '+psnr+'\n')
    write_list.append('ssim: '+ssim+'\n')
    # write_list.append('fsim: '+fsim+'\n')
    write_list.append('sre: '+sre+'\n')
    # write_list.append('uiq: '+uiq)


    f = open(path+"/summary_eval.txt", "w")
    f.writelines(write_list)
    f.close()

if __name__ == '__main__':            
    path = sys.argv[1]
    main(path)