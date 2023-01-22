#!/bin/bash

cat=$1 # take first cmd line arg
DIR=/mnt/data1/jielin/msmo/keyframe/; # /data/jielin/msmo/video/;
OUT=/mnt/data1/claire/video-summ/sift/; # /home/jielin/claire/video-summ/keyframes/sift/;
HOMEDIR=$PWD;
sampling_rate="1";

# echo $DIR$cat
for subcat in $OUT$cat/*/;do
    echo $subcat
    for vid in $subcat*/;do
        echo $vid
        cd $HOMEDIR
        # echo $folder_name
        trunc=$(dirname "$vid")
        subfolder=$(basename "$trunc")/$(basename "$vid")
        echo $DIR$cat/$subfolder" and "$vid"_keyframes_"
        # echo $OUT$subfolder/$folder_name/
        python get_imgs.py $DIR$cat/$subfolder $vid"_keyframes_"
    done
done