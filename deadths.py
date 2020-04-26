# -*- coding: utf-8 -*-

#%%

import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


#%%

#loading data to df's

deaths_data = pd.read_csv('./LUDN_2286_CTAB_20200422181131.csv', delimiter=';')
weather_data = pd.read_csv('./pwd.csv')

deaths_data.head()

#%%
weather_data.head()

#%%

# cleaning deadhs data

# executing just general polish data of deadhs

deaths_data = deaths_data[deaths_data['Nazwa']== 'POLSKA']

#%%
deaths_data = deaths_data.drop(['Nazwa','Kod'], axis=1)
#%%
list_of_new_colnames = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
                        2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
deaths_data.columns = list_of_new_colnames
deaths_data = deaths_data.drop(2019, axis=1)

#%%
# transposing data frame

deaths_data = deaths_data.T

#%%

weather_data.head()
weather_data['year'] = pd.DatetimeIndex(weather_data['date_time']).year
future_index_type = str(type(weather_data.loc[1,'year']))

#%%

weather_data = weather_data.set_index('year')

#%%
weather_data_mean = weather_data.groupby(level='year').mean()

#%%

full_df = deaths_data.merge(weather_data_mean, left_index=True, right_index=True)
full_df = full_df.rename(columns={0: 'deaths'})


#%%

# correlation

#def get_corrs(df):
    #col_correlations = df.corr()
    #col_correlations.loc[:, :] = np.tril(col_correlations, k=-1)
    #cor_pairs = col_correlations.stack()
    #return cor_pairs.to_dict()

#corr_df = get_corrs(full_df)
    
#%%
    
# corr testing


    






