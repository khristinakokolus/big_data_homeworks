CREATE  KEYSPACE reviews WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE reviews;

-- 1 table
CREATE TABLE product_rating(
    product_id text,
    review_id text,
    star_rating int,
    review_body text,
    PRIMARY KEY (product_id, star_rating));

-- 2 table
CREATE TABLE customer_rating(
    customer_id int,
    review_id text,
    star_rating int,
    review_body text,
    PRIMARY KEY (customer_id, star_rating));

-- 3 table
CREATE TABLE customer_statistics(
    customer_id int,
    total_reviews_amount int,
    product_ids list<text>,
    PRIMARY KEY(customer_id, total_reviews_amount, product_ids))