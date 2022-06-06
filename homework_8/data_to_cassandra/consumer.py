import json
from kafka import KafkaConsumer
import variables as var
from cassandra_client import CassandraClient


CONSUMER = KafkaConsumer(var.TOPIC, bootstrap_servers=var.BOOTSTRAP_SERVERS,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         auto_offset_reset='earliest', group_id=None)


def main():

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    for message in CONSUMER:

        message_data = message.value

        fraud_transactions_data = (
            var.FRAUD_TRANSACTIONS_TABLE, message_data["nameOrig"], message_data["step"], message_data["type"],
            message_data["amount"], message_data["oldbalanceOrg"], message_data["newbalanceOrig"],
            message_data["nameDest"], message_data["oldbalanceDest"], message_data["newbalanceDest"],
            message_data["isFraud"])
        client.insert_fraud_transactions(fraud_transactions_data)

        transactions_amounts_data = (var.TRANSACTIONS_AMOUNTS_TABLE, message_data["nameOrig"], message_data["amount"])
        client.insert_transactions_amounts(transactions_amounts_data)

        received_transaction_data = (
            var.RECEIVED_TRANSACTIONS_TABLE, message_data["nameOrig"], message_data["amount"],
            message_data["transaction_date"])
        client.insert_received_transactions(received_transaction_data)

    client.close()


if __name__ == '__main__':
    main()