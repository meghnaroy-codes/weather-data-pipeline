import requests
import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="weatherdb",
    user="admin",
    password="admin",
    port=5432
)

cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    windspeed FLOAT,
    time TEXT
)
""")

# fetch weather data
url = "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"
response = requests.get(url)
data = response.json()

weather = data["current_weather"]

# insert into DB
cur.execute("""
INSERT INTO weather (temperature, windspeed, time)
VALUES (%s, %s, %s)
""", (
    weather["temperature"],
    weather["windspeed"],
    weather["time"]
))

conn.commit()

print("Data inserted successfully!")

cur.close()
conn.close()