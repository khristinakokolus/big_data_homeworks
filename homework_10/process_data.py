import json
from datetime import timedelta
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import to_date, max, min


SPARK = SparkSession.builder.appName('DataProcessing').getOrCreate()


def read_data(spark, file_name):
    df = spark.read.format("csv").option("header", "true").option("multiline", "true") \
        .option("inferSchema", "true").load(file_name)
    df_updated = df.withColumn("trending_date", to_date(df.trending_date, 'yy.dd.mm'))
    return df_updated


def write_data(result_data, file_name):
    json_object = json.dumps(result_data, indent=4)

    with open(file_name, "w") as outfile:
        outfile.write(json_object)


def get_category_name(category_id, file_name):
    with open(file_name, 'r') as json_file:
        category_data = json.load(json_file)
        for item in category_data["items"]:
            if item["id"] == category_id:
                category_name = item["snippet"]["title"]
                return category_name
    return None


def find_trending_videos(df):
    trending_videos = {"videos": []}
    most_trending_videos = df.groupBy("video_id").count().sort(desc('count')).limit(10)
    videos = most_trending_videos.collect()
    for video in videos:
        video_data = df.filter(df.video_id == video.video_id).sort(desc('trending_date'))
        video_data_collected = video_data.collect()

        trending_days_data = []
        for row in video_data_collected:
            trending_day = {
                "date": row.trending_date.strftime("%Y.%d.%m"),
                "views": int(row.views),
                "likes": int(row.likes),
                "dislikes": int(row.dislikes)
            }
            trending_days_data.append(trending_day)

        video = {
            "id": video.video_id,
            "title": video_data_collected[0].title,
            "description": video_data_collected[0].description,
            "latest_views": int(video_data_collected[0].views),
            "latest_likes": int(video_data_collected[0].likes),
            "latest_dislikes": int(video_data_collected[0].dislikes),
            "trending_days": trending_days_data
        }

        trending_videos["videos"].append(video)
    return trending_videos


def find_trending_week_categories(df, file_with_category):
    trending_week_categories = {"weeks": []}

    first_min_date = df.agg(min('trending_date').alias('min_trending_date')).collect()[0].min_trending_date
    last_max_date = df.agg(max('trending_date').alias('max_trending_date')).collect()[0].max_trending_date

    first_day_week = first_min_date
    last_day_week = first_day_week + timedelta(days=6)

    while last_day_week <= last_max_date:

        week_data_df = df.filter((df.trending_date >= first_day_week) & (df.trending_date <= last_day_week))
        if week_data_df.rdd.isEmpty():
            week = {
                "start_date": first_day_week.strftime("%Y.%d.%m"),
                "end_date": last_day_week.strftime("%Y.%d.%m"),
                "category_id": "",
                "category_name": "",
                "number_of_videos": 0,
                "total_views": 0,
                "video_ids": []
            }
            trending_week_categories["weeks"].append(week)

            first_day_week = first_day_week + timedelta(days=7)
            last_day_week = last_day_week + timedelta(days=7)
            continue
        videos_min_date_df = week_data_df.groupBy('video_id').agg(min('trending_date').alias('min_trending_date'))
        videos_max_date_df = week_data_df.groupBy('video_id').agg(max('trending_date').alias('max_trending_date'))
        df_videos_dates = week_data_df.join(videos_min_date_df, on='video_id').join(videos_max_date_df, on='video_id')

        popular_videos_df = df_videos_dates.filter(
            df_videos_dates.min_trending_date != df_videos_dates.max_trending_date)
        videos_min_date_df = popular_videos_df.filter(
            popular_videos_df.trending_date == popular_videos_df.min_trending_date).select('video_id', 'views')\
            .withColumnRenamed('views', 'initial_views')
        videos_max_date_df = popular_videos_df.filter(
            popular_videos_df.trending_date == popular_videos_df.max_trending_date).select('video_id', 'category_id', 'views')\
            .withColumnRenamed('views', 'result_views')
        videos_joined_df = videos_min_date_df.join(videos_max_date_df, on='video_id')
        videos_joined_df = videos_joined_df.withColumn('total_views',
                                                       videos_joined_df.result_views - videos_joined_df.initial_views)
        categories_df = videos_joined_df.groupBy('category_id').sum('total_views') \
            .withColumnRenamed("sum(total_views)", "views_by_category")

        top_category = categories_df.sort(desc('views_by_category')).limit(1).collect()[0]
        category_name = get_category_name(str(top_category.category_id), file_with_category)

        collected_videos_joined_df = videos_joined_df\
            .filter(videos_joined_df.category_id == top_category.category_id).collect()
        video_ids = []
        for video in collected_videos_joined_df:
            video_ids.append(video.video_id)

        week = {
            "start_date": first_day_week.strftime("%Y.%d.%m"),
            "end_date": last_day_week.strftime("%Y.%d.%m"),
            "category_id": top_category.category_id,
            "category_name": category_name,
            "number_of_videos": len(video_ids),
            "total_views": top_category.views_by_category,
            "video_ids": video_ids
        }

        trending_week_categories["weeks"].append(week)

        first_day_week = first_day_week + timedelta(days=7)
        last_day_week = last_day_week + timedelta(days=7)

    return trending_week_categories


def find_trending_tags(df):
    trending_tags = {"months": []}

    first_month_min_date = df.agg(min('trending_date').alias('min_trending_date')).collect()[0].min_trending_date
    last_month_max_date = df.agg(max('trending_date').alias('max_trending_date')).collect()[0].max_trending_date

    first_day_month = first_month_min_date
    last_day_month = first_day_month.replace(
        day=1, month=first_day_month.month % 12 + 1, year=first_day_month.year + int(
                                                        first_day_month.month / 12)) - timedelta(days=1)

    while last_day_month <= last_month_max_date:

        month_data = df.filter((df.trending_date >= first_day_month) & (df.trending_date <= last_day_month))
        tags_df = month_data.select('video_id', 'tags').dropDuplicates(['video_id']).collect()
        tags_data = dict()

        for row in tags_df:
            updated_tags = row.tags.replace('"', '').split("|")
            for tag in updated_tags:
                if tag in tags_data.keys():
                    tags_data[tag].append(row.video_id)
                else:
                    tags_data[tag] = [row.video_id]
        most_trending_tags = sorted(tags_data.items(), key=lambda x: len(x[1]), reverse=True)[:10]
        tags_data = []
        for trending_tag in most_trending_tags:
            tag = {
                "tag": trending_tag[0],
                "number_of_videos": len(trending_tag[1]),
                "video_ids": trending_tag[1]
            }
            tags_data.append(tag)

        month = {
            "start_date": first_day_month.strftime("%Y.%d.%m"),
            "end_date": last_day_month.strftime("%Y.%d.%m"),
            "tags": tags_data
        }

        trending_tags["months"].append(month)

        first_day_month = last_day_month + timedelta(days=1)
        last_day_month = first_month_min_date.replace(
            day=1, month=first_day_month.month % 12 + 1, year=first_day_month.year + int(
                first_day_month.month / 12)) - timedelta(days=1)
    return trending_tags


def find_top_viewed_channels(df):
    top_viewed_channels = {"channels": []}
    full_df = df.join(df.groupBy('video_id').agg(max('trending_date').alias('max_trending_date')), on='video_id')
    full_videos_max_date_df = full_df.filter(full_df.trending_date == full_df.max_trending_date)
    channel_views_df = full_videos_max_date_df.groupBy('channel_title') \
        .sum('views').withColumnRenamed("sum(views)", "total_views").sort(desc('total_views')).limit(20)

    collected_channel_views_df = channel_views_df.collect()
    for row in collected_channel_views_df:
        start_date = df.filter(
            df.channel_title == row.channel_title).agg(min('trending_date').alias('min_trending_date')).collect()[
                                                              0].min_trending_date
        end_date = df.filter(
            df.channel_title == row.channel_title).agg(max('trending_date').alias('max_trending_date')).collect()[
                                                            0].max_trending_date

        channel_videos_df = full_videos_max_date_df.filter(full_videos_max_date_df.channel_title == row.channel_title)
        collected_channel_videos_df = channel_videos_df.collect()
        videos_views = []
        for video in collected_channel_videos_df:
            video_data = {
                "video_id": video.video_id,
                "views": video.views
            }
            videos_views.append(video_data)

        channel = {
            "channel_name": row.channel_title,
            "start_date": start_date.strftime("%Y.%d.%m"),
            "end_date": end_date.strftime("%Y.%d.%m"),
            "total_views": int(row.total_views),
            "videos_views": videos_views
        }
        top_viewed_channels["channels"].append(channel)

    return top_viewed_channels


def find_channels_with_trending_videos(df):
    channels_with_trending_videos = {"channels": []}

    video_data_df = df.groupBy("video_id", "title",  "channel_title").count()
    channels_with_trending_videos_df = video_data_df.groupBy('channel_title') \
        .sum('count').withColumnRenamed("sum(count)", "trending_days").sort(desc('trending_days')).limit(10)

    collected_channels_with_trending_videos = channels_with_trending_videos_df.collect()
    for row in collected_channels_with_trending_videos:

        channel_videos_df = video_data_df.filter(video_data_df.channel_title == row.channel_title)\
            .withColumnRenamed('count', 'trending_days_amount')
        collected_channel_videos_df = channel_videos_df.collect()
        videos_days = []
        for video in collected_channel_videos_df:
            video_day = {
                "video_id": video.video_id,
                "video_title": video.title,
                "trending_days": int(video.trending_days_amount)
            }

            videos_days.append(video_day)

        channel = {
            "channel_name": row.channel_title,
            "total_trending_days": int(row.trending_days),
            "videos_days": videos_days
        }
        channels_with_trending_videos["channels"].append(channel)

    return channels_with_trending_videos


def find_top_videos_by_ratio(df, file_with_category):
    top_videos_by_ratio = {"categories": []}
    top_videos_df = df.filter(df.views > 100000).withColumn("ratio_likes_dislikes", df.likes/df.dislikes)
    categories = df.select('category_id').distinct().collect()

    for row in categories:
        category_name = get_category_name(str(row.category_id), file_with_category)

        categories_videos_df = top_videos_df.filter(top_videos_df.category_id == str(row.category_id))
        max_ratio_likes_dislikes_df = categories_videos_df.groupBy('video_id').agg(max('ratio_likes_dislikes')
                                                                                   .alias('max_ratio_likes_dislikes'))
        ratio_likes_dislikes_df = categories_videos_df.join(max_ratio_likes_dislikes_df, on='video_id')
        videos_df = ratio_likes_dislikes_df.filter(
            ratio_likes_dislikes_df.ratio_likes_dislikes == ratio_likes_dislikes_df.max_ratio_likes_dislikes)

        videos_df = videos_df.sort(desc('ratio_likes_dislikes')).limit(10).collect()

        videos = []
        for video in videos_df:
            video = {
                "video_id": video.video_id,
                "video_title": video.title,
                "ratio_likes_dislikes": video.ratio_likes_dislikes,
                "views": int(video.views)
            }
            videos.append(video)

        category = {
            "category_id": int(row.category_id),
            "category_name": category_name,
            "videos": videos
        }

        top_videos_by_ratio["categories"].append(category)
    return top_videos_by_ratio


def process_data(df):
    category_file = "US_category_id.json"

    print("Started processing 1 question: ")
    # find trending videos
    trending_videos = find_trending_videos(df)
    write_data(trending_videos, "results/trending_videos.json")
    print("Successfully processed 1 question")
    print()

    print("Started processing 2 question: ")
    # find trending week categories
    trending_week_categories = find_trending_week_categories(df, category_file)
    write_data(trending_week_categories, "results/trending_week_categories.json")
    print("Successfully processed 2 question")
    print()

    print("Started processing 3 question: ")
    # find trending tags
    trending_tags = find_trending_tags(df)
    write_data(trending_tags, "results/trending_tags.json")
    print("Successfully processed 3 question")
    print()

    print("Started processing 4 question: ")
    # find top viewed channels
    top_viewed_channels = find_top_viewed_channels(df)
    write_data(top_viewed_channels, "results/top_viewed_channels.json")
    print("Successfully processed 4 question")
    print()

    print("Started processing 5 question: ")
    # find channels with trending videos
    channels_with_trending_videos = find_channels_with_trending_videos(df)
    write_data(channels_with_trending_videos, "results/channels_with_trending_videos.json")
    print("Successfully processed 5 question")
    print()

    print("Started processing 6 question: ")
    # find top videos by categories
    top_videos_by_ratio = find_top_videos_by_ratio(df, category_file)
    write_data(top_videos_by_ratio, "results/top_videos_by_ratio.json")
    print("Successfully processed 6 question")
    print()

    print("Successfully processed all questions.")


def main():
    # here using sample csv file from archive from Kaggle
    df = read_data(SPARK, 'USvideos.csv')
    process_data(df)


if __name__ == '__main__':
    main()
