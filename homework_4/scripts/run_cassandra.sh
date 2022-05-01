#!/bin/bash

declare -r NETWORK="kokolus-cassandra-network"

docker network create --driver bridge ${NETWORK}
docker run --name cassandra-node --network ${NETWORK} -p 9042:9042 -d cassandra:latest
