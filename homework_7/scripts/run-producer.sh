#!/bin/bash
declare -r NETWORK="kokolus-homework-7-network"

docker build --tag kokolus-producer -f Dockerfile.producer .
docker run -d --name kafka-producer --network ${NETWORK} --rm kokolus-producer
