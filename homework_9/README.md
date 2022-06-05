# Homework 9: Spark launch


## Description

The purpose of this homework is to launch Spark.


## Usage


To create one master and worker Spark containers:

```
cd homework_9
docker-compose up -d
```

Then launch spark-commit container:

```
bash run-container.sh
```

Inside container run such commands:

```
cd /opt/app
spark-submit --master spark://spark-master:7077 --deploy-mode client count_rows.py
exit
```

NOTE: in ```homework_9``` folder must be ```PS_20174392719_1491204439457_log.csv``` file.

To shutdown Spark cluster:

```
docker-compose down
```

## Results


- docker ps result after Spark launching

<img width="972" alt="ps" src="https://user-images.githubusercontent.com/60686300/172067702-6cd71a70-7808-468b-98f5-b324f8fd431a.png">


- result of the program using Spark methods. Amount of data in the dataset is 6362621

![spark-res](https://user-images.githubusercontent.com/60686300/172067759-e8cb5f1e-bbe7-4613-8454-031f8618aa06.jpg)
