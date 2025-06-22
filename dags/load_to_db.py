import sqlite3
import pandas as pd
import os

def load_to_sqlite(file_path="data/Mumbai_weather.csv", db_file="weather.db"):
    try:
        df = pd.read_csv(file_path)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT,
                timestamp TEXT,
                temperature REAL,
                humidity INTEGER,
                description TEXT
            );
        """)

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO weather_data (city, timestamp, temperature, humidity, description)
                VALUES (?, ?, ?, ?, ?);
            """, (row.city, row.timestamp, row.temperature, row.humidity, row.description))

        conn.commit()
        conn.close()
        print("✅ Data loaded into SQLite.")

    except Exception as e:
        print(f"❌ Failed: {e}")
