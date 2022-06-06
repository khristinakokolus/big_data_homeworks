import json
import time
from kafka import KafkaProducer
import pandas as pd
import datetime
import random


TOPIC = 'transactions'
PRODUCER = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))
FILE_NAME = "PS_20174392719_1491204439457_log.csv"


def read_data(file_name):
    data = pd.read_csv(file_name, sep=',')
    return data


def get_random_date():
    days = random.randint(0, 30)
    random_date = datetime.datetime.now() - datetime.timedelta(days=days)
    return random_date.strftime("%Y-%m-%d")


def main():
    df = read_data(FILE_NAME)
    dictionary_data = [
        dict([
            (colname, row[i])
            for i, colname in enumerate(df.columns)
        ])
        for row in df.values
    ]
    for transaction in dictionary_data:
        transaction['transaction_date'] = get_random_date()
        PRODUCER.send(TOPIC, transaction)

        time.sleep(0.04)
    PRODUCER.flush()


if __name__ == '__main__':
    main()