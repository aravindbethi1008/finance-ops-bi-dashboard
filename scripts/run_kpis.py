import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
DB_PATH = ROOT / "daxwell_bi.db"

def main():
    OUT_DIR.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    exec_kpi = pd.read_sql_query("""
        SELECT
          COUNT(*) AS total_transactions,
          ROUND(SUM(amount), 2) AS total_revenue,
          ROUND(AVG(amount), 2) AS avg_transaction_value,
          SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) AS success_txns,
          SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) AS failed_txns,
          ROUND(100.0 * SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) / COUNT(*), 2) AS failure_rate_pct,
          SUM(CASE WHEN is_fraud_flag = 1 THEN 1 ELSE 0 END) AS fraud_flag_txns
        FROM fact_transactions;
    """, conn)

    monthly = pd.read_sql_query("""
        SELECT
          d.year,
          d.month,
          d.month_name,
          COUNT(*) AS transactions,
          ROUND(SUM(t.amount), 2) AS revenue
        FROM fact_transactions t
        JOIN dim_date d ON d.date_key = t.txn_date
        GROUP BY d.year, d.month, d.month_name
        ORDER BY d.year, d.month;
    """, conn)

    exec_kpi.to_csv(OUT_DIR / "executive_kpi.csv", index=False)
    monthly.to_csv(OUT_DIR / "monthly_revenue.csv", index=False)

    conn.close()

    print("KPIs exported to outputs/:")
    print("- outputs/executive_kpi.csv")
    print("- outputs/monthly_revenue.csv")

if __name__ == "__main__":
    main()
