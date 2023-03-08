#!/bin/sh
if [ $# -eq 0 ]
  then
    echo " Please pass path to the input file"!
    exit 1
fi
echo "Running island counter script for input file: $1 "
echo "Building docker image"
docker build --tag isl_counter .
echo "Running docker image"
docker run isl_counter python ./src/main.py $1
