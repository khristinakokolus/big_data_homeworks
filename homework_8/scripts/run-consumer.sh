#!/bin/bash
declare -r NETWORK="kokolus-homework-8-network"

docker build --tag kokolus-consumer -f Dockerfile.consumer .
docker run -d --name kafka-consumer --network ${NETWORK} --rm kokolus-consumer