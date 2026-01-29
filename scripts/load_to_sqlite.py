import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SQL_DIR = ROOT / "sql"
DB_PATH = ROOT / "daxwell_bi.db"

def main():
    # Read CSVs
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    accounts = pd.read_csv(DATA_DIR / "accounts.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    transactions = pd.read_csv(DATA_DIR / "transactions.csv")

    # Connect DB
    conn = sqlite3.connect(DB_PATH)

    # Create tables
    create_sql = (SQL_DIR / "01_create_tables.sql").read_text(encoding="utf-8")
    conn.executescript(create_sql)

    # Load dimensions
    customers.to_sql("dim_customers", conn, if_exists="append", index=False)
    accounts.to_sql("dim_accounts", conn, if_exists="append", index=False)
    products.to_sql("dim_products", conn, if_exists="append", index=False)

    # Build dim_date from transactions
    dates = pd.to_datetime(transactions["txn_date"]).drop_duplicates().sort_values()
    dim_date = pd.DataFrame({
        "date_key": dates.dt.date.astype(str),
        "year": dates.dt.year,
        "quarter": ((dates.dt.month - 1) // 3 + 1),
        "month": dates.dt.month,
        "month_name": dates.dt.strftime("%b"),
        "week": dates.dt.isocalendar().week.astype(int),
        "day": dates.dt.day,
    })
    dim_date.to_sql("dim_date", conn, if_exists="append", index=False)

    # Load fact
    transactions.to_sql("fact_transactions", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

    print(f" Loaded SQLite DB: {DB_PATH}")

if __name__ == "__main__":
    main()
