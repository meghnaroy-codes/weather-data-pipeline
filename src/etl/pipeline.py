from etl.load import load_data
from etl.logger import log_info
import psycopg2
from config.config import DB_CONFIG

def validate_data():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM weather_data;")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    log_info(f"Row count after load: {count}")

    if count != 1000000:
        log_info("WARNING: Data count mismatch!")
    else:
        log_info("Validation successful ✔")

def run_pipeline():
    log_info("Starting ETL pipeline...")

    load_data()
    validate_data()

    log_info("ETL pipeline completed")

if __name__ == "__main__":
    run_pipeline()