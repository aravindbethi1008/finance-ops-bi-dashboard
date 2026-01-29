import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

np.random.seed(42)

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

def random_dates(start_date: datetime, end_date: datetime, n: int) -> pd.Series:
    start_u = int(start_date.timestamp())
    end_u = int(end_date.timestamp())
    stamps = np.random.randint(start_u, end_u, size=n)
    s = pd.Series(pd.to_datetime(stamps, unit="s"))
    return s.dt.date.astype(str)

def main():
    n_customers = 500
    n_products = 12
    n_accounts = 800
    n_txn = 12000

    today = datetime.today()
    start_date = today - timedelta(days=365)

    # Customers
    customers = pd.DataFrame({
        "customer_id": np.arange(1, n_customers + 1),
        "customer_name": [f"Customer {i}" for i in range(1, n_customers + 1)],
        "segment": np.random.choice(["Retail", "SME", "Corporate"], size=n_customers, p=[0.7, 0.2, 0.1]),
        "region": np.random.choice(["NE", "SE", "MW", "SW", "W"], size=n_customers),
        "onboarding_status": np.random.choice(["Completed", "In Progress", "Failed"], size=n_customers, p=[0.78, 0.17, 0.05]),
        "created_date": random_dates(start_date, today, n_customers),
    })

    # Products
    product_categories = ["Payments", "Cards", "Loans", "Deposits"]
    products = pd.DataFrame({
        "product_id": np.arange(1, n_products + 1),
        "product_name": [f"Product {i}" for i in range(1, n_products + 1)],
        "product_category": np.random.choice(product_categories, size=n_products),
    })

    # Accounts
    account_types = ["Checking", "Savings", "Credit", "Loan"]
    accounts = pd.DataFrame({
        "account_id": np.arange(1, n_accounts + 1),
        "customer_id": np.random.choice(customers["customer_id"], size=n_accounts),
        "account_type": np.random.choice(account_types, size=n_accounts, p=[0.4, 0.3, 0.2, 0.1]),
        "opened_date": random_dates(start_date, today, n_accounts),
        "status": np.random.choice(["Active", "Closed", "Frozen"], size=n_accounts, p=[0.88, 0.08, 0.04]),
    })

    # Transactions
    txn_dates = pd.to_datetime(random_dates(start_date, today, n_txn))
    status = np.random.choice(["SUCCESS", "FAILED"], size=n_txn, p=[0.93, 0.07])
    channels = np.random.choice(["Mobile", "Web", "Branch", "API"], size=n_txn, p=[0.45, 0.35, 0.12, 0.08])

    base_amount = np.random.lognormal(mean=3.5, sigma=0.6, size=n_txn)  # skewed like real payments
    amount = np.round(base_amount, 2)

    fraud_flag = (np.random.rand(n_txn) < 0.02).astype(int)  # ~2% flagged

    transactions = pd.DataFrame({
        "txn_id": np.arange(1, n_txn + 1),
        "txn_date": txn_dates.dt.date.astype(str),
        "customer_id": np.random.choice(customers["customer_id"], size=n_txn),
        "account_id": np.random.choice(accounts["account_id"], size=n_txn),
        "product_id": np.random.choice(products["product_id"], size=n_txn),
        "amount": amount,
        "status": status,
        "channel": channels,
        "is_fraud_flag": fraud_flag,
    })

    # Save CSVs
    customers.to_csv(DATA_DIR / "customers.csv", index=False)
    accounts.to_csv(DATA_DIR / "accounts.csv", index=False)
    products.to_csv(DATA_DIR / "products.csv", index=False)
    transactions.to_csv(DATA_DIR / "transactions.csv", index=False)

    print(" - Data generated:")
    print(" - data/customers.csv")
    print(" - data/accounts.csv")
    print(" - data/products.csv")
    print(" - data/transactions.csv")

if __name__ == "__main__":
    main()
