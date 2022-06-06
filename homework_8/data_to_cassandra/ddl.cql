CREATE KEYSPACE transactions WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE transactions;

CREATE TABLE fraud_transactions (
    uid text,
    step int,
    type text,
    amount float,
    old_balance_org float,
    new_balance_orig float,
    name_dest text,
    old_balance_dest float,
    new_balance_dest float,
    is_fraud int,
    PRIMARY KEY ((uid), is_fraud)
);


CREATE TABLE transactions_amounts(
    uid text,
    amount float,
    PRIMARY KEY ((uid), amount)
);


CREATE TABLE received_transactions (
    uid text,
    amount float,
    transaction_date date,
    PRIMARY KEY ((uid), transaction_date)
);