import json
from kafka import KafkaProducer
import pandas as pd
import datetime


TOPIC = 'tweets'
PRODUCER = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))


def read_data(file_name):
    data = pd.read_csv(file_name, sep=',')
    return data


def current_time():
    return datetime.datetime.today()


def main():
    file_name = "twcs.csv"
    df = read_data(file_name)
    dictionary_data = [
        dict([
            (colname, row[i])
            for i, colname in enumerate(df.columns)
        ])
        for row in df.values
    ]
    for tweet in dictionary_data:
        tweet['created_at'] = str(current_time())
        PRODUCER.send(TOPIC, tweet)
    PRODUCER.flush()


if __name__ == '__main__':
    main()
