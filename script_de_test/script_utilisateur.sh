#!/bin/bash
for i in 1 5 10 50 100 500 1000
do
	bash /home/antoine/Documents/FAC/M2-S4/pds/script_requete.sh $i & 

	#debut=$(($(date +%s%N)/1000000))
	#for (( j=1; j<=$i; j++ ))
	#do
		#rand=$(($RANDOM%6+35))
		#curl "https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getCloserRestaurant?lat=$rand&long=-75.19926226811313" --silent > /dev/null
		#echo "$i $j"
		#curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getCategories/Cuban --silent > /dev/null
	#done
	#fin=$(($(date +%s%N)/1000000))

	#echo $i $(( ($fin-$debut)/$i )) 
done