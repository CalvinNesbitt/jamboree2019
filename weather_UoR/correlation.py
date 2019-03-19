#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:56:58 2019

@author: mc4117
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:48:30 2019

@author: mc4117
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

import sklearn as skl

from sklearn import datasets, linear_model

weather = pd.read_csv('weather.csv')


for i in range(1, len(weather['TimeStamp'])):
    weather['TimeStamp'][i] = datetime.datetime.strptime(weather['TimeStamp'][i], '%Y%m%d')


weather_no_nan = weather.dropna().reset_index(drop= True)[1:len(weather)].reset_index(drop= True)

column_list = list(weather_no_nan.columns.values)[2:len(weather_no_nan.columns.values)]


for i in column_list:
    weather_no_nan[i] = pd.to_numeric(weather_no_nan[i])
    


## restrict to March    
weather_no_nan['Month'] = weather_no_nan['TimeStamp'].map(lambda x: x.month)
weather_no_nan_march = weather_no_nan[weather_no_nan['Month'] == 3].reset_index(drop = True).drop(labels=['Month'],axis=1)

noon_march = weather_no_nan_march[weather_no_nan_march['Time']=='1200'].reset_index(drop=True).drop(labels=['Time'],axis=1)

print(noon_march.mean())
print(noon_march.var())
mydate = datetime.datetime(2000,1, 1, 0,0)
noon_march['Number_of_days'] = noon_march['TimeStamp'].map(lambda x: (x-mydate).days)

noon_march_sorted_values = noon_march.sort_values('Number_of_days')


noon = weather_no_nan[weather_no_nan['Time']=='1200'].reset_index(drop=True).drop(labels=['Time'],axis=1)


noon['Month'] = noon['TimeStamp'].map(lambda x: x.month)
noon['Number_of_days'] = noon['TimeStamp'].map(lambda x: (x-mydate).days)

def plt_dist_24(noon_df, column_name):

    restr = noon_df[['Td', 'TSoil100', 'P', column_name]]
    
    X = restr[['Td', 'TSoil100', 'P']]
    y = restr[column_name]

    


    
    X_train, X_test, y_train, y_test = skl.model_selection.train_test_split(X, y, test_size=0.25, random_state=42)
    
    return X_train, X_test, y_train, y_test
    
new_column_list = ['RH', 'Sdur', 'Rain_accum_der', 'U10']

for i in new_column_list:
    print(i)
    X_train, X_test, y_train, y_test = plt_dist_24(noon, i)
    # Create linear regression object
    regr = linear_model.LinearRegression()

    #array_x = np.array(X_train).reshape(-1,1)
    #array_y = np.array(y_train).reshape(-1,1)
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    
 

    # Make predictions using the testing set
    y_pred = regr.predict(X_test)
    
    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
      % skl.metrics.mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' %skl.metrics.r2_score(y_test, y_pred))5#, multioutput='raw_values'))