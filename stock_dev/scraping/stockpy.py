#!/usr/bin/env python
# coding: utf-8

import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import seaborn as sns
import pandas as pd
from time import sleep

def hello():
    print("Hello World2!")

def linear_fit(x, a, b):
    return a*x + b

def linear_fit_pre(x, a, b):
    return a*x + b

def find_index1(item, record):
    return record.where(record == item).first_valid_index()

def kabu_japan(df,df_data_base,length, a_1, b_1, c_1, a_2, b_2, c_2):
    list_df = pd.DataFrame()
    for i in range(length):
    #for i in range(1380,1383):
        #print(i)
        
        sleep(0.2)
        
        try:
            find_index1(df.A[i], df_data_base)
            if find_index1(df.A[i], df_data_base) == None:
                continue
        except KeyError:
            continue
    
        tickerSymbol = str(df.A[i])+'.T'
        #tickerSymbol = '1438.T'
        tickerData = yf.Ticker(tickerSymbol)
        tickerDf = tickerData.history(period=a_1, start=b_1, end=c_1)
        tickerDf_pre = tickerData.history(period=a_2, start=b_2, end=c_2)
        #print(len(tickerDf.Close))
        if len(tickerDf.Close) > 1 :

            list_linear_x = range(0,len(tickerDf),1)
            array_x = np.array(list_linear_x)

            param, cov = curve_fit(linear_fit, array_x, tickerDf.Close/max(tickerDf.Close))
            array_y_fit = param[0] * array_x + param[1]
            tilt = param[0]
            intercept = param[1]


            list_linear_x_pre = range(0,len(tickerDf_pre),1)
            array_x_pre = np.array(list_linear_x_pre)
            param_pre, cov_pre = curve_fit(linear_fit_pre, array_x_pre, tickerDf_pre.Close/max(tickerDf_pre.Close))

            array_y_fit = param_pre[0] * array_x_pre + param_pre[1]
            tilt_pre = param_pre[0]
            intercept_pre = param_pre[1]

            tilt_diff = abs(tilt - tilt_pre)
            #print(find_index1(df.A[i], df_data_base), df)

            
#
            if tilt > 0.015 and 0.02 > tilt and np.average(tickerDf.Volume) > 200000:
                
                num = find_index1(df.A[i], df_data_base)
                #print(num)
                df_1 = pd.Series([float(df_data_base[num:(num+1)].B), float(df_data_base[num:(num+1)].C), float(df_data_base[num:(num+1)].D)])
                list_linear_x = range(0,3,1)
                
                print(i)
                array_x = np.array(list_linear_x)
                param, cov = curve_fit(linear_fit, array_x, df_1/max(df_1))

                array_y_fit = param[0] * array_x + param[1]
                reeki = param[0]
                reeki_seppen = param[1]
                #print(reeki)

                #df_1 = [df.A[i],tilt, tilt_mean]
                #df_1.loc[df.A[i]] = [df.A[i],tilt, tilt_mean]
                df_1 = pd.DataFrame([[str(df.A[i]),(np.average(tickerDf.Volume)*tilt/tilt_diff)*(-reeki), -reeki, tilt, tilt_pre, tilt_diff, np.average(tickerDf.Volume),tickerDf_pre.Close[0], tickerDf.Close[len(tickerDf.Close)-1]]], columns=['code','point', 'netincome','tilt','tilt_pre','tilt_diff','Volume','price_pre','price_now'])
                list_df = list_df.append(df_1)

                #print(find_index1(df.A[i], df_data_base))

                #print("The number"+str(df.A[i])+"'s tilt is " +str(param[0]))
                #tmp_se = pd.Series( [ df.A[i], tilt, tilt_mean ], index=list_df.columns )
                #list_df = list_df.append( tmp_se, ignore_index=True )
                #df_1.loc[str(df.A[i])] = 0
                #df_1.(df.A[i])
        print("Now "+str(i)+" in " +str(length))
        #print("\r"+"Now "+str((i/length)*100)+"%",end="")
    print("\n"+"Finish")
    return list_df

def kabu_america(df,df_data_base,length, a_1, b_1, c_1, a_2, b_2, c_2):
    list_df = pd.DataFrame()
    for i in range(length):
        sleep(0.2)
        
        try:
            find_index1(df.A[i], df_data_base)
            if find_index1(df.A[i], df_data_base) == None:
                continue
        except KeyError:
            continue

        tickerSymbol = str(df.A[i])
        #tickerSymbol = '1438.T'
        tickerData = yf.Ticker(tickerSymbol)
        tickerDf = tickerData.history(period=a_1, start=b_1, end=c_1)
        tickerDf_pre = tickerData.history(period=a_2, start=b_2, end=c_2)
        #print(len(tickerDf.Close))
        if len(tickerDf.Close) > 1 :

            list_linear_x = range(0,len(tickerDf),1)
            array_x = np.array(list_linear_x)

            param, cov = curve_fit(linear_fit, array_x, tickerDf.Close/max(tickerDf.Close))
            array_y_fit = param[0] * array_x + param[1]
            tilt = param[0]
            intercept = param[1]


            list_linear_x_pre = range(0,len(tickerDf_pre),1)
            array_x_pre = np.array(list_linear_x_pre)
            param_pre, cov_pre = curve_fit(linear_fit_pre, array_x_pre, tickerDf_pre.Close/max(tickerDf_pre.Close))

            array_y_fit = param_pre[0] * array_x_pre + param_pre[1]
            tilt_pre = param_pre[0]
            intercept_pre = param_pre[1]

            tilt_diff = abs(tilt - tilt_pre)
            #print(find_index1(df.A[i], df_data_base))
            


#tilt > 0.0015 and np.average(tickerDf.Volume) > 10000000
            if tilt > 0.0015 and np.average(tickerDf.Volume) > 10000000 :
                num = find_index1(df.A[i], df_data_base)
                df_1 = pd.Series([float(df_data_base[num:(num+1)].B), float(df_data_base[num:(num+1)].C), float(df_data_base[num:(num+1)].D)])

                list_linear_x = range(0,3,1)

                array_x = np.array(list_linear_x)
                param, cov = curve_fit(linear_fit, array_x, df_1/max(df_1))

                array_y_fit = param[0] * array_x + param[1]
                reeki = param[0]
                reeki_seppen = param[1]
                #print(reeki)

                #df_1 = [df.A[i],tilt, tilt_mean]
                #df_1.loc[df.A[i]] = [df.A[i],tilt, tilt_mean]
                df_1 = pd.DataFrame([[str(df.A[i]),(np.average(tickerDf.Volume)*tilt/tilt_diff)*(-reeki), -reeki, tilt, tilt_pre, tilt_diff, np.average(tickerDf.Volume),tickerDf_pre.Close[0], tickerDf.Close[len(tickerDf.Close)-1]]], columns=['code','point', 'netincome','tilt','tilt_pre','tilt_diff','Volume','price_pre','price_now'])
                list_df = list_df.append(df_1)
                #print(find_index1(df.A[i], df_data_base), df)

                #print("The number"+str(df.A[i])+"'s tilt is " +str(param[0]))
                #tmp_se = pd.Series( [ df.A[i], tilt, tilt_mean ], index=list_df.columns )
                #list_df = list_df.append( tmp_se, ignore_index=True )
                #df_1.loc[str(df.A[i])] = 0
                #df_1.(df.A[i])
        print("Now "+str(i)+" in " +str(length))
        #print("\r"+"Now "+str((i/length)*100)+"%",end="")
    print("\n"+"Finish")
    return list_df
