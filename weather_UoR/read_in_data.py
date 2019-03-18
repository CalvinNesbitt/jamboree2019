#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:56:07 2019

@author: mc4117
"""

import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np
from datetime import datetime

## load dataset

weather = pd.read_csv('weather.csv')


for i in range(1, len(weather['TimeStamp'])):
    weather['TimeStamp'][i] = datetime.strptime(weather['TimeStamp'][i], '%Y%m%d')



weather_no_nan = weather.dropna().reset_index(drop= True)[1:len(weather)].reset_index(drop= True)

column_list = list(weather_no_nan.columns.values)[2:len(weather_no_nan.columns.values)]


for i in column_list:
    weather_no_nan[i] = pd.to_numeric(weather_no_nan[i])

weather_no_nan['Month'] = weather_no_nan['TimeStamp'].map(lambda x: x.month)

## restrict to March    

weather_no_nan_march = weather_no_nan[weather_no_nan['Month'] == 3].reset_index(drop = True)

print(weather_no_nan_march)


## correlation heat_map

#corr = weather_no_nan.corr()

#sns.heatmap(corr, 
            #xticklabels=corr.columns.values,
            #yticklabels=corr.columns.values)



