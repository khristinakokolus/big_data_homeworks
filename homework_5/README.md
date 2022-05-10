# Homework 5: Kafka launch

## Description

The purpose of this homework is to get acquainted with Kafka. Here are three bash scripts:
cluster launching, topic creation and shutting down cluster.


## Usage


To create Zookeeper and Kafka servers:
```
cd homework_5
bash run-cluster.sh
```

To create a new topic:
```
bash create-topic.sh
```


To shutdown servers:
```
bash shutdown-cluster.sh
```


NOTE: if bash script fails to execute then execute first such command ```dos2unix {bash script}```.
After that bash script have to work.


## Results

1. docker ps command after servers launching


2. topic creation


3. sending and reading messages from the created topic


4. shutting down servers