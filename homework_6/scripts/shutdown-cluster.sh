#!/bin/bash

declare -r NETWORK="kokolus-homework-6-network"
declare -a CONTAINERS=(zookeeper-server kafka-server)

# stop docker containers
for container in "${CONTAINERS[@]}"
do
  if docker stop ${container}; then
    echo "Stopped ${container}"
  else
    echo "Failed to stop ${container}"
  fi
done

# remove docker containers
for container in "${CONTAINERS[@]}"
do
  if docker rm ${container}; then
    echo "Removed ${container}"
  else
    echo "Failed to remove ${container}"
  fi
done

# delete network
if docker network rm ${NETWORK}; then
   echo "Successfully deleted network ${NETWORK}"
else
   echo "Can not delete network ${NETWORK}"
fi
