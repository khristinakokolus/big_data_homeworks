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


2. DESCRIBE TABLES after execution of ```DDL_script.sh```


3. SELECT * from both tables after execution of ```DML_script.sh```
