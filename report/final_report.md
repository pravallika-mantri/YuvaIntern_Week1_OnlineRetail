# Online Retail Data Analysis Report

## 1. Project Overview

This project analyzes an Online Retail dataset to understand sales performance,
customer behavior, product performance, and geographical revenue distribution.

The analysis includes data cleaning, exploratory data analysis, visualization,
and business insights.

---

## 2. Dataset Summary

- Original rows: 541,909
- Cleaned sales rows: 524,878
- Rows removed: 17,031
- Original columns: 8
- Final columns: 9

A Revenue column was created to calculate transaction-level sales value.

---

## 3. Data Cleaning

The following data-quality issues were addressed:

- Duplicate transactions were removed.
- Transactions with missing product descriptions were removed.
- Cancelled invoices were excluded from valid sales analysis.
- Negative quantities were removed.
- Invalid unit prices were removed.
- Date fields were converted to the appropriate datetime format.
- Revenue was calculated using Quantity × UnitPrice.
- Customer IDs were checked for missing values.

Final quality checks confirmed:

- Remaining duplicate rows: 0
- Remaining negative quantities: 0
- Remaining invalid prices: 0
- Remaining missing descriptions: 0

---

## 4. Key Business Metrics

| Metric | Value |
|---|---:|
| Total Revenue | £10,642,110.80 |
| Total Quantity Sold | 5,572,420 |
| Total Orders | 19,960 |
| Unique Products | 3,922 |
| Unique Customers | 4,338 |
| Average Order Value | £533.17 |

---

## 5. Revenue Trend

The highest revenue month was:

**November 2011 — £1,503,866.78**

Monthly revenue analysis shows noticeable variation in sales performance
throughout the available period.

This indicates that sales are influenced by seasonal or time-based purchasing
patterns.

---

## 6. Top Products

### Top Products by Revenue

1. DOTCOM POSTAGE
2. REGENCY CAKESTAND 3 TIER
3. PAPER CRAFT , LITTLE BIRDIE
4. WHITE HANGING HEART T-LIGHT HOLDER
5. PARTY BUNTING
6. JUMBO BAG RED RETROSPOT
7. MEDIUM CERAMIC TOP STORAGE JAR
8. POSTAGE
9. Manual
10. RABBIT NIGHT LIGHT

### Top Products by Quantity Sold

1. PAPER CRAFT , LITTLE BIRDIE
2. MEDIUM CERAMIC TOP STORAGE JAR
3. WORLD WAR 2 GLIDERS ASSTD DESIGNS
4. JUMBO BAG RED RETROSPOT
5. WHITE HANGING HEART T-LIGHT HOLDER
6. POPCORN HOLDER
7. PACK OF 72 RETROSPOT CAKE CASES
8. ASSORTED COLOUR BIRD ORNAMENT
9. RABBIT NIGHT LIGHT
10. MINI PAINT SET VINTAGE

The results show that products with high sales volume are not necessarily
the same products generating the highest revenue.

---

## 7. Geographical Performance

The United Kingdom generated the highest revenue by a significant margin.

Top countries by revenue include:

- United Kingdom
- Netherlands
- EIRE
- Germany
- France
- Australia
- Spain
- Switzerland
- Belgium
- Sweden

The UK is the company's dominant market, while several European markets
represent potential opportunities for further growth.

---

## 8. Customer Analysis

The dataset contains:

**4,338 unique customers**

The highest-revenue customers contribute substantially to overall sales,
indicating that customer-level purchasing behavior should be considered
when developing retention and loyalty strategies.

---

## 9. Key Business Insights

### Insight 1 — UK is the dominant market

The United Kingdom generated approximately £9.00 million in revenue,
making it by far the largest market.

### Insight 2 — Revenue is concentrated

A relatively small number of products and customers generate a substantial
portion of total revenue.

### Insight 3 — High quantity does not always mean high revenue

Some products sell in very large quantities but do not necessarily rank
highest by revenue.

### Insight 4 — November was the strongest month

November 2011 recorded the highest monthly revenue at approximately
£1.50 million.

### Insight 5 — International markets provide growth opportunities

Countries such as the Netherlands, EIRE, Germany, and France generated
meaningful revenue and could be targeted for international expansion.

---

## 10. Business Recommendations

### 1. Focus on high-value customers

Develop loyalty programs, personalized offers, and retention campaigns
for customers contributing significant revenue.

### 2. Promote high-performing products

Use the highest-revenue products in promotional campaigns and
cross-selling strategies.

### 3. Investigate seasonal demand

Analyze the factors behind the strong November performance and prepare
inventory and marketing campaigns ahead of peak periods.

### 4. Expand international sales

Investigate customer preferences and purchasing behavior in strong
international markets such as the Netherlands, EIRE, Germany, and France.

### 5. Optimize product portfolio

Compare product quantity, revenue, and profitability to identify products
that have high demand but relatively low revenue.

---

## 11. Visualizations

The following visualizations were created:

1. Missing Values Analysis
2. Monthly Revenue Trend
3. Top 10 Countries by Revenue
4. Revenue vs Quantity Correlation

These visualizations help communicate the major patterns identified
during exploratory data analysis.

---

## 12. Conclusion

The analysis provides a clear overview of the company's online retail
performance.

The business generated more than £10.6 million in revenue from over
524,000 cleaned sales transactions. The United Kingdom was the dominant
market, while November 2011 recorded the highest monthly revenue.

Product-level and customer-level analysis shows opportunities to improve
customer retention, optimize product promotion, and expand sales in
international markets.

Overall, the analysis demonstrates how data cleaning, exploratory analysis,
and visualization can be used to generate actionable business insights.