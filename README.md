# 🌦️ Weather Data Pipeline (Beginner Data Engineering Project)
End-to-end data engineering pipeline using Python, Docker, and PostgreSQL

## 🚀 Overview

This project is a simple end-to-end **data engineering pipeline** that collects live weather data from an API, processes it using Python, and stores it in a PostgreSQL database running inside Docker.

You can then explore the data using SQL tools like DBeaver.

---

## 🎯 Project Goal

To simulate a real-world data engineering workflow:

- Extract data from a public API
- Transform and clean data using Python
- Load data into a PostgreSQL database
- Query and analyze data using SQL

---

## 🧱 Architecture

Weather API → Python ETL Script → PostgreSQL (Docker) → DBeaver

---

## 🛠️ Tech Stack

- Python 🐍
- PostgreSQL 🗄️
- Docker Desktop 🐳
- DBeaver 🧭
- Open-Meteo Weather API 🌦️
- VS Code 💻

---

## 📦 Features

- Fetches real-time weather data from API
- Extracts temperature, windspeed, and timestamp
- Stores structured data in PostgreSQL
- Supports SQL-based analysis
- Fully containerized database setup

---

## 🗂️ Database Schema

### Table: `weather`

| Column       | Type   | Description            |
|-------------|--------|------------------------|
| id          | SERIAL | Primary key            |
| temperature | FLOAT  | Current temperature    |
| windspeed   | FLOAT  | Wind speed value       |
| time        | TEXT   | Timestamp from API     |

---

## ⚙️ Setup Instructions

### 1. Start PostgreSQL using Docker

bash
docker run -d \
  --name weather-postgres \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=weatherdb \
  -p 5432:5432 \
  postgres

### 2. Install Python dependencies
pip install -r requirements.txt


### 3. Run ETL pipeline
python etl.py


## 🌐 API Used
Open-Meteo API (Free Weather API)
Example endpoint:
https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true


## 📊 Example Output
id	temperature	windspeed	time
1	29.5	12.3	2026-05-23T10:00


## 🧠 What You Learn
API data ingestion
ETL pipeline design
SQL database operations
Docker container usage
Real-world data engineering workflow

## 🚀 Future Improvements
Add Airflow for scheduling
Store historical weather data
Add data visualizations
Deploy to cloud (AWS/GCP)
Convert into multi-source pipeline

## ⭐ Purpose
To simulate a real-world production-like data pipeline using Python, SQL, and Docker.