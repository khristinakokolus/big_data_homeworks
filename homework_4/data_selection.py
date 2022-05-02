from cassandra_client import CassandraClient
import default_values


def create_connection():
    client = CassandraClient(default_values.host, default_values.port, default_values.keyspace)
    client.connect()


def reviews_by_product(client, table, product_id):
    select = "SELECT review_body FROM %s WHERE product_id = '%s' ALLOW FILTERING;" % (table, product_id)
    data = list(client.session.execute(select))
    return data


def reviews_by_product_rating(client, table, product_id, star_rating):
    select = "SELECT review_body " \
             "FROM %s " \
             "WHERE product_id = '%s' " \
             "AND star_rating = %d ALLOW FILTERING;" % (table, product_id, star_rating)
    data = list(client.session.execute(select))
    return data


def reviews_by_customer(client, table, customer_id):
    select = "SELECT review_body" \
             " FROM %s" \
             " WHERE customer_id = %d " \
             "ALLOW FILTERING;" % (table, customer_id)
    data = list(client.session.execute(select))
    return data

