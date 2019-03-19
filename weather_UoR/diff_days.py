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

    restr = noon_df[['Number_of_days', column_name]]

    list1_days = []
    list1_data = []

    list2_days = []
    list2_data = []
    
    for i in range(len(restr)):
        list1_days.append(restr.loc[i]['Number_of_days'])
        list1_data.append(restr.loc[i][column_name])
        df = restr[restr['Number_of_days'] == restr['Number_of_days'][i] + 1].reset_index(drop=True)
        if len(df) == 0:
            list2_days.append(np.nan)
            list2_data.append(np.nan)
        elif len(df) == 1:
            list2_days.append(df.loc[0]['Number_of_days'])
            list2_data.append(df.loc[0][column_name])
        else:
            print('error')
    
    
    df_diff = pd.concat([pd.DataFrame(list1_data, columns = [str(column_name) + '_pre']), pd.DataFrame(list2_data, columns = [str(column_name) + '_post'])], axis = 1)

    plt.scatter(df_diff[str(column_name) + '_pre'], df_diff[str(column_name) + '_post'])
    plt.xlabel(str(column_name))
    plt.ylabel(str(column_name) + ' one day after')
    plt.show()

    df_diff_no_nan = df_diff.dropna()

    
    X_train, X_test, y_train, y_test = skl.model_selection.train_test_split(df_diff_no_nan[str(column_name) + '_pre'], df_diff_no_nan[str(column_name) + '_post'], test_size=0.25, random_state=42)
    
    return X_train, X_test, y_train, y_test
    

pred_values = [11.6,	78,	161,	8.2,	0.2,	1019.9,	2.3]


for i in range(len(column_list)):
    print(column_list[i])
    X_train, X_test, y_train, y_test = plt_dist_24(noon, column_list[i])
    # Create linear regression object
    regr = linear_model.LinearRegression()

    array_x = np.array(X_train).reshape(-1,1)
    array_y = np.array(y_train).reshape(-1,1)
    # Train the model using the training sets
    regr.fit(array_x, array_y)
    
    array_X_test = np.array(X_test).reshape(-1,1)
    array_y_test = np.array(y_test).reshape(-1,1)    

    # Make predictions using the testing set
    y_pred = regr.predict(array_X_test)
    
    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
      % skl.metrics.mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' %skl.metrics.r2_score(array_y_test, y_pred, multioutput='raw_values'))
    
    er = []

    for j in range(len(y_test)):
        x = abs(array_y_test[j] - y_pred[j])
        er.append(x)
    print('Variance' + str(np.var(er)))
    
    print(pred_values[i])
    print(regr.predict(np.array(pred_values[i]).reshape(-1,1)))