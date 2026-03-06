print("Market Data Analyzer")

import requests
import sqlite3

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

response = requests.get(url)
data = response.json()

print(data)

conn = sqlite3.connect("prices.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prices (
    asset TEXT,
    price REAL
)
""")

price = data["bitcoin"]["usd"]

cursor.execute(
    "INSERT INTO prices (asset, price) VALUES (?, ?)",
    ("bitcoin", price)
)

conn.commit()

cursor.execute("SELECT * FROM prices")

rows = cursor.fetchall()

print("Stored prices:")
for row in rows:
    print(row)
    
conn.close()