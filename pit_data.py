# function to download pit stop data for each race in a season

import requests
import pandas as pd

def fetch_pit_data(series_num, race_ids):
    pit_data = []

    for race_id in race_ids:
        pit_url = f"https://cf.nascar.com/cacher/live/series_{series_num}/{race_id}/live-pit-data.json"

        try:
            response = requests.get(pit_url, verify=False, timeout=30)
            response.raise_for_status()
            race_data = pd.DataFrame(response.json())

            if race_data.empty:
                print(f"Race {race_id}: No pit data returned. Skipping.")
                continue

            race_data["race_id"] = race_id
            pit_data.append(race_data)

        except Exception as e:
            print(f"Race {race_id}: Failed to download ({e}). Skipping.")
            continue

    if not pit_data:
        print("No pit data was successfully downloaded.")
        return pd.DataFrame()

    pit_df = pd.concat(pit_data, ignore_index=True)

    pit_df = pit_df[
        [
            "vehicle_number",
            "lap_count",
            "pit_stop_type",
            "left_front_tire_changed",
            "right_front_tire_changed",
            "left_rear_tire_changed",
            "right_rear_tire_changed",
            "race_id",
        ]
    ]

    print(f"Successfully downloaded pit data for {len(pit_data)} races.")
    return pit_df