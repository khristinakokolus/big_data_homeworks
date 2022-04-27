#!/bin/bash

declare -a NODES=(node1 node2 node3)
declare -r KEY_SPACE="hw2_Kokolus"

declare -r dml="
USE ${KEY_SPACE};
INSERT INTO favorite_songs (id, author, song_name, release_year)
VALUES (1, 'KALUSH', 'Stefania', 2022);
INSERT INTO favorite_songs (id, author, song_name, release_year)
VALUES (2, 'Go_A', 'SHUM', 2021);

INSERT INTO favorite_movies (id, name, producer, release_year)
VALUES (1, 'Home Alone', 'John Hughes', 1990);
INSERT INTO favorite_movies (id, name, producer, release_year)
VALUES (2, 'The Shawshank Redemption' , 'Niki Marvin', 1994);"

echo "Started executing DML"
docker exec -it ${NODES[0]} cqlsh -e "${dml}"
echo "Finished executing DML"