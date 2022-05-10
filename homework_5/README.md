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

![docker_ps](https://user-images.githubusercontent.com/60686300/167567616-2c1c4cbb-ef66-4fda-aee8-4ab62c72b508.png)

2. topic creation

![topic](https://user-images.githubusercontent.com/60686300/167567678-631dde8d-f4f5-4a49-9c16-b82df6ac2b9f.png)

3. sending and reading messages from the created topic

![producer-consumer](https://user-images.githubusercontent.com/60686300/167567727-d0a72394-8fac-43ae-9a79-787e2922f0ca.png)

4. shutting down servers

![down](https://user-images.githubusercontent.com/60686300/167567773-555e0768-fe01-411e-aa64-4696930d258b.png)

