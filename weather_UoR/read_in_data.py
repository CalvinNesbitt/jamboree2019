#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:56:07 2019

@author: mc4117
"""

import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
#import numpy as np
from datetime import datetime

## load dataset

weather = pd.read_csv('weather.csv')


for i in range(1, len(weather['TimeStamp'])):
    weather['TimeStamp'][i] = datetime.strptime(weather['TimeStamp'][i], '%Y%m%d')


column_list_1 = list(weather.values)[2:len(weather.columns.values)]

for i in column_list_1:
    weather[i] = pd.to_numeric(weather[i])

weather_no_nan = weather.dropna().reset_index(drop= True)[1:len(weather)].reset_index(drop= True)

column_list = list(weather_no_nan.columns.values)[2:len(weather_no_nan.columns.values)]


for i in column_list:
    weather_no_nan[i] = pd.to_numeric(weather_no_nan[i])

# final data with nan is weather

# final data no nan is weather_no_nan
    


## correlation heat_map

corr = weather_no_nan.corr()

sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)



