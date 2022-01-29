#!/bin/bash

echo 'connecting to my docker hub'
docker login -u "abdou2020" -p "abdou54460380"
echo 'pulling the image'
docker pull abdou2020/houce-price-app
echo 'kill on port 5000 before running the container'
docker kill $(docker ps -q) | true
echo 'running the container'
docker run -d -p 5000:5000 abdou2020/houce-price-app
