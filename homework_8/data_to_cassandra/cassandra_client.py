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

    def insert_fraud_transactions(self, data):
        query = "INSERT INTO %s (uid, step, type, amount, old_balance_org, new_balance_orig," \
                " name_dest, old_balance_dest, new_balance_dest, is_fraud) " \
                "VALUES ('%s', %s, '%s', %s, %s, %s, '%s', %s, %s, %s)" % data
        self.execute(query)

    def insert_transactions_amounts(self, data):
        query = "INSERT INTO %s (uid, amount) " \
                "VALUES ('%s', %s)" % data
        self.execute(query)

    def insert_received_transactions(self, data):
        query = "INSERT INTO %s (uid, amount, transaction_date) " \
                "VALUES ('%s', %s, '%s')" % data
        self.execute(query)
