#!/bin/bash

path="/home/pi/Pictures"
mkdir "$path/processed"

i=$(ls $path/processed | wc -l)
max=$(ls $path | wc -l)
echo $path
echo $i
echo $max

for f in $(ls $path | grep -i '[0-z]......................jpg');
do	
	i=$((i+1))
	echo $(($i*100/$max))
	echo $f
	#ffmpeg -i "$f" -q:v 10 -hide_banner -loglevel error -vf scale=100:100 -n "$path/processed/$f"
	
done



