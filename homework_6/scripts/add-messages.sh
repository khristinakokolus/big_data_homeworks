#!/bin/bash
declare -r NETWORK="kokolus-homework-6-network"

docker build --tag kokolus-add-messages .
docker run -d --name kafka-producer --network ${NETWORK} kokolus-add-messages