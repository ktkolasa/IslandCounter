#!/bin/sh
echo "Building docker image"
docker build --tag isl_counter .
echo "Running docker image"
docker run isl_counter python ./src/main.py $1