#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:56:07 2019

@author: mc4117
"""

import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('weather.csv')

weather_no_nan = weather.dropna()

plt.matshow(weather_no_nan.corr())
plt.show()