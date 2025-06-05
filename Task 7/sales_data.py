import sqlite3


conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')


data = [
    ('Chocolate', 10, 2.5),
    ('Candy', 20, 1.0),
    ('Cookie', 15, 1.5),
    ('Chocolate', 5, 2.5),
    ('Candy', 10, 1.0)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', data)
conn.commit()
conn.close()
