# function to get results data for a single season

import requests
import pandas as pd

def fetch_single_result(year,series_num, race_id):
    race_url = f"https://cf.nascar.com/loopstats/prod/{year}/{series_num}/{race_id}.json"
    try:
        response = requests.get(race_url)
        data = response.json()
        # pull out lap data and create a row for each driver lap time
        df = pd.json_normalize(
            data,
            record_path='drivers',
            meta=['race_id']
        )
        df = df[['driver_id', 'ps', 'laps', 'race_id']]

        return df
    
    except Exception as e:
        print(f"Race {race_id}: Failed to download results ({e}). Skipping.")
        return None


# using the result function for each race in the season to get a df of all results
def get_result_data(year, series_num, race_ids):
    result_data = []

    for race_id in race_ids:
        race_data = fetch_single_result(year, series_num, race_id)
        
        if race_data is None:
            continue

        result_data.append(race_data)

    if not result_data:
        print(f"No race results found for {year}.")
        return pd.DataFrame()

    return pd.concat(result_data, ignore_index=True)