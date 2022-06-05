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