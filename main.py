print("Market Data Analyzer")

import requests
import sqlite3
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

response = requests.get(url)
data = response.json()

print(data)

conn = sqlite3.connect("prices.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prices (
    asset TEXT,
    price REAL,
    timestamp TEXT
)
""")

cursor.execute("PRAGMA table_info(prices)")
columns = [column[1] for column in cursor.fetchall()]

if "timestamp" not in columns:
    cursor.execute("ALTER TABLE prices ADD COLUMN timestamp TEXT")

price = data["bitcoin"]["usd"]
timestamp = datetime.now().isoformat()

cursor.execute(
    "INSERT INTO prices (asset, price, timestamp) VALUES (?, ?, ?)",
    ("bitcoin", price, timestamp)
)

conn.commit()

cursor.execute("SELECT * FROM prices")
rows = cursor.fetchall()

print("Stored prices:")
for row in rows:
    print(row)

conn.close()