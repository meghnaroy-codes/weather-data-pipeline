import random
import pandas as pd
from faker import Faker
from datetime import datetime

fake = Faker()

data = []

for _ in range(1000000):
    weather_record = {
        "city": fake.city(),
        "temperature": round(random.uniform(10, 45), 2),
        "humidity": random.randint(20, 100),
        "timestamp": fake.date_time_between(
            start_date='-30d',
            end_date='now'
        )
    }

    data.append(weather_record)

df = pd.DataFrame(data)

df.to_csv("weather_data.csv", index=False)

print("100,000 weather records generated successfully!")