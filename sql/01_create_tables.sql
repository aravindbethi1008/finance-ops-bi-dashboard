DROP TABLE IF EXISTS dim_customers;
DROP TABLE IF EXISTS dim_accounts;
DROP TABLE IF EXISTS dim_products;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS fact_transactions;

CREATE TABLE dim_customers (
  customer_id INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL,
  segment TEXT NOT NULL,
  region TEXT NOT NULL,
  onboarding_status TEXT NOT NULL,
  created_date TEXT NOT NULL
);

CREATE TABLE dim_accounts (
  account_id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  account_type TEXT NOT NULL,
  opened_date TEXT NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
);

CREATE TABLE dim_products (
  product_id INTEGER PRIMARY KEY,
  product_name TEXT NOT NULL,
  product_category TEXT NOT NULL
);

CREATE TABLE dim_date (
  date_key TEXT PRIMARY KEY,
  year INTEGER NOT NULL,
  quarter INTEGER NOT NULL,
  month INTEGER NOT NULL,
  month_name TEXT NOT NULL,
  week INTEGER NOT NULL,
  day INTEGER NOT NULL
);

CREATE TABLE fact_transactions (
  txn_id INTEGER PRIMARY KEY,
  txn_date TEXT NOT NULL,
  customer_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  status TEXT NOT NULL,
  channel TEXT NOT NULL,
  is_fraud_flag INTEGER NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
  FOREIGN KEY (account_id) REFERENCES dim_accounts(account_id),
  FOREIGN KEY (product_id) REFERENCES dim_products(product_id)
);
