# Homework 5: Writing to Kafka using code

## Description

The purpose of this homework is to work with Kafka using code.


## Usage


To create Zookeeper and Kafka servers and create new topic:
```
cd homework_6
bash scripts/run-cluster.sh
```


To send data to Kafka:

```
cd src
bash ../scripts/add-messages.sh
```

NOTE: in ```src``` folder must be ```tweets.csv``` file. For now there is provided sample tweets file.


To shutdown servers:
```
bash scripts/shutdown-cluster.sh
```


## Results

1. docker ps command after servers launching



2. launch of container with Kafka producer



3. Kafka consumer



4. shutting down servers


