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

1. servers launching and topic creation

![docker_ps](https://user-images.githubusercontent.com/60686300/168819852-59a758fb-0ad9-4493-8dfe-403e83be2682.png)

2. docker ps command after servers launching

![true_ps](https://user-images.githubusercontent.com/60686300/168821191-a896685e-c1bd-4cbf-b6ba-baeb70ed1dd5.png)

3. launch of container with Kafka producer

![build](https://user-images.githubusercontent.com/60686300/168820117-3f69680e-97ed-4683-b73d-90b0e946b0b9.png)

4. Kafka consumer

![process](https://user-images.githubusercontent.com/60686300/168820207-bb63cdbd-0fef-4115-aa88-5d3477247748.png)

5. shutting down servers


![shutwown](https://user-images.githubusercontent.com/60686300/168820256-b5346fbb-170f-4d46-9d7e-a9bb316045af.png)

