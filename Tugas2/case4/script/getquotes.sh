#!/bin/sh

apk update && apk add curl jq

URL=https://api.adviceslip.com/advice
LOKASI=/data

echo will run every $DELAY seconds

while true;
do
	date=$(date '+%Y-%m-%d_%H:%M:%S')
	echo processing at $date
	fname="output_$date.txt"
	curl -sL $URL | jq '.slip.advice' > $fname 
	sleep $DELAY
done
