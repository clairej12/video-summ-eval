#!/bin/bash

cat=$1 # take first cmd line arg
DIR=/mnt/data1/jielin/msmo/keyframe/; # /data/jielin/msmo/video/;
OUT=/mnt/data1/claire/video-summ/keyframe-extraction/; # /home/jielin/claire/video-summ/keyframes/sift/;
HOMEDIR=$PWD;
sampling_rate="1";

# echo $DIR$cat
for subcat in $OUT$cat/*/;do
    echo $subcat
    for vid in `find $subcat -name "*2[1-9]"`;do
        path=$vid"/kfs_per_scene/evaluation.txt"
        if [ ! -f  "$path" ]
        then
            cd $HOMEDIR
            # echo $folder_name
            trunc=$(dirname "$vid")
            subfolder=$(basename "$trunc")/$(basename "$vid")
            echo $DIR$cat/$subfolder
            echo $vid"/kfs_per_scene"
            # echo $OUT$subfolder/$folder_name/
            python get_imgs.py $DIR$cat/$subfolder $vid"/kfs_per_scene"
        else
            echo "Already evaluated"
        fi
    done
done