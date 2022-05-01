#!/bin/bash
docker run --name rest-api --network kokolus-cassandra-network -p 8080:8080 -d rest:1.0