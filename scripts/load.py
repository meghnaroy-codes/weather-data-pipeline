import psycopg2

def load_data(df):
    conn = psycopg2.connect(
        host="localhost",
        database="weather_pipeline",
        user="postgres",
        password="postgres123"
    )

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO weather_data (city, temperature, humidity, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (row["city"], row["temperature"], row["humidity"], row["timestamp"]))

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded into PostgreSQL")