# function to get track information 

import requests
import pandas as pd

# function to get track information 
def get_track_info():
    track_info_url = "https://cf.nascar.com/cacher/tracks.json"
    response = requests.get(track_info_url)
    data = response.json()
    df = pd.DataFrame(data['items'])
    df = df[['track_id', 'track_name', 'track_surface', 'track_type']]
    return df
