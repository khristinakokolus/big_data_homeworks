# Homework 10: Data processing with Spark


## Description

The purpose of this homework is to process data with Spark.


## Usage


To create one master and worker Spark containers:

```
cd homework_10
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


- Successful creation of answers to 6 quastions in Spark:
![image](https://user-images.githubusercontent.com/60686300/172728065-cbefb98f-f7e6-42eb-b583-a160e00f1564.png)

Results are in ```results``` folder:
1. question - ```trending_videos.json```
2. question - ```trending_week_categories.json```
3. question - ```trending_tags.json```
4. question - ```top_viewed_channels.json```
5. question - ```channels_with_trending_videos.json```
6. question - ```top_videos_by_ratio.json```
