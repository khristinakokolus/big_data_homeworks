# Homework 5: Read from Kafka using code

## Description

The purpose of this homework is to work with Kafka using code.


## Usage


To create Zookeeper and Kafka servers and create new topic:
```
cd homework_7
bash scripts/run-cluster.sh
```


To send data to Kafka:

```
cd src
bash ../scripts/run-producer.sh
```

To read data from Kafka and created files with tweets data:

```
cd src
bash ../scripts/run-consumer.sh
```

NOTE: in ```src``` folder must be ```twcs.csv``` file. For now there is provided sample tweets file.


To shutdown servers:
```
cd ..
bash scripts/shutdown-cluster.sh
```


## Results
