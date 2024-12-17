#!/bin/sh

apk update && apk add curl jq

URL=https://api.chucknorris.io/jokes/random
LOKASI=/data

echo will run every $DELAY seconds

while true;
do
    date=$(date '+%Y-%m-%d_%H:%M:%S')
    echo processing at $date
    fname="output_$date.txt"
    
    # Mengambil data dari API dan memeriksa apakah curl berhasil
    response=$(curl -sL $URL)
    if [ $? -eq 0 ]; then
        joke=$(echo $response | jq '.value')
        echo $joke > $fname
    else
        echo "Error: Failed to fetch joke" > $fname
    fi

    sleep $DELAY
done
