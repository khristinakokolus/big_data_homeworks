#!/bin/bash

declare -r NETWORK="kokolus-homework-8-network"

docker build -f Dockerfile.api . -t rest_api:1.0
docker run -d -p 8080:8080 --network ${NETWORK}  --name rest_api --rm rest_api:1.0
