#!/bin/bash
declare -r NETWORK="kokolus-homework-8-network"

docker build --tag kokolus-producer -f Dockerfile.producer .
docker run -d --name kafka-producer --network ${NETWORK} --rm kokolus-producer