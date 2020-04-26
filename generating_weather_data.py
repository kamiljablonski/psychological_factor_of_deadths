# -*- coding: utf-8 -*-
#%%
from wwo_hist import retrieve_hist_data

# weather data form https://www.worldweatheronline.com/


import os
os.chdir("./")

frequency=24
start_date = '02-01-2010'
end_date = '02-01-2019'
api_key = '3287e0d3bbb24204bef170141202204'
location_list = ['poland']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = False,
                                store_df = True)


poland_weather_data = hist_weather_data[0]
print(poland_weather_data.head())
poland_weather_data.to_csv('pwd.csv', header=True, index=False)