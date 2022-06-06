#!/bin/bash

declare -r NETWORK="kokolus-homework-8-network"

if docker run --name cassandra-node --network ${NETWORK} -p 9042:9042 -d cassandra:latest; then
   echo "Successfully created Cassandra node"
else
   echo "Cassandra node already exists"
fi

sleep 80s
docker cp data_to_cassandra/ddl.cql cassandra-node:/
docker exec cassandra-node cqlsh -f ddl.cql
