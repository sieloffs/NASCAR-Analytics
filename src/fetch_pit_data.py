import requests
import pandas as pd

def fetch_pit_data(year, series_num):
    
    series_key = f"series_{series_num}"

    race_list_url = f"https://cf.nascar.com/cacher/{year}/race_list_basic.json"
    response = requests.get(race_list_url)
    data = response.json()

    races_df = pd.DataFrame(data[series_key])

    # Convert race_date to datetime
    races_df['race_date'] = pd.to_datetime(races_df['race_date'], errors='coerce')
    races_df = races_df[races_df['race_type_id'] == 1] 

    # Keep only past races
    today = pd.Timestamp.now()
    past_races_df = races_df[races_df['race_date'] <= today]

    race_ids = past_races_df['race_id'].tolist()

    def fetch_single_race(series_num, race_id):
        pit_url = f"https://cf.nascar.com/cacher/live/series_{series_num}/{race_id}/live-pit-data.json"
        response = requests.get(pit_url)
        data = response.json()
        return pd.DataFrame(data)

    pit_data = []
    for race_id in race_ids:
        race_data = fetch_single_race(series_num,race_id)
        race_data['race_id'] = race_id
        pit_data.append(race_data)

    pit_df = pd.concat(pit_data, ignore_index=True)

    return pit_df
