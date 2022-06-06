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

1. Launch of Zookeeper, Kafka and Cssandra servers

![photo_2022-06-06_11-19-12](https://user-images.githubusercontent.com/60686300/172123342-44ef766a-1208-47b2-844b-c4705f82cb72.jpg)

<img width="639" alt="Screenshot 2022-06-06 at 11 05 28" src="https://user-images.githubusercontent.com/60686300/172123456-012a6ab9-f12e-4e8d-a5dd-ca02e9e8ce82.png">

2. Launch of Kafka producer and consumer

![photo_2022-06-06_11-19-13](https://user-images.githubusercontent.com/60686300/172123541-e912588a-2eeb-4b36-adb0-f0a69249acc5.jpg)

![photo_2022-06-06_11-19-15](https://user-images.githubusercontent.com/60686300/172123666-22730896-fe24-4120-9149-56dc9d184157.jpg)

3. Working generator->Kafka->consumer schema

<img width="1249" alt="Screenshot 2022-06-06 at 10 01 40" src="https://user-images.githubusercontent.com/60686300/172123963-9afd959b-7905-4ade-8e3a-a73ebc119844.png">

4. Look of tables in Cassandra

![photo_2022-06-06_11-19-17](https://user-images.githubusercontent.com/60686300/172124032-c18922a4-4ce3-4718-b1f8-3250be0fbb68.jpg)

![photo_2022-06-06_11-19-18](https://user-images.githubusercontent.com/60686300/172124065-67a4f1bd-3e61-4705-9735-6c49c7fd04f7.jpg)

![photo_2022-06-06_11-19-20](https://user-images.githubusercontent.com/60686300/172124098-49a1414c-373b-4875-8e7f-f03ed683bf19.jpg)

5. Sample API responses

![photo_2022-06-06_11-19-21](https://user-images.githubusercontent.com/60686300/172124346-f16a5983-9896-400e-8784-57b52df36e8e.jpg)

![photo_2022-06-06_11-19-23](https://user-images.githubusercontent.com/60686300/172124465-81cc9d7e-4403-4a95-9993-3333dda0a4fe.jpg)

![photo_2022-06-06_11-19-25](https://user-images.githubusercontent.com/60686300/172124502-8786e0f9-4d9e-4fe6-873f-ec5a6608e87a.jpg)
