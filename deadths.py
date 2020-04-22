# -*- coding: utf-8 -*-

#%%

import pandas as pd
import numpy as np
from wwo_hist import retrieve_hist_data


#%%

df = pd.read_csv('LUDN_2286_CTAB_20200422181131.csv', delimiter=';')

#%%

# weather data form https://www.worldweatheronline.com/


import os
os.chdir("./")

frequency=3
start_date = '11-DEC-2018'
end_date = '11-MAR-2019'
api_key = '3287e0d3bbb24204bef170141202204'
location_list = ['singapore','california']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)