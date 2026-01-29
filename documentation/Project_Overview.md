Project Overview

This is a solo end-to-end Business Intelligence project designed to simulate how Finance and Operations analytics are built in real enterprise environments. The project focuses on transforming raw transactional data into actionable insights through structured data modeling, KPI calculations, and executive-level reporting.

The entire pipeline is built from scratch, starting with synthetic enterprise data generation, followed by relational data modeling, SQL-based KPI computation, and finally visual reporting using Power BI. The goal is to demonstrate practical BI skills rather than just visualization.

Business Objective

The primary objective of this project is to enable Finance and Operations stakeholders to quickly monitor and analyze key business performance indicators, including:

Transaction volumes and overall revenue trends
Successful versus failed transaction rates
Fraud-flagged transaction activity
Product-level and account-level performance
Time-based trends for operational monitoring

The dashboard is designed to support executive decision-making, operational monitoring, and performance analysis.

Data Modeling Approach

A star schema design is used to mirror common data warehouse architectures in enterprise BI systems.

The central fact table captures all transactional activity, while surrounding dimension tables provide descriptive context for slicing and analysis.

Fact Table

fact_transactions – Stores transaction amounts, status, fraud flags, and transaction dates

Dimension Tables

dim_customers – Customer segmentation and regional details

dim_accounts – Account type and lifecycle status

dim_products – Product category and attributes

dim_date – Calendar breakdown for time-based analysis

This structure enables efficient querying, scalable reporting, and clean KPI calculations.

Technology Stack

The project leverages commonly used BI and analytics tools:

Python – Data generation, transformation, and orchestration
SQL – KPI computation and aggregation logic
SQLite – Lightweight relational data storage
Power BI – Dashboard development and visualization
Pandas & NumPy – Data manipulation and calculations

The stack was intentionally chosen to reflect real-world BI workflows while keeping the project easy to run locally.

Validation & Reproducibility

The project is fully reproducible and can be validated end-to-end:

The data generation script can be re-run to create fresh datasets
The SQLite database can be rebuilt and reloaded from CSV files
KPI scripts regenerate output files based on SQL logic
The Power BI dashboard directly reflects the exported KPI results

This ensures transparency, consistency, and alignment between data logic and visual outputs.