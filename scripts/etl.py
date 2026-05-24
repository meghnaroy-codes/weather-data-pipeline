import psycopg2

# CONFIG
DB_CONFIG = {
    "host": "localhost",
    "database": "weather_pipeline",
    "user": "postgres",
    "password": "postgres123"
}

CSV_FILE = "C:/Users/Meghna/OneDrive/Desktop/projects/weather-data-pipeline/weather_data.csv"   # change if needed


def load_data():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        print("Connected to database")

        # Clean table before load (IMPORTANT for duplicates)
        cur.execute("TRUNCATE TABLE weather_data;")
        conn.commit()

        print("Table cleared")

        # Bulk load using COPY
        with open(CSV_FILE, 'r') as f:
            next(f)  # skip header

            cur.copy_expert("""
                COPY weather_data(city, temperature, humidity, timestamp)
                FROM STDIN WITH CSV
            """, f)

        conn.commit()

        print("Data loaded successfully using COPY!")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            cur.close()
            conn.close()
            print("Connection closed")


if __name__ == "__main__":
    load_data()