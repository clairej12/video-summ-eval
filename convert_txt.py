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

def main(filename, metafile):
    f = open(metafile)
    annotation = json.load(f)
    indices = loadtxt(filename, comments="#", delimiter="\n", unpack=False)

    duration = get_duration(annotation)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    annotation = sys.argv[2] if len(sys.argv) > 2 else None
    if(filenmae != None and annotation != None):
        main(filename, annotation)
    else:
        print("Missing Video Path Argument")