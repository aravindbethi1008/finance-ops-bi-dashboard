-- Executive KPIs (overall)
SELECT
  COUNT(*) AS total_transactions,
  ROUND(SUM(amount), 2) AS total_revenue,
  ROUND(AVG(amount), 2) AS avg_transaction_value,
  SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) AS success_txns,
  SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) AS failed_txns,
  ROUND(100.0 * SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) / COUNT(*), 2) AS failure_rate_pct,
  SUM(CASE WHEN is_fraud_flag = 1 THEN 1 ELSE 0 END) AS fraud_flag_txns
FROM fact_transactions;

-- Revenue by month
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

-- Product performance
SELECT
  p.product_category,
  p.product_name,
  COUNT(*) AS transactions,
  ROUND(SUM(t.amount), 2) AS revenue,
  ROUND(AVG(t.amount), 2) AS avg_value
FROM fact_transactions t
JOIN dim_products p ON p.product_id = t.product_id
GROUP BY p.product_category, p.product_name
ORDER BY revenue DESC;

-- Segment + region breakdown
SELECT
  c.segment,
  c.region,
  COUNT(*) AS transactions,
  ROUND(SUM(t.amount), 2) AS revenue,
  ROUND(100.0 * SUM(CASE WHEN t.status='FAILED' THEN 1 ELSE 0 END) / COUNT(*), 2) AS failure_rate_pct
FROM fact_transactions t
JOIN dim_customers c ON c.customer_id = t.customer_id
GROUP BY c.segment, c.region
ORDER BY revenue DESC;

-- Onboarding status distribution
SELECT
  onboarding_status,
  COUNT(*) AS customers
FROM dim_customers
GROUP BY onboarding_status
ORDER BY customers DESC;

-- Month-over-Month revenue growth (simple)
WITH monthly AS (
  SELECT
    d.year,
    d.month,
    ROUND(SUM(t.amount), 2) AS revenue
  FROM fact_transactions t
  JOIN dim_date d ON d.date_key = t.txn_date
  GROUP BY d.year, d.month
)
SELECT
  year,
  month,
  revenue,
  LAG(revenue) OVER (ORDER BY year, month) AS prev_month_revenue,
  CASE
    WHEN LAG(revenue) OVER (ORDER BY year, month) IS NULL THEN NULL
    WHEN LAG(revenue) OVER (ORDER BY year, month) = 0 THEN NULL
    ELSE ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY year, month)) / LAG(revenue) OVER (ORDER BY year, month), 2)
  END AS mom_growth_pct
FROM monthly
ORDER BY year, month;
