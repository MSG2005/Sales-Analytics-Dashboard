# Sales Analytics Dashboard

This project is an end-to-end Sales Data Analytics solution built using Python.
It focuses on analyzing business performance, identifying key trends, and deriving actionable insights through data cleaning, exploratory analysis, customer segmentation, and interactive dashboards.

The goal of this project is to simulate a real-world data analyst workflow, from raw data to business-ready insights.

## Project Overview
This project analyzes sales data to uncover:
- Revenue trends
- Top-performing regions & categories
- Customer segmentation using RFM analysis
- Business insights through visual dashboards

## Tools & Technologies
- Python
- Pandas – data manipulation
- NumPy – numerical operations
- Matplotlib & Seaborn – data visualization
- Streamlit – interactive dashboard
- Git & GitHub – version control

## Business Objectives

This project answers the following key business questions:

1) What is the overall sales performance of the business?
2) Which regions and product categories generate the highest revenue?
3) Who are the most valuable customers?
4) How do sales vary over time?
5) How can customers be segmented for better decision-making?   

## Project Summary

Business Intelligence & RFM AnalysisThe workflow transforms raw sales data into actionable business strategy through five distinct phases:

**- Data Foundations (Loading & Cleaning):** Established a reliable source of truth by handling date conversions, removing duplicates, and engineering time-based features (Year/Month) for longitudinal analysis.

**- Business Intelligence (EDA & KPIs):** Identified core revenue drivers through category and regional performance metrics. Key findings highlighted significant seasonality and a Pareto-style distribution where a minority of product categories generate the majority of total revenue.
  
**- Customer Strategy (RFM Segmentation):** Quantified customer value by scoring Recency, Frequency, and Monetary behaviors. This resulted in a tiered segmentation (High, Medium, and Low Value), providing a framework for targeted marketing and churn prevention.

## Project Pipeline Overview

| Phase | Focus | Key Output |
|---|---|---|
| Ingestion | Structure & Health | Identification of missing values and data types |
| Refinement  | Data Integrity | Cleaned dataset with time-series features |
| Exploration | Pattern Recognition | Discovery of sales trends and seasonality |
| Evaluation  | Metric Tracking | Core KPIs: Total Sales, AOV, and Order Volume |
| Strategy | Behavioral Analysis | RFM Segments for personalized targeting |

## Interactive Dashboard (Streamlit)

The Streamlit dashboard allows users to:
- Filter data by Region and Category
- View KPIs dynamically
- Analyze:
    - Sales by Category
    - Sales by Region
    - Monthly Sales Trends
    - Customer Segments

## How to Run This Project Locally

Install required libraries
```
pip install -r requirements.txt
```

Launch the Streamlit dashboard
```
streamlit run app/app.py
```

Once launched, the dashboard will open in your browser where you can explore sales insights interactively.

## Key Business Insights

- A small set of customers contributes a large portion of total revenue.
- Certain regions consistently outperform others.
- Sales show clear monthly seasonality.
- High-value customers are critical for business growth.

## Final Note

This project represents my commitment to continuous learning and building real-world analytical solutions.
More improvements and advanced features will be added in future iterations.
