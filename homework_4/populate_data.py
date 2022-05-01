from data_preparation import read_dataset, form_product_statistics_data,\
    form_customer_statistics_data, form_haters_backers_data
from cassandra_client import CassandraClient


def main():
    file_name = "reviews.tsv"
    data = read_dataset(file_name)
    product_statistics_data = form_product_statistics_data(data)
    customer_statistics_data = form_customer_statistics_data(data)
    haters_backers_data = form_haters_backers_data(data)

    host = 'localhost'
    port = 9042
    keyspace = 'hw4_kokolus'
    product_table = 'product_statistics'
    customer_table = 'customer_statistics'
    haters_backers_table = 'haters_backers'

    client = CassandraClient(host, port, keyspace)
    client.connect()
    records_amount = len(product_statistics_data)
    for i in range(records_amount):
        client.insert_product_record(product_table, product_statistics_data[i][0],
                                     product_statistics_data[i][1],
                                     product_statistics_data[i][2],
                                     product_statistics_data[i][3],
                                     product_statistics_data[i][4],
                                     product_statistics_data[i][5])
        client.insert_customer_record(customer_table, customer_statistics_data[i][0],
                                      customer_statistics_data[i][1],
                                      customer_statistics_data[i][2],
                                      customer_statistics_data[i][3],
                                      customer_statistics_data[i][4])
        client.insert_haters_backers_record(haters_backers_table, haters_backers_data[i][0],
                                            haters_backers_data[i][1],
                                            haters_backers_data[i][2],
                                            haters_backers_data[i][3])
    client.close()


if __name__ == '__main__':
    main()
