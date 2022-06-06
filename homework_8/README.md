# Homework 8: Interact with Cassandra and Kafka through code

## Description

The purpose of this homework is to work with Cassandra and Kafka using code.


## Usage


To create Zookeeper, Kafka and Cassandra servers, create new topic and tables:
```
cd homework_8
bash scripts/run-kafka-cluster.sh
bash scripts/run-cassandra-cluster.sh
```


To send data to Kafka:

```
cd data_to_kafka
bash ../scripts/run-producer.sh
```

To read data from Kafka and add to Cassandra tables:

```
cd ..
cd data_to_cassandra
bash ../scripts/run-consumer.sh
```

To run API:
```
cd ..
cd api
bash ../scripts/run-api.sh
```

NOTE: in ```data_to_kafka``` folder must be ```PS_20174392719_1491204439457_log.csv``` file.


To shutdown Kafka, Zookeeper and Cassandra servers:
```
cd ..
bash scripts/shutdown-cluster.sh
```

## API usage

Example queries are located in ```requests.http```

There are three endpoints in the API:
1. http://localhost:8080/fraud_transactions. 
Here you can get answer to the question: Show all user transactions with certain id that have been marked as fraud.
2. http://localhost:8080/transactions_amounts
Here you can get answer to the question: Show the 3 biggest transactions of user with certain id.
3. http://localhost:8080/received_transactions
Here you can get answer to the question: Show the sum of all incoming transactions received by the user with certain 
id for the specified period.

For every query you receive dictionary that contains all names of the columns and rows with data.


## Results