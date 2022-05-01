from cassandra_client import CassandraClient
import pandas as pd

host = '0.0.0.0'
port = 9042
keyspace = 'hw4_kokolus'


def create_connection():
    client = CassandraClient(host, port, keyspace)
    client.connect()


def reviews_by_product(client, table, product_id):
    select = "SELECT review_body FROM %s WHERE product_id = '%s' ALLOW FILTERING;" % (table, product_id)
    print("create select")
    rows = client.execute(select)
    print(rows)
    df = pd.DataFrame(list(client.session.execute(select)))
    print("get query")
    return df.to_json()


def reviews_by_product_rating(client, table, product_id, star_rating):
    select = "SELECT review_body " \
             "FROM %s " \
             "WHERE product_id = '%s' " \
             "AND star_rating = %d ALLOW FILTERING;" % (table, product_id, star_rating)


def reviews_by_customer(client, table, customer_id):
    select = "SELECT review_body" \
             " FROM %s" \
             " WHERE customer_id = %d " \
             "ALLOW FILTERING;" % (table, customer_id)


def most_reviewed_products(client, table, review_date_start, review_date_end):
    select = "SELECT COUNT(product_id) AS products_reviews_count, product_id, product_title " \
             "FROM %s " \
             "WHERE review_date <= '%s' " \
             "AND review_date >= '%s' " \
             "GROUP BY product_id " \
             "ALLOW FILTERING;" % (table, review_date_start, review_date_end)