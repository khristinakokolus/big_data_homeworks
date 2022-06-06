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
        return self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def select_fraud_transactions(self, table, uid):
        query = "SELECT * FROM %s WHERE uid = '%s' AND is_fraud = 1;" % (table, uid)
        rows = self.execute(query)
        return rows

    def select_transactions_amounts(self, table, uid):
        query = "SELECT * FROM %s WHERE uid = '%s' ORDER BY amount DESC LIMIT 3;" % (table, uid)
        rows = self.execute(query)
        return rows

    def select_received_transactions(self, table, uid, start_date, end_date):
        query = f"SELECT sum(amount) FROM %s WHERE uid = '%s' " \
                f"AND transaction_date >= '%s' " \
                f"AND transaction_date <= '%s';" % (table, uid, start_date, end_date)
        rows = self.execute(query)
        return rows
