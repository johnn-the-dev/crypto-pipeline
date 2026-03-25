import os
import requests
import psycopg2
import datetime
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices (
        coin_name TEXT,
        price REAL,
        volume REAL,
        timestamp TEXT
    )
""")

url = "https://api.coingecko.com/api/v3/simple/price"
parametres = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd",
    "include_24hr_change": "true",
    "include_24hr_vol": "true"
}

response = requests.get(url, params=parametres)
if response.status_code == 200:
    print("OK")
    content = response.json()

    for coin_name, values in content.items():
        price = values.get("usd", 0.0)
        volume = values.get("usd_24h_vol", 0.0)
        timestamp = str(datetime.datetime.now())

        cursor.execute("INSERT INTO crypto_prices VALUES (%s, %s, %s, %s)", (coin_name, price, volume, timestamp))

    connection.commit()
    connection.close()
else:
    print("not ok")

