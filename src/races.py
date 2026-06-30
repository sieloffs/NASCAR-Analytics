import requests
import pandas as pd
def get_race_ids(year, series_key):

    race_list_url = f"https://cf.nascar.com/cacher/{year}/race_list_basic.json"
    response = requests.get(race_list_url, verify = False)
    data = response.json()
    races_df = pd.DataFrame(data[series_key])
    races_df_clean = races_df[['race_id', 'series_id', 'race_season', 'track_id', 'race_name', 'race_type_id', 'actual_laps', 'race_date']]
    
    return races_df_clean
