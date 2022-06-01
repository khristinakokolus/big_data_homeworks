#!/bin/bash
declare -r NETWORK="kokolus-homework-7-network"

docker build --tag kokolus-consumer -f Dockerfile.consumer .
docker run -d --name kafka-consumer --network ${NETWORK} -v "$(pwd)"/tweets_data:/opt/app/tweets_data --rm kokolus-consumer
