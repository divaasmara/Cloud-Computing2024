#!/bin/sh
docker container run \
    --name myprocess1 \
    -dit \
    -e DELAY=8 \
    -v $(pwd)/files:/data \
    -v $(pwd)/script:/script \
    --workdir /data \
    alpine:3.18 \
    /bin/sh -c "/script/getjokes.sh; while true; do echo jalan; sleep 20000; done"



