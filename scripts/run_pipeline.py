from extract import extract_data
from transform import transform_data
from load import load_data

file_path = "weather_data.csv"

df = extract_data(file_path)
df = transform_data(df)
load_data(df)