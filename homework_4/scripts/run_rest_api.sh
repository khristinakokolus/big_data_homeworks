#!/bin/bash
docker build --tag kokolus-rest .
docker run --name rest-api --network kokolus-cassandra-network -p 5000:5000 kokolus-rest