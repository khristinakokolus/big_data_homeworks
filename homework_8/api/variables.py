
# Cassandra configs
HOST = 'cassandra-node'
PORT = 9042
KEYSPACE = 'transactions'
FRAUD_TRANSACTIONS_TABLE = "fraud_transactions"
SELECTED_DATA_FRAUD_TRANSACTIONS = ["uid", "step", "type", "amount", "old_balance_org", "new_balance_orig",
            "name_dest", "old_balance_dest", "new_balance_dest", "is_fraud"]
TRANSACTIONS_AMOUNTS_TABLE = "transactions_amounts"
SELECTED_DATA_TRANSACTIONS_AMOUNTS = ["uid", "amount"]
RECEIVED_TRANSACTIONS_TABLE = "received_transactions"
SELECTED_DATA_RECEIVED_TRANSACTIONS = ["total_amount"]
