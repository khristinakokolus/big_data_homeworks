#!/bin/bash

declare -a NODES=(node1 node2 node3)
declare -r NETWORK="cassandra-network-homework-2"
declare -r C_SEEDS="node1,node2,node3"

# create network for Cassandra cluster
if docker network create --driver bridge ${NETWORK}; then
   echo "Successfully created network ${NETWORK}"
else
   echo "Such network ${NETWORK} already exists"
fi

# create nodes for Cassandra cluster
for node in "${NODES[@]}"
do
  if docker run --name ${node} --network ${NETWORK} -d -e CASSANDRA_SEEDS=${C_SEEDS} cassandra:latest; then
    echo "Created container for ${node} for Cassandra cluster"
  else
    echo "Failed to create container for ${node} for Cassandra cluster"
  fi
done