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


1. Kafka servers launching and topic creation

![create_kafka_cluster](https://user-images.githubusercontent.com/60686300/171344669-3daea1a5-0214-4d5e-aa17-d2e155e968bb.png)


2.Producer launching

![producer](https://user-images.githubusercontent.com/60686300/171345073-50b20cca-a2ef-4f49-aca8-5bb75357ae21.png)


3.Consumer launching

![consumer](https://user-images.githubusercontent.com/60686300/171345103-96af829b-832f-41cb-8f52-f400733207f5.png)


4. Running containers

![ps](https://user-images.githubusercontent.com/60686300/171345152-8e9e4566-997a-49ff-a1e2-ce4627dbdd0f.png)


5. Created files by consumer

![files](https://user-images.githubusercontent.com/60686300/171345199-73bb7035-dc5c-4e03-90e9-70a253e92c90.png)


6. Files inside

![data1](https://user-images.githubusercontent.com/60686300/171345234-751f70d4-b073-40c4-aad5-6fa18aae2647.png)

![data2](https://user-images.githubusercontent.com/60686300/171345287-d7b7ce70-70a1-400c-b302-345fdea60a69.png)

