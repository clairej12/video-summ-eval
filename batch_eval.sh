#!/bin/bash

# animals      food     movies
# art          health   personal_style
# clothes      hobbies  sports
# cooking      holiday  transportation
# education    house    travel
# electronics  job

declare -a arr=("food" "movies" "art" "health" 
    "personal_style" "clothes" "hobbies" "sports" 
    "cooking" "holiday" "transportation" "education" 
    "house" "travel" "electronics" "job")

max_num_processes=$(ulimit -u)
limiting_factor=10
num_processes=$((max_num_processes/limiting_factor))

for cat in "${arr[@]}";do
    ((i=i%num_processes)); ((i++==0)) && wait
    echo $cat
    ./eval.sh $cat &
done