#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:30:42 2019

@author: os3918
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

weather = pd.read_csv('weather.csv')


for i in range(1, len(weather['TimeStamp'])):
    weather['TimeStamp'][i] = datetime.strptime(weather['TimeStamp'][i], '%Y%m%d')


weather_no_nan = weather.dropna().reset_index(drop= True)[1:len(weather)].reset_index(drop= True)

column_list = list(weather_no_nan.columns.values)[2:len(weather_no_nan.columns.values)]


for i in column_list:
    weather_no_nan[i] = pd.to_numeric(weather_no_nan[i])
    
    


noon = weather_no_nan[weather_no_nan['Time']=='1200'].reset_index(drop=True).drop(labels=['TimeStamp','Time'],axis=1)

print(noon.mean())
print(noon.var())