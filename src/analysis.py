# ============================================================
# WEEK 1 - ONLINE RETAIL DATA ANALYSIS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
VIS_DIR = BASE_DIR / "visualizations"

INPUT_FILE = DATA_DIR / "Online Retail.xlsx"
OUTPUT_FILE = DATA_DIR / "cleaned_online_retail.csv"

VIS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("=" * 70)
print("STEP 1 - DATA ACQUISITION")
print("=" * 70)

df = pd.read_excel(INPUT_FILE)

print(f"Dataset loaded successfully from: {INPUT_FILE}")
print(f"Original rows: {len(df):,}")
print(f"Original columns: {len(df.columns)}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 3. INITIAL DATASET INSPECTION
# ============================================================

print("\n" + "=" * 70)
print("STEP 2 - INITIAL DATASET INSPECTION")
print("=" * 70)

print("\nDataset information:")
print(df.info())

print("\nInitial data types:")
print(df.dtypes)

print("\nInitial missing values:")
print(df.isnull().sum())

print("\nInitial descriptive statistics:")
print(df.describe(include="all"))


# ============================================================
# 4. CREATE CLEANING COPY
# ============================================================

print("\n" + "=" * 70)
print("STEP 3 - CREATE CLEANING COPY")
print("=" * 70)

cleaned_df = df.copy()

print("A copy of the original dataset was created for cleaning.")
print("The original dataset remains unchanged.")


# ============================================================
# 4.1 DUPLICATE REMOVAL
# ============================================================

print("\n" + "=" * 70)
print("4.1 - DUPLICATE REMOVAL")
print("=" * 70)

duplicates = cleaned_df.duplicated().sum()

print(f"Duplicate rows found: {duplicates:,}")

cleaned_df = cleaned_df.drop_duplicates()

print(f"Rows after removing duplicates: {len(cleaned_df):,}")


# ============================================================
# 4.2 DATA TYPE CORRECTION
# ============================================================

print("\n" + "=" * 70)
print("4.2 - DATA TYPE CORRECTION")
print("=" * 70)

cleaned_df["InvoiceNo"] = cleaned_df["InvoiceNo"].astype("string")
cleaned_df["StockCode"] = cleaned_df["StockCode"].astype("string")
cleaned_df["Description"] = cleaned_df["Description"].astype("string")

cleaned_df["InvoiceDate"] = pd.to_datetime(
    cleaned_df["InvoiceDate"],
    errors="coerce"
)

cleaned_df["Quantity"] = pd.to_numeric(
    cleaned_df["Quantity"],
    errors="coerce"
).astype("Int64")

cleaned_df["UnitPrice"] = pd.to_numeric(
    cleaned_df["UnitPrice"],
    errors="coerce"
)

cleaned_df["CustomerID"] = pd.to_numeric(
    cleaned_df["CustomerID"],
    errors="coerce"
).astype("Int64")

cleaned_df["Country"] = cleaned_df["Country"].astype("string")

print("Data types corrected successfully.")

print("\nData types after correction:")
print(cleaned_df.dtypes)


# ============================================================
# 4.3 MISSING DESCRIPTION HANDLING
# ============================================================

print("\n" + "=" * 70)
print("4.3 - MISSING DESCRIPTION HANDLING")
print("=" * 70)

missing_description = cleaned_df["Description"].isna().sum()

print(
    f"Missing Description rows before handling: "
    f"{missing_description:,}"
)

cleaned_df = cleaned_df.dropna(subset=["Description"])

print(
    f"Rows remaining after removing missing descriptions: "
    f"{len(cleaned_df):,}"
)


# ============================================================
# 4.4 CANCELLED INVOICE IDENTIFICATION
# ============================================================

print("\n" + "=" * 70)
print("4.4 - CANCELLED INVOICE IDENTIFICATION")
print("=" * 70)

cancelled_rows = cleaned_df["InvoiceNo"].str.startswith(
    "C",
    na=False
).sum()

print(
    f"Cancelled invoice rows identified: "
    f"{cancelled_rows:,}"
)


# ============================================================
# 4.5 INVALID QUANTITY AND PRICE CHECK
# ============================================================

print("\n" + "=" * 70)
print("4.5 - INVALID QUANTITY AND PRICE CHECK")
print("=" * 70)

negative_quantity = (cleaned_df["Quantity"] < 0).sum()
zero_quantity = (cleaned_df["Quantity"] == 0).sum()

invalid_price = (
    cleaned_df["UnitPrice"].isna()
    | (cleaned_df["UnitPrice"] <= 0)
).sum()

print(f"Negative quantity rows: {negative_quantity:,}")
print(f"Zero quantity rows: {zero_quantity:,}")
print(f"Invalid/zero price rows: {invalid_price:,}")


# ============================================================
# 4.6 FILTER VALID SALES TRANSACTIONS
# ============================================================

print("\n" + "=" * 70)
print("4.6 - FILTER VALID SALES TRANSACTIONS")
print("=" * 70)

cleaned_df = cleaned_df[
    (~cleaned_df["InvoiceNo"].str.startswith("C", na=False))
    & (cleaned_df["Quantity"] > 0)
    & (cleaned_df["UnitPrice"] > 0)
    & (cleaned_df["InvoiceDate"].notna())
].copy()

print(
    f"Valid sales rows remaining: "
    f"{len(cleaned_df):,}"
)


# ============================================================
# 4.7 CUSTOMER ID CHECK
# ============================================================

print("\n" + "=" * 70)
print("4.7 - CUSTOMER ID CHECK")
print("=" * 70)

missing_customer_id = cleaned_df["CustomerID"].isna().sum()

missing_customer_percentage = (
    missing_customer_id / len(cleaned_df)
) * 100

print(
    f"Missing CustomerID in valid sales data: "
    f"{missing_customer_id:,}"
)

print(
    f"Percentage of valid sales with missing CustomerID: "
    f"{missing_customer_percentage:.2f}%"
)

print(
    "\nDecision: Missing CustomerID values were retained because "
    "CustomerID is not required to calculate transaction-level revenue."
)


# ============================================================
# 4.8 CREATE REVENUE COLUMN
# ============================================================

print("\n" + "=" * 70)
print("4.8 - CREATE REVENUE COLUMN")
print("=" * 70)

cleaned_df["Revenue"] = (
    cleaned_df["Quantity"] * cleaned_df["UnitPrice"]
)

total_revenue = cleaned_df["Revenue"].sum()

print("Revenue column created successfully.")

print(
    f"Total Revenue calculated: "
    f"£{total_revenue:,.2f}"
)


# ============================================================
# 4.9 FINAL DATA TYPE VERIFICATION
# ============================================================

print("\n" + "=" * 70)
print("4.9 - FINAL DATA TYPE VERIFICATION")
print("=" * 70)

print(cleaned_df.dtypes)


# ============================================================
# 4.10 FINAL DATA QUALITY CHECK
# ============================================================

print("\n" + "=" * 70)
print("4.10 - FINAL DATA QUALITY CHECK")
print("=" * 70)

print(
    f"Remaining duplicate rows: "
    f"{cleaned_df.duplicated().sum():,}"
)

print(
    f"Remaining negative quantities: "
    f"{(cleaned_df['Quantity'] < 0).sum():,}"
)

print(
    f"Remaining invalid prices: "
    f"{(cleaned_df['UnitPrice'] <= 0).sum():,}"
)

print(
    f"Remaining missing descriptions: "
    f"{cleaned_df['Description'].isna().sum():,}"
)

print(
    f"Remaining missing InvoiceDate values: "
    f"{cleaned_df['InvoiceDate'].isna().sum():,}"
)


# ============================================================
# 5. CLEANED DATASET SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("STEP 5 - CLEANED DATASET SUMMARY")
print("=" * 70)

original_rows = len(df)
cleaned_rows = len(cleaned_df)
rows_removed = original_rows - cleaned_rows

print(f"Original rows: {original_rows:,}")
print(f"Cleaned sales rows: {cleaned_rows:,}")
print(f"Rows removed: {rows_removed:,}")
print(f"Columns: {len(cleaned_df.columns)}")

print("\nFinal columns:")
print(cleaned_df.columns.tolist())


# ============================================================
# 6. EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 6 - EXPLORATORY DATA ANALYSIS")
print("=" * 70)


# ============================================================
# 6.1 CREATE YEAR-MONTH COLUMN
# ============================================================

cleaned_df["YearMonth"] = (
    cleaned_df["InvoiceDate"]
    .dt.to_period("M")
)


# ============================================================
# 6.2 KEY BUSINESS METRICS
# ============================================================

print("\n" + "=" * 70)
print("6.2 - KEY BUSINESS METRICS")
print("=" * 70)

total_revenue = cleaned_df["Revenue"].sum()

total_quantity = cleaned_df["Quantity"].sum()

total_orders = cleaned_df["InvoiceNo"].nunique()

unique_products = cleaned_df["StockCode"].nunique()

unique_customers = cleaned_df["CustomerID"].nunique()

average_order_value = (
    cleaned_df.groupby("InvoiceNo")["Revenue"]
    .sum()
    .mean()
)

print(f"Total Revenue: £{total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Unique Products: {unique_products:,}")
print(f"Unique Customers: {unique_customers:,}")
print(f"Average Order Value: £{average_order_value:,.2f}")


# ============================================================
# 6.3 MONTHLY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("6.3 - MONTHLY REVENUE")
print("=" * 70)

monthly_revenue = (
    cleaned_df.groupby("YearMonth")["Revenue"]
    .sum()
)

print(monthly_revenue)

highest_month = monthly_revenue.idxmax()
highest_month_revenue = monthly_revenue.max()

lowest_month = monthly_revenue.idxmin()
lowest_month_revenue = monthly_revenue.min()

print(
    f"\nHighest revenue month: {highest_month}"
)

print(
    f"Highest monthly revenue: "
    f"£{highest_month_revenue:,.2f}"
)

print(
    f"\nLowest revenue month: {lowest_month}"
)

print(
    f"Lowest monthly revenue: "
    f"£{lowest_month_revenue:,.2f}"
)


# ============================================================
# 6.4 TOP 10 PRODUCTS BY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("6.4 - TOP 10 PRODUCTS BY REVENUE")
print("=" * 70)

top_products_revenue = (
    cleaned_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products_revenue)


# ============================================================
# 6.5 TOP 10 PRODUCTS BY QUANTITY SOLD
# ============================================================

print("\n" + "=" * 70)
print("6.5 - TOP 10 PRODUCTS BY QUANTITY SOLD")
print("=" * 70)

top_products_quantity = (
    cleaned_df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products_quantity)


# ============================================================
# 6.6 TOP 10 COUNTRIES BY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("6.6 - TOP 10 COUNTRIES BY REVENUE")
print("=" * 70)

top_countries_revenue = (
    cleaned_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_countries_revenue)


# ============================================================
# 6.7 TOP 10 CUSTOMERS BY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("6.7 - TOP 10 CUSTOMERS BY REVENUE")
print("=" * 70)

top_customers_revenue = (
    cleaned_df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers_revenue)


# ============================================================
# 6.8 REVENUE DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("6.8 - REVENUE DISTRIBUTION")
print("=" * 70)

print(
    cleaned_df["Revenue"].describe()
)


# ============================================================
# 6.9 TOP 10 TRANSACTIONS BY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("6.9 - TOP 10 TRANSACTIONS BY REVENUE")
print("=" * 70)

top_transactions = (
    cleaned_df[
        [
            "InvoiceNo",
            "Description",
            "Quantity",
            "UnitPrice",
            "Revenue",
            "Country"
        ]
    ]
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print(top_transactions.to_string(index=False))


# ============================================================
# 6.10 NUMERICAL CORRELATION
# ============================================================

print("\n" + "=" * 70)
print("6.10 - NUMERICAL CORRELATION")
print("=" * 70)

correlation = cleaned_df[
    ["Quantity", "UnitPrice", "Revenue"]
].corr()

print(correlation)


# ============================================================
# 7. DATA VISUALIZATIONS
# ============================================================

print("\n" + "=" * 70)
print("STEP 7 - DATA VISUALIZATIONS")
print("=" * 70)


# ============================================================
# 7.1 MISSING VALUES BEFORE CLEANING
# ============================================================

print("Creating missing values visualization...")

missing_values = df.isnull().sum()

missing_values = missing_values[
    missing_values > 0
].sort_values(ascending=True)

plt.figure(figsize=(10, 6))

plt.barh(
    missing_values.index,
    missing_values.values
)

plt.title(
    "Missing Values Before Data Cleaning",
    fontsize=16
)

plt.xlabel("Number of Missing Values")
plt.ylabel("Column")

plt.tight_layout()

plt.savefig(
    VIS_DIR / "01_missing_values_before_cleaning.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 7.2 MONTHLY REVENUE TREND
# ============================================================

print("Creating monthly revenue trend visualization...")

plt.figure(figsize=(12, 7))

x_labels = monthly_revenue.index.astype(str)

plt.plot(
    x_labels,
    monthly_revenue.values,
    marker="o",
    linewidth=2
)

plt.title(
    "Monthly Revenue Trend",
    fontsize=16
)

plt.xlabel("Month")
plt.ylabel("Revenue (£)")

plt.xticks(rotation=45)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    VIS_DIR / "02_monthly_revenue_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 7.3 TOP 10 COUNTRIES BY REVENUE
# ============================================================

print("Creating top countries revenue visualization...")

country_plot = top_countries_revenue.sort_values()

plt.figure(figsize=(11, 7))

plt.barh(
    country_plot.index,
    country_plot.values
)

plt.title(
    "Top 10 Countries by Revenue",
    fontsize=16
)

plt.xlabel("Revenue (£)")
plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    VIS_DIR / "03_top_10_countries_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 7.4 REVENUE VS QUANTITY
# ============================================================

print("Creating revenue vs quantity visualization...")

plt.figure(figsize=(11, 7))

plt.scatter(
    cleaned_df["Quantity"],
    cleaned_df["Revenue"],
    alpha=0.25,
    s=20
)

plt.title(
    "Revenue vs Quantity Sold",
    fontsize=16
)

plt.xlabel("Quantity Sold")
plt.ylabel("Revenue (£)")

plt.grid(
    alpha=0.2
)

plt.tight_layout()

plt.savefig(
    VIS_DIR / "04_revenue_vs_quantity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 7.5 CORRELATION HEATMAP
# ============================================================

print("Creating correlation heatmap...")

plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    square=True
)

plt.title(
    "Correlation Heatmap",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    VIS_DIR / "05_correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 7.6 REVENUE DISTRIBUTION
# ============================================================

print("Creating revenue distribution visualization...")

plt.figure(figsize=(11, 7))

plt.hist(
    cleaned_df["Revenue"],
    bins=100
)

plt.title(
    "Distribution of Transaction Revenue",
    fontsize=16
)

plt.xlabel("Revenue (£)")
plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    VIS_DIR / "06_revenue_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# 8. AFTER-CLEANING MISSING VALUE CHECK
# ============================================================

print("\n" + "=" * 70)
print("STEP 8 - AFTER-CLEANING MISSING VALUE CHECK")
print("=" * 70)

remaining_missing = (
    cleaned_df.isnull()
    .sum()
)

remaining_missing = remaining_missing[
    remaining_missing > 0
]

print(
    "Remaining missing values after cleaning:"
)

print(remaining_missing)


# ============================================================
# 9. SAVE CLEANED DATASET
# ============================================================

print("\n" + "=" * 70)
print("STEP 9 - SAVE CLEANED DATASET")
print("=" * 70)

# Remove helper column before saving
final_output_df = cleaned_df.drop(
    columns=["YearMonth"]
)

final_output_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(
    "Cleaned dataset saved successfully:"
)

print(OUTPUT_FILE)


# ============================================================
# 10. WEEK 1 PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("WEEK 1 PROJECT SUMMARY")
print("=" * 70)

print(
    f"Original dataset rows: "
    f"{original_rows:,}"
)

print(
    f"Final cleaned sales rows: "
    f"{cleaned_rows:,}"
)

print(
    f"Rows removed: "
    f"{rows_removed:,}"
)

print(
    f"Total Revenue: "
    f"£{total_revenue:,.2f}"
)

print(
    f"Total Quantity Sold: "
    f"{total_quantity:,}"
)

print(
    f"Total Orders: "
    f"{total_orders:,}"
)

print(
    f"Unique Products: "
    f"{unique_products:,}"
)

print(
    f"Unique Customers: "
    f"{unique_customers:,}"
)

print(
    f"Average Order Value: "
    f"£{average_order_value:,.2f}"
)

print(
    f"Highest Revenue Month: "
    f"{highest_month}"
)

print(
    f"Highest Monthly Revenue: "
    f"£{highest_month_revenue:,.2f}"
)


# ============================================================
# 11. VISUALIZATION FILES
# ============================================================

print("\nVisualization files created:")

print("1. 01_missing_values_before_cleaning.png")
print("2. 02_monthly_revenue_trend.png")
print("3. 03_top_10_countries_revenue.png")
print("4. 04_revenue_vs_quantity.png")
print("5. 05_correlation_heatmap.png")
print("6. 06_revenue_distribution.png")

print("\nAll visualizations are saved in:")
print(VIS_DIR)


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 70)
print("WEEK 1 ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)