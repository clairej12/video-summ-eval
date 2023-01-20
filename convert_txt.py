from numpy import loadtxt
import sys
import os
import json
from datetime import datetime

def get_duration(annotation):
    duration = annotation["info"]["duration"]
    dt = datetime.strptime(timestring,'%H:%M:%S')
    total_seconds = dt.second + dt.minute*60 + dt.hour*3600
    return total_seconds

def create_vector(indices, duration):
    output = np.zeros(duration)
    output[indices] = 1
    return output
    # vector = [int(i in indices) for i in range(0, duration)]
    # return np.array(map(lambda x: (1 if x else 0),vector))

def create_range_vector(indices, duration, interval):
    output = np.zeros(duration, dtype=int)
    intervals = [[min(0,i-interval),max(duration-1, i+interval)] for i in indices]
    for start, end in intervals:
        output[np.arange(start, end+1)] = 1
    return output

def ground_truth():
    # find out ground truth format (img or time stamp)

def main(filename, metafile):
    f = open(metafile)
    annotation = json.load(f)
    indices = loadtxt(filename, comments="#", delimiter="\n", unpack=False)
    # frame_indices=[int(idx) for idx in open(directory+'frame_indices_'+ sys.argv[6]+'_'+str(n_clusters)+'_'+str(sampling_rate)+'.txt','r').read().splitlines()]

    duration = get_duration(annotation)

    gt = ground_truth()
    out = create_vector(indices, duration)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    annotation = sys.argv[2] if len(sys.argv) > 2 else None
    if(filenmae != None and annotation != None):
        main(filename, annotation)
    else:
        print("Missing Video Path Argument")