import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect("/content/database.sqlite")  # Update with correct path if needed

# Query 1: Monthly Sales Revenue
monthly_sales_query = """
SELECT strftime('%Y-%m', order_purchase_timestamp) AS month, SUM(payment_value) AS total_revenue
FROM orders o
JOIN order_payments op ON o.order_id = op.order_id
WHERE order_status = 'delivered'
GROUP BY month
ORDER BY month;
"""
monthly_sales = pd.read_sql_query(monthly_sales_query, conn)

# Query 2: Top 10 Best-Selling Products
top_products_query = """
SELECT p.product_category_name, COUNT(oi.product_id) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY total_sold DESC
LIMIT 10;
"""
top_products = pd.read_sql_query(top_products_query, conn)

# Query 3: Payment Type Distribution
payment_type_query = """
SELECT payment_type, COUNT(*) AS count
FROM order_payments
GROUP BY payment_type;
"""
payment_type = pd.read_sql_query(payment_type_query, conn)

# Query 4: Orders by State
orders_by_state_query = """
SELECT s.seller_state, COUNT(o.order_id) AS total_orders
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN sellers s ON oi.seller_id = s.seller_id
WHERE order_status = 'delivered'
GROUP BY s.seller_state
ORDER BY total_orders DESC;
"""
orders_by_state = pd.read_sql_query(orders_by_state_query, conn)

# Close connection
conn.close()

# Plot 1: Monthly Sales Revenue
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x="month", y="total_revenue", marker="o", color="b")
plt.xticks(rotation=45)
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.show()

# Plot 2: Top 10 Best-Selling Products
plt.figure(figsize=(12, 6))
sns.barplot(data=top_products, x="total_sold", y="product_category_name", palette="viridis")
plt.title("Top 10 Best-Selling Product Categories")
plt.xlabel("Total Sold")
plt.ylabel("Product Category")
plt.show()

# Plot 3: Payment Type Distribution
plt.figure(figsize=(8, 6))
sns.barplot(data=payment_type, x="payment_type", y="count", palette="coolwarm")
plt.title("Distribution of Payment Types")
plt.xlabel("Payment Type")
plt.ylabel("Count")
plt.show()

# Plot 4: Orders by State
plt.figure(figsize=(12, 6))
sns.barplot(data=orders_by_state, x="total_orders", y="seller_state", palette="magma")
plt.title("Orders by State")
plt.xlabel("Total Orders")
plt.ylabel("State")
plt.show()
