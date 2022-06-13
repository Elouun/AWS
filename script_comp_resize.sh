#!/bin/bash

mkdir processed
i=10116
for f in $(ls | grep -i '[j-z]......................jpg');
do	
	i=$((i+1))
	echo $(($i*100/21605))
	ffmpeg -i "$f" -q:v 10 -hide_banner -loglevel error -vf scale=100:100 -y "processed/$f"
	
done



