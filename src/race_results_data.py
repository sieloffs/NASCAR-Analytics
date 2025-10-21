import requests
import pandas as pd

def fetch_result_data(year, series_num):

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

    def single_race_data(series_num, race_id):
        result_url = f"https://cf.nascar.com/loopstats/prod/{year}/{series_num}/{race_id}.json"
        response = requests.get(result_url)
        data = response.json()
        return pd.DataFrame(data)
    
    result_data = []
    for race_id in race_ids:
        race_data = single_race_data(series_num,race_id)
        race_data['race_id'] = race_id
        result_data.append(race_data)

    result_df = pd.concat(result_data, ignore_index=True)

    return result_df
