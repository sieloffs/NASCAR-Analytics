# NASCAR Analytics & Race Prediction Pipeline

An end-to-end data engineering and analytics project that scrapes NASCAR race data, builds structured datasets (laps, pit stops, results), and powers an interactive Power BI dashboard for race analysis and performance insights.

---

## Project Overview

This project collects and processes NASCAR race data from public APIs and transforms it into structured datasets for analysis and visualization.

It includes:
- Race schedule and track data
- Lap data
- Pit stop data
- Driver performance tracking
- Feature engineering for future predictive modeling

The final output is used in a Power BI dashboard to explore race trends, driver performance, and historical comparisons.

---

## Key Features

- Automated scraping of NASCAR race, lap, and pit data
- Python ETL pipeline
- Season level data aggregation
- Feature engineering (tire age, pit strategy, position changes, etc.)
- Power BI ready datasets
- Foundation for win probability / race prediction modeling

---


## Design

- Each module is responsible for a single data source (laps, pit stops, results, tracks). These can be found in the src folder explained below.
- `process_season()` acts as an orchestration layer for a full season of data
- `main.py` handles multi-season and multi-series execution

---

## Project Structure

```text
src/
  drivers.py
  laps.py
  pit_stop.py
  tracks.py
  drivers.py
  races.py
  results.py
  process_season.py



