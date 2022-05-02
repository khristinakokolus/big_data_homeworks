# Homework 4: Cassandra interaction

## Description

The purpose of this homework is to interact with Cassandra using Python code.


## Usage

1. To launch connection with Cassandra run:

```
bash scripts/run_cassandra.sh
```

2. To create tables in Cassandra:

```
bash scripts/create_tables.sh
```

3. To populate tables with data in Cassandra:

```
bash scripts/populate_data_cassandra.sh
```

4. To run REST API:

```
bash scripts/run_rest_api.sh
```


5. To get answers to questions use such queries.

To get reviews by product id:
    - http://localhost:5000/reviews_by_product?product_id=B002G54DAA

To get reviews by product id and star rating:
    - http://localhost:5000/reviews_by_product?product_id=B002G54DAA&star_rating=5

To get reviews by customer id:
    - http://localhost:5000/reviews_by_product?customer_id=43173394


NOTE: sample select statements are located in select_statements.cql.
