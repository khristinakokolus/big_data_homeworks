from cassandra_client import CassandraClient
import pandas as pd


def create_connection(table):
    host = 'cassandra-node'
    port = 9042
    keyspace = 'reviews'

    client = CassandraClient(host, port, keyspace)
    client.connect()


def reviews_by_product(client, table, product_id):
    select = "SELECT review_body FROM %s WHERE product_id = '%s' ALLOW FILTERING;" % (table, product_id)
    print("create select")
    rows = client.execute(select)
    print(rows)
    df = pd.DataFrame(list(client.execute(select)))
    client.close()
    print("get query")
    return df.to_json()
