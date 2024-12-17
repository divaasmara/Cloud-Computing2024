#!/bin/sh
docker container run \
    --name myprocess1 \
    -dit \
    -e DELAY=10000 \
    -v $(pwd)/files:/data \
    -v $(pwd)/script:/script \
    --workdir /data \
    alpine:3.18 \
    /bin/sh /script/getjokes.sh



