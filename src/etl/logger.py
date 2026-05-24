import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_file = f"{LOG_DIR}/etl_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    print(message)
    logging.info(message)

def log_error(message):
    print(message)
    logging.error(message)