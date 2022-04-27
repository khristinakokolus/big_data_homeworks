# Homework 2: Cassandra launch

## Description

The purpose of this homework is to get acquainted with Cassandra. Here are four bash scripts:
cluster launching, DDL queries, DML queries and cluster shutdown.


## Usage


To create a cluster:
```
cd homework_2
bash run-cluster.sh
```

To create and populate tables:
```
bash DDL_script.sh
bash DML_script.sh
```


To shutdown cluster:
```
bash shutdown-cluster.sh
```


NOTE: if bash script fails to execute then execute first such command ```dos2unix {bash script}```.
After that bash script have to work.


## Results

1. docker ps command after cluster launching

![image](https://user-images.githubusercontent.com/60686300/165501528-9684fd9a-30b3-4ca2-942b-99bd15c692fb.png)


2. DESCRIBE TABLES after execution of ```DDL_script.sh```


![image](https://user-images.githubusercontent.com/60686300/165501731-62943e6c-e057-40bf-81c3-1ca4749df5c3.png)


3. SELECT * from both tables after execution of ```DML_script.sh```

![image](https://user-images.githubusercontent.com/60686300/165501796-20c72233-3926-4cb0-a063-a1eff0d788f4.png)

4. Shutting down cluster

![image](https://user-images.githubusercontent.com/60686300/165502324-0e23aec9-a68b-4fab-b82f-1a510a7fda0d.png)
