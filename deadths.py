# -*- coding: utf-8 -*-

#%%

import pandas as pd
import numpy as np
from wwo_hist import retrieve_hist_data


#%%

df = pd.read_csv('./LUDN_2286_CTAB_20200422181131.csv', delimiter=';')


list_of_columns = list(df.columns)
list_of_new_columns = ['kod', 'nazwa', '2002', '2003', '2004', '2005', 
                       '2006', '2007', '2008', '2009', '2010', '2011', '2012', 
                       '2013', '2014', '2015', '2016', '2017', '2018', '2019']

#%%
df.columns = list_of_new_columns 

#%%



df_new = df[df['nazwa'].str.isupper() == False]

df_sum = df_new.sum()
df_sum = df_sum.drop(['kod', 'nazwa','2019'], axis=0)

df_sum = pd.DataFrame(df_sum)
columns_sum = ['sum']
df_sum.columns = columns_sum

#%%



#%%

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

#%%

poland_weather_data = hist_weather_data[0]
print(poland_weather_data.head())


#%%
pwd_mean = poland_weather_data.set_index('date_time')

pwd_mean.head()

pwd_mean = pwd_mean.astype({"maxtempC": int, "mintempC": int})
print(type(pwd_mean.iloc[0,0]))
pwd_mean_temp = pwd_mean[['maxtempC','mintempC']]

#%%
pwd_mean_temp = pwd_mean.resample('Y').mean()
pwd_mean_temp = pwd_mean_temp.reset_index()



import datetime
pwd_mean_temp['year'] = pd.DatetimeIndex(pwd_mean_temp['date_time']).year


df_sum['year'] = df_sum.index

pwd_mean_temp = pwd_mean_temp.set_index('year')
df_sum = df_sum[['sum','year']]

#%%

















