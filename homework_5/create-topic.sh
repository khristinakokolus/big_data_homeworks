#!/bin/bash

declare -r NETWORK="kokolus-homework-5-network"

# creating Kafka topic
docker run -it --rm --network ${NETWORK} -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-topics.sh --create  --bootstrap-server kafka-server:9092 --replication-factor 1 --partitions 3 --topic test-topic