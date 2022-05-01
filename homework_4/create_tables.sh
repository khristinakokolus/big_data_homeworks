#!/bin/bash

declare -r KEY_SPACE="hw4_Kokolus"

declare -r ddl="
CREATE KEYSPACE ${KEY_SPACE} WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE ${KEY_SPACE};
CREATE TABLE product_statistics(
    review_id text,
    product_id text,
    product_title text,
    star_rating int,
    review_body text,
    review_date date,
    PRIMARY KEY (product_id, review_id, star_rating, review_date)
) WITH CLUSTERING ORDER BY (review_id DESC, star_rating DESC, review_date ASC
);
CREATE TABLE customer_statistics(
    review_id text,
    customer_id int,
    verified_purchase text,
    review_body text,
    review_date date,
    PRIMARY KEY (customer_id, review_id, verified_purchase, review_date)
) WITH CLUSTERING ORDER BY (review_id DESC, verified_purchase DESC, review_date DESC
);
CREATE TABLE haters_backers(
    review_id text,
    customer_id int,
    star_rating int,
    review_date date,
    PRIMARY KEY (customer_id, review_id, star_rating, review_date)
) WITH CLUSTERING ORDER BY (review_id DESC, star_rating DESC, review_date DESC
);"

echo "Started executing tables creation"
docker exec -it cassandra-node cqlsh -e "${ddl}"
echo "Finished executing tables creation"