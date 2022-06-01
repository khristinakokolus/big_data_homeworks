import json
from kafka import KafkaConsumer
import pandas as pd
from datetime import datetime


TOPIC = 'tweets'
CONSUMER = KafkaConsumer(TOPIC, bootstrap_servers=['kafka-server:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         auto_offset_reset='earliest', group_id=None)
FILE_STARTS = "tweets_data/tweets_"


def form_df(data):
    df = pd.DataFrame(data, columns=['author_id', 'created_at', 'text'])
    return df


def create_file_name(created_at):
    date = str(created_at.day) + "_" \
           + str(created_at.month) + "_" + str(created_at.year) + \
           "_" + str(created_at.hour) + "_" + str(created_at.minute)
    csv_file_name = FILE_STARTS + date + ".csv"
    return csv_file_name


def write_data_to_file(df, csv_file_name):
    df.to_csv(csv_file_name, index=False)


def main():
    old_min = None
    data = []
    for message in CONSUMER:

        # convert created_at to datetime
        created_at_str = message.value["created_at"].split(".", 1)[0]
        created_at = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S")

        # append data
        data.append([message.value["author_id"], created_at, message.value["text"]])

        new_min = created_at.minute

        if old_min is None:
            old_min = new_min

        # check whether minute changed
        if old_min != new_min:
            # process data and write to csv file
            df = form_df(data)
            csv_file_name = create_file_name(df['created_at'].iat[0])
            write_data_to_file(df, csv_file_name)

            # update minute and data list
            data = []
            old_min = new_min


if __name__ == '__main__':
    main()




