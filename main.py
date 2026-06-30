# function that uses the process season to pull in result, lap, race, and pit data over multiple seasons

from src.process_season import process_season
import pandas as pd

years = range(2021, 2027)
series = "series_1"
series_num = 1
all_races = []
all_laps = []
all_results = []
all_pits = []

for year in years:
    print(f"Processing {year}...")

    races, laps, results, pits = process_season(year,series, series_num)

    all_races.append(races)
    all_laps.append(laps)
    all_results.append(results)
    all_pits.append(pits)

races = pd.concat(all_races, ignore_index=True)
laps = pd.concat(all_laps, ignore_index=True)
results = pd.concat(all_results, ignore_index=True)
pit = pd.concat(all_pits, ignore_index=True)