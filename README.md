Daxwell Finance & Operations BI Dashboard
Overview

This project is a solo end-to-end Business Intelligence solution that simulates how Finance and Operations analytics are built in a real enterprise environment.

The focus is not just on visualization, but on the entire BI lifecycle — from data creation and modeling to KPI computation and executive reporting. The project demonstrates how raw transactional data can be transformed into decision-ready insights using Python, SQL, and Power BI.

Business Problem

Finance and Operations teams often need a single, reliable view of business performance to answer questions such as:

How much revenue are we generating over time?

How many transactions are successful vs failed?

What is the overall failure and fraud rate?

Are revenues trending up or down month over month?

Can executives quickly monitor performance without digging into raw data?

This project addresses these needs by building a lightweight BI reporting layer that mirrors real-world finance and operational reporting systems.

Solution Approach

The solution follows a structured BI workflow:

Generate realistic, enterprise-style transactional data

Store data in a relational database using a star schema

Compute business KPIs using SQL

Export analytics-ready datasets

Build an executive dashboard in Power BI

Each step is modular, reproducible, and easy to validate.

daxwell-bi-dashboard/
│
├── data/
│   ├── customers.csv
│   ├── accounts.csv
│   ├── products.csv
│   └── transactions.csv
│
├── scripts/
│   ├── generate_data.py
│   ├── load_to_sqlite.py
│   └── run_kpis.py
│
├── sql/
│   ├── 01_create_tables.sql
│   └── 02_kpi_queries.sql
│
├── outputs/
│   ├── executive_kpi.csv
│   ├── monthly_revenue.csv
│   └── screenshots/
│       ├── kpi_cards.png
│       └── monthly_revenue_trend.png
│
├── powerbi/
│   └── Financial_Operational_Dashboard.pbix
│
├── documentation/
│   ├── Project_Overview.md
│   └── Video_Script.md
│
├── daxwell_bi.db
└── README.md

Data Modeling

The project uses a star schema, a standard approach in enterprise data warehouses.

Fact Table

fact_transactions

Transaction amount

Transaction status (success / failed)

Fraud flag

Transaction date

Foreign keys to dimensions

Dimension Tables

dim_customers – customer segment and region

dim_accounts – account type and status

dim_products – product category and attributes

dim_date – year, month, and calendar breakdown

This design enables efficient KPI computation and scalable reporting.

Key KPIs Implemented

The following executive-level metrics are calculated using SQL:

Total Revenue

Total Transactions

Average Transaction Value

Successful Transactions

Failed Transactions

Failure Rate (%)

Fraud-Flagged Transactions

Monthly Revenue Trend

These KPIs are exported as clean CSV files and consumed directly by Power BI.

Technology Stack

Python – data generation, orchestration

Pandas / NumPy – data manipulation

SQLite – relational database storage

SQL – KPI aggregation and business logic

Power BI – dashboard and visualization

The stack was chosen to reflect real-world BI tooling while remaining lightweight and easy to run locally.

How to Run the Project
1. Generate Data
python scripts/generate_data.py


Creates enterprise-style CSV datasets for customers, accounts, products, and transactions.

2. Load Data into SQLite
python scripts/load_to_sqlite.py


Builds the SQLite database and loads data into star schema tables.

3. Generate KPIs
python scripts/run_kpis.py


Exports:

outputs/executive_kpi.csv

outputs/monthly_revenue.csv

4. View Dashboard

Open the Power BI file:

powerbi/Financial_Operational_Dashboard.pbix


The dashboard reflects the KPI logic generated from SQL.

Dashboard Overview

The Power BI dashboard is designed for executive and operational users:

Top section: KPI cards for quick performance monitoring

Bottom section: Monthly revenue trend for time-based analysis

Screenshots are included in the outputs/screenshots folder for quick review.

Validation & Reproducibility

This project is fully reproducible:

Scripts can be re-run to regenerate fresh data

Database can be rebuilt from CSV files

KPI outputs are regenerated using SQL logic

Dashboard reflects the latest KPI exports

This ensures transparency between data logic and visual output.

What This Project Demonstrates

End-to-end BI pipeline design

Practical data modeling skills

SQL-based KPI development

Executive-focused dashboard design

Ability to explain and validate analytics outputs

This project mirrors the type of work performed in Finance, Operations, and Analytics teams in real organizations.

Author

Aravind Bethi
Business Intelligence Analyst

Last updated by Aravind Bethi