#!/bin/bash

mkdir processed
path="/home/pi/Pictures"
i="ls $path/precessed | wc -l"
max="ls $path | wc -l"
echo $path
echo $i
echo $max

for f in $(ls | grep -i '[j-z]......................jpg');
do	
	i=$((i+1))
	echo $(($i*100/$max))
	ffmpeg -i "$f" -q:v 10 -hide_banner -loglevel error -vf scale=100:100 -y "$path/processed/$f"
	
done



