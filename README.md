# Task-7
Making the 7th task for the internship in data analytics in Elevate Labs

Steps I followed:

 Load SQLite database: import sqlite3 conn = sqlite3.connect("sales_data.db")
 Run basic SQL: query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS
 revenue FROM sales GROUP BY product"
 Load into pandas: import pandas as pd df = pd.read_sql_query(query, conn)
 Print results: print(df)
 Plot simple bar chart: df.plot(kind='bar', x='product', y='revenue')
 Save chart if needed: plt.savefig("sales_chart.png"
