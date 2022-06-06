
# Kafka configs
TOPIC = 'transactions'
BOOTSTRAP_SERVERS=['kafka-server:9092']

# Cassandra configs
HOST = 'cassandra-node'
PORT = 9042
KEYSPACE = 'transactions'
FRAUD_TRANSACTIONS_TABLE = "fraud_transactions"
TRANSACTIONS_AMOUNTS_TABLE = "transactions_amounts"
RECEIVED_TRANSACTIONS_TABLE = "received_transactions"
