#!/bin/bash

declare -a NODES=(node1 node2 node3)
declare -r KEY_SPACE="hw2_Kokolus"

declare -r ddl="
CREATE KEYSPACE ${KEY_SPACE} WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE ${KEY_SPACE};
CREATE TABLE favorite_songs(
  id int,
  author text,
  song_name text,
  release_year int,
  PRIMARY KEY (id)
);
CREATE TABLE favorite_movies(
  id int,
  name text,
  producer text,
  release_year int,
  PRIMARY KEY (id)
);"

echo "Started executing DDL"
docker exec -it ${NODES[0]} cqlsh -e "${ddl}"
echo "Finished executing DDL"
