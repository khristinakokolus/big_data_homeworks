#!/bin/bash

declare -a NODES=(node1 node2 node3)
declare -r NETWORK="cassandra-network-homework-2"

# stop docker containers
for node in "${NODES[@]}"
do
  if docker stop ${node}; then
    echo "Stopped ${node} container"
  else
    echo "Failed to stop ${node} container"
  fi
done

# remove docker containers
for node in "${NODES[@]}"
do
  if docker rm ${node}; then
    echo "Removed ${node} container"
  else
    echo "Failed to remove ${node} container"
  fi
done

# delete network
if docker network rm ${NETWORK}; then
   echo "Successfully deleted network ${NETWORK}"
else
   echo "Can not delete network ${NETWORK}"
fi