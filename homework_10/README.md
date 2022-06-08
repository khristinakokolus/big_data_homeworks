# Homework 10: Spark launch


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
spark-submit --master spark://spark-master:7077 --deploy-mode client process_data.py
exit
```

NOTE: in ```homework_10``` folder must be ```USvideos.csv``` and ```US_category_id.json``` files.

To shutdown Spark cluster:

```
docker-compose down
```

## Results