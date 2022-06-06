from cassandra_client import CassandraClient
from flask import Flask, request
import variables as var

app = Flask(__name__)


@app.route("/fraud_transactions", methods=['POST'])
def select_data_fraud_transactions():
    query_data = request.get_json()
    response = dict()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_fraud_transactions(var.FRAUD_TRANSACTIONS_TABLE, query_data['uid'])
    response["columns"] = var.SELECTED_DATA_FRAUD_TRANSACTIONS
    i = 1
    for row in data:
        response[str(i)] = row
        i += 1

    client.close()
    return response


@app.route("/transactions_amounts", methods=['POST'])
def select_data_transactions_amounts():
    query_data = request.get_json()
    response = dict()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_transactions_amounts(var.TRANSACTIONS_AMOUNTS_TABLE, query_data['uid'])
    response["columns"] = var.SELECTED_DATA_TRANSACTIONS_AMOUNTS
    i = 1
    for row in data:
        response[str(i)] = row
        i += 1

    client.close()
    return response


@app.route("/received_transactions", methods=['POST'])
def select_data_received_transactions():
    query_data = request.get_json()
    response = dict()

    client = CassandraClient(var.HOST, var.PORT, var.KEYSPACE)
    client.connect()

    data = client.select_received_transactions(
        var.RECEIVED_TRANSACTIONS_TABLE, query_data['uid'], query_data["start_date"], query_data["end_date"])
    response["columns"] = var.SELECTED_DATA_RECEIVED_TRANSACTIONS
    i = 1
    for row in data:
        response[str(i)] = row
        i += 1

    client.close()
    return response


if __name__ == "__main__":
    app.run(debug=True)
