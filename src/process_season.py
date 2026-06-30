
from src.races import get_race_ids
from src.tracks import get_track_info
from src.laps import get_lap_data
from src.results import get_result_data
from src.pit_stop import fetch_pit_data

def process_season(year, series_key, series_num):
    
    races = get_race_ids(year, series_key)
    races = races[races['race_type_id'] ==1]
    # create a list of race ids
    race_ids = races['race_id'].tolist()

    # get tracking infromation
    track_df = get_track_info()

    # merginging track information with the race information
    races = races.merge(track_df, on='track_id', how='left')

    # get lap data for each race in the season
    laps = get_lap_data(year, series_num, race_ids)

    # get result data for each race in the season
    results = get_result_data(year, series_num, race_ids)

    # get pit data for the season
    pit = fetch_pit_data(series_num,race_ids)
    return races, laps, results, pit
