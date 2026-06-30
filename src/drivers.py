# function to pull driver information and images

import requests
import pandas as pd

def get_driver_info():
       driver_url = "https://cf.nascar.com/cacher/drivers.json"
       response = requests.get(driver_url)
       data = response.json()
       drivers = pd.DataFrame(data['response'])
       drivers_clean = drivers[['Nascar_Driver_ID', 'Driver_Series', 'First_Name',
              'Last_Name', 'Full_Name', 'Short_Name',
              'DOB', 'DOD', 'Rookie_Year_Series_1', 'Rookie_Year_Series_2',
              'Rookie_Year_Series_3', 'Badge','Badge_Image', 'Manufacturer', 'Team', 'Image',
              'Image_Transparent', 'SecondaryImage', 'Firesuit_Image']]
       drivers_clean = drivers_clean.drop_duplicates(subset=["Nascar_Driver_ID"])
       return drivers_clean