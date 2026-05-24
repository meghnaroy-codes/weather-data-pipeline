import psycopg2
from config.config import DB_CONFIG, CSV_PATH
from etl.logger import log_info, log_error

def load_data():
    conn = None

    try:
        log_info("Connecting to database...")
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        log_info("Connection successful")

        # Safety: ensure clean load
        log_info("Clearing table...")
        cur.execute("TRUNCATE TABLE weather_data;")
        conn.commit()

        log_info("Table cleared")

        # Validate file exists
        log_info(f"Loading file: {CSV_PATH}")

        with open(CSV_PATH, "r") as f:
            header = next(f)

            cur.copy_expert("""
                COPY weather_data(city, temperature, humidity, timestamp)
                FROM STDIN WITH CSV
            """, f)

        conn.commit()
        log_info("Data loaded successfully")

    except Exception as e:
        log_error(f"ETL failed: {str(e)}")
        if conn:
            conn.rollback()

    finally:
        if conn:
            cur.close()
            conn.close()
            log_info("Database connection closed")