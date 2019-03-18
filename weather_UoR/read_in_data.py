#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:56:07 2019

@author: mc4117
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

weather = pd.read_csv('weather.csv')

weather_no_nan = weather.dropna().reset_index(drop= True)[1:len(weather)].reset_index(drop= True)

column_list = list(weather_no_nan.columns.values)


for i in column_list:
    weather_no_nan[i] = pd.to_numeric(weather_no_nan[i])

print(weather_no_nan.info())
corr = weather_no_nan.corr()

sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
