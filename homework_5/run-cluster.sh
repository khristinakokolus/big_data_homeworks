#!/bin/bash

declare -r NETWORK="kokolus-homework-5-network"

# create network for Kafka
if docker network create --driver bridge ${NETWORK}; then
   echo "Successfully created network ${NETWORK}"
else
   echo "Such network ${NETWORK} already exists"
fi


# create Zookeeper and Kafka servers
if docker run -d --name zookeeper-server --network ${NETWORK} -e ALLOW_ANONYMOUS_LOGIN=yes bitnami/zookeeper:latest; then
  echo "Created container for Zookeeper server"
else
  echo "Failed to create container for Zookeeper server"
fi

if docker run -d --name kafka-server --network ${NETWORK} -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest; then
  echo "Created container for Kafka server"
else
  echo "Failed to create container for Kafka server"
fi