# Online Retail Data Analysis

## Project Overview

This project analyzes an Online Retail dataset to identify sales trends,
top-performing products, customer behavior, and geographical revenue patterns.

The project demonstrates an end-to-end data analysis workflow using Python,
Pandas, Matplotlib, and Seaborn, including data acquisition, data cleaning,
exploratory data analysis, visualization, and business insights.

---

## Objectives

- Clean and validate the retail dataset
- Remove duplicate and invalid transactions
- Handle missing and inconsistent data
- Calculate transaction-level revenue
- Analyze monthly revenue trends
- Identify top-performing products
- Analyze revenue by country
- Identify high-value customers
- Analyze relationships between quantity, price, and revenue
- Create business-focused visualizations
- Generate actionable business recommendations

---

## Dataset

The project uses the Online Retail dataset containing transaction-level
information for an online retail business.

The original dataset contains **541,909 rows and 8 columns**.

### Dataset Columns

- `InvoiceNo` — Invoice number
- `StockCode` — Product stock code
- `Description` — Product description
- `Quantity` — Number of items purchased
- `InvoiceDate` — Date and time of the transaction
- `UnitPrice` — Price per item
- `CustomerID` — Customer identifier
- `Country` — Customer country

A derived `Revenue` column was created using:

```text
Revenue = Quantity × UnitPrice
```

### Project Structure

YuvaIntern_Week1_OnlineRetail/
│
├── data/
│   ├── Online Retail.xlsx
│   └── cleaned_online_retail.csv
│
├── notebooks/
│
├── report/
│   └── final_report.md
│
├── src/
│   └── analysis.py
│
├── visualizations/
│   ├── 01_missing_values_before_cleaning.png
│   ├── 02_monthly_revenue_trend.png
│   ├── 03_top_10_countries_revenue.png
│   ├── 04_revenue_vs_quantity.png
│   ├── 05_correlation_heatmap.png
│   └── 06_revenue_distribution.png
│
├── README.md
└── requirements.txt