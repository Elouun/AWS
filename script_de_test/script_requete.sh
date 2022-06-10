#!/bin/bash
debut=$(($(date +%s%N)/1000000))
for (( j=1; j<=$1; j++ ))
do

	curl https://myxzcnelvk.execute-api.eu-west-3.amazonaws.com/api/getCategories/Cuban --silent > /dev/null
done
fin=$(($(date +%s%N)/1000000))

echo $1 $(( ($fin-$debut)/$1 )) 