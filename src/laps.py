# function to get single lap data for each race in a season

import requests
import pandas as pd

FLAG_KEY = {
    0: "None",
    1: "Green",
    2: "Yellow",
    3: "Red",
    4: "White",
    5: "Checkered",
    8: "Hot Track",
    9: "Cold Track"
}


def fetch_single_race(year, series_num, race_id):

    race_url = f"https://cf.nascar.com/cacher/{year}/{series_num}/{race_id}/lap-times.json"

    try:
        response = requests.get(race_url, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()

        df = pd.json_normalize(
            data["laps"],
            record_path="Laps",
            meta=["Number", "FullName", "NASCARDriverID"]
        )

        flag_status = pd.DataFrame(data["flags"])
        flag_status["FlagName"] = (
            flag_status["FlagState"]
            .map(FLAG_KEY)
            .fillna("Unknown")
        )

        df = pd.merge(
            df,
            flag_status,
            left_on="Lap",
            right_on="LapsCompleted",
            how="left"
        )

        return df

    except Exception as e:
        print(f"Race {race_id}: Failed to download lap data ({e}). Skipping.")
        return None
    
def get_lap_data(year, series_num, race_ids):

    lap_data = []

    for race_id in race_ids:

        race_data = fetch_single_race(year, series_num, race_id)

        if race_data is None:
            continue

        race_data["race_id"] = race_id
        lap_data.append(race_data)

    if not lap_data:
        print(f"No lap data downloaded for {year}.")
        return pd.DataFrame()

    return pd.concat(lap_data, ignore_index=True)
