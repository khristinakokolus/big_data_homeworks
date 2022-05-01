class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def insert_product_record(self, table, review_id, product_id, product_title, star_rating, review_body, review_date):
        review_body = review_body.replace("\'", "").replace("\"", "")
        product_title = product_title.replace("\'", "").replace("\"", "")
        data = (table, review_id, product_id, product_title, star_rating, review_body, review_date)
        query = "INSERT INTO %s (review_id, product_id, product_title, star_rating, review_body, review_date) " \
                "VALUES ('%s', '%s', '%s', %d, '%s', %r)" % data
        self.execute(query)

    def insert_customer_record(self, table, review_id, customer_id, verified_purchase, review_body, review_date):
        review_body = review_body.replace("\'", "").replace("\"", "")
        data = (table, review_id, customer_id, verified_purchase, review_body, review_date)
        query = "INSERT INTO %s (review_id, customer_id, verified_purchase, review_body, review_date)" \
                " VALUES ('%s', %d, %r, '%s',  %r)" % data
        self.execute(query)

    def insert_haters_backers_record(self, table, review_id, customer_id, star_rating, review_date):
        data = (table, review_id, customer_id, star_rating, review_date)
        query = "INSERT INTO %s (review_id, customer_id, star_rating, review_date)" \
                " VALUES ('%s', %d, %d, %r)" % data
        self.execute(query)

    def read_from_table(self, table_name):
        query = "SELECT * FROM %s" % table_name
        rows = self.session.execute(query)
        for row in rows:
            print(row)