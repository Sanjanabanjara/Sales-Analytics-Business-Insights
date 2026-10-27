import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
from pathlib import Path

dataset_path = Path(__file__).resolve().parent.parent / "dataset" / "sales_analytics_dataset.csv"
df = pd.read_csv(dataset_path)
# Display the first five records
print(df.head())

# Display the number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display all column names
print("\nColumn Names:")
print(df.columns.tolist())

# =====================================
# SALES DATA ANALYSIS
# =====================================

print("\n========== SALES BUSINESS INSIGHTS ==========")

# 1. Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", round(total_sales, 2))

# 2. Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", round(total_profit, 2))

# 3. Total Orders
total_orders = df["Order_ID"].nunique()
print("Total Orders:", total_orders)

# 4. Total Quantity Sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# 5. Best-Selling Product by Quantity
best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)
print("Best-Selling Product:", best_product)

# 6. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(
    ascending=False
)
print("\nSales by Region:")
print(region_sales)

# 7. Profit by Category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(
    ascending=False
)
print("\nProfit by Category:")
print(category_profit)

# =====================================
# MONTHLY SALES ANALYSIS
# =====================================

print("\n========== MONTHLY SALES ANALYSIS ==========")

# Convert Order_Date into datetime format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Group sales by month
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()

print("\nMonthly Sales:")
print(monthly_sales.round(2))

# Find the month with highest sales
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print("\nMonth with Highest Sales:", best_month)
print("Highest Monthly Sales:", round(highest_sales, 2))

# Find the month with lowest sales
lowest_month = monthly_sales.idxmin()
lowest_sales = monthly_sales.min()

print("\nMonth with Lowest Sales:", lowest_month)
print("Lowest Monthly Sales:", round(lowest_sales, 2))



# =====================================
# MONTHLY SALES CHART
# =====================================

# Convert monthly index into strings
months = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    months,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Analysis - 2025")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

# =====================================
# PRODUCT-WISE SALES ANALYSIS
# =====================================

print("\n========== PRODUCT-WISE SALES ==========")

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Product:")
print(product_sales.round(2))

print("\nHighest Revenue Product:", product_sales.idxmax())
print("Highest Product Sales:", round(product_sales.max(), 2))

# Create product sales chart
plt.figure(figsize=(12, 6))

product_sales.plot(kind="bar")

plt.title("Product-wise Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# =====================================
# REGION-WISE SALES ANALYSIS
# =====================================

print("\n========== REGION-WISE ANALYSIS ==========")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Region:")
print(region_sales.round(2))

print("\nHighest Sales Region:", region_sales.idxmax())
print("Highest Region Sales:", round(region_sales.max(), 2))

print("\nLowest Sales Region:", region_sales.idxmin())
print("Lowest Region Sales:", round(region_sales.min(), 2))

# Create region-wise sales chart
plt.figure(figsize=(9, 5))

region_sales.plot(kind="bar")

plt.title("Region-wise Sales Analysis")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
