
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("sales_analytics.db")

# SQL Query 1: Display first 5 records
query = """
SELECT *
FROM sales
LIMIT 5;
"""

result = pd.read_sql_query(query, conn)

print("FIRST 5 SALES RECORDS:")
print(result.to_string(index=False))


# SQL Query 2: Filter Electronics products

query2 = """
SELECT Order_ID, Product, Category, Sales
FROM sales
WHERE Category = 'Electronics'
LIMIT 10;
"""

result2 = pd.read_sql_query(query2, conn)

print("\nELECTRONICS PRODUCTS:")
print(result2.to_string(index=False))


# SQL Query 3: Total Sales, Profit and Orders

query3 = """
SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM sales;
"""

result3 = pd.read_sql_query(query3, conn)

print("\n========== SALES SUMMARY ==========")
print(result3.to_string(index=False))


# =====================================
# SQL QUERY 4: REGION-WISE SALES
# =====================================

query4 = """
SELECT
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

result4 = pd.read_sql_query(query4, conn)

print("\n========== REGION-WISE SALES ==========")
print(result4.to_string(index=False))


# =====================================
# SQL QUERY 5: CATEGORY-WISE PROFIT
# =====================================

query5 = """
SELECT
    Category,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;
"""

result5 = pd.read_sql_query(query5, conn)

print("\n========== CATEGORY-WISE PROFIT ==========")
print(result5.to_string(index=False))


# =====================================
# SQL QUERY 6: HAVING CLAUSE
# =====================================

query6 = """
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Category
HAVING SUM(Profit) > 50000
ORDER BY Total_Profit DESC;
"""

result6 = pd.read_sql_query(query6, conn)

print("\n========== CATEGORIES WITH PROFIT ABOVE 50000 ==========")
print(result6.to_string(index=False))


# =====================================
# SQL QUERY 7: MONTHLY SALES ANALYSIS
# =====================================

query7 = """
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY strftime('%Y-%m', Order_Date)
ORDER BY Month ASC;
"""

result7 = pd.read_sql_query(query7, conn)

print("\n========== MONTHLY SALES ANALYSIS ==========")
print(result7.to_string(index=False))


# =====================================
# SQL QUERY 9: TOP 5 PRODUCTS
# =====================================

query9 = """
SELECT
    Product,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 5;
"""

result9 = pd.read_sql_query(query9, conn)

print("\n========== TOP 5 PRODUCTS ==========")
print(result9.to_string(index=False))


# =====================================
# SQL QUERY 10: SALES CHANNEL ANALYSIS
# =====================================

query10 = """
SELECT
    Sales_Channel,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Sales_Channel
ORDER BY Total_Sales DESC;
"""

result10 = pd.read_sql_query(query10, conn)

print("\n========== SALES CHANNEL ANALYSIS ==========")
print(result10.to_string(index=False))


# =====================================
# SQL QUERY 11: PAYMENT METHOD ANALYSIS
# =====================================

query11 = """
SELECT
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales
GROUP BY Payment_Method
ORDER BY Total_Orders DESC;
"""

result11 = pd.read_sql_query(query11, conn)

print("\n========== PAYMENT METHOD ANALYSIS ==========")
print(result11.to_string(index=False))


# =====================================
# SQL QUERY 12: PROFIT MARGIN ANALYSIS
# =====================================

query12 = """
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(
        SUM(Profit) * 100.0 / NULLIF(SUM(Sales), 0),
        2
    ) AS Profit_Margin_Percent
FROM sales
GROUP BY Category
ORDER BY Profit_Margin_Percent DESC;
"""

result12 = pd.read_sql_query(query12, conn)

print("\n========== CATEGORY PROFIT MARGIN ==========")
print(result12.to_string(index=False))


# Close connection
conn.close()


