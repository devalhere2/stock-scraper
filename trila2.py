from calendar import month
from distutils.util import change_root
import requests
import datetime 
from datetime import timedelta
import pandas as pd
import math

from functions import  *



            
def fun(name = '9',):
    e = datetime.datetime.now()
    epochi = int(datetime.datetime(e.year , e.month -1 , e.day, 15, 31, 0).timestamp())
    epochf = int(datetime.datetime(e.year, e.month, e.day, 15, 31, 0).timestamp())
    datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution=1D&from={epochi}&to={epochf}' 
    dataget = requests.get(datalink)
    data = dataget.json()
    
    df = pd.DataFrame(columns=['open','close','high','low'])
    
    for i in range(len(data['t'])):
            df.loc[i] = [data['o'][i],data['c'][i],data['h'][i],data['l'][i],]
    df['change'] = abs(((df['close'] - df['open'])/ df['open'])*100)
    df['volatility'] = abs(((df['high'] - df['low'])/ df['low'])*100)
    df['day_change'] = ((df['close'] - df['open'])/ df['open'])*100
    # df['condition'] = 0
    mean_change = df['change'].mean()
    mean_volatality = df['volatility'].mean()
    
    today_change = df['change'][len(df['open'])-1]
    whereitlies = 0
    for i in range(len(df['open'])):
        try:
            if today_change > df['change'][i+1]:
                whereitlies += 1
            else:
                pass
        except:
            pass
    


    # for i in range(len(df['day_change'])):
    #     # if abs(i) > mean_change:
    #     #     df['condition'] = 'True'
    #     # else:
    #     #     df['condition'] = 'Faslse'
            
    #     if df.at[i,'change'] > mean_volatality:
    #         df.at[i,'condition'] = 'True'
            
    #     else:
    #         df.at[i,'condition'] = 'False'





    df['c1'] = abs((df['high'] - df['open'])/df['open'])*100
           
   
    print(df)
    print('Change :' , mean_change , 'Average High :', df['c1'].mean())
    print('Volatility :' , mean_volatality)
    print(today_change    ,whereitlies,len(df['c1']))






    # correct_signal = 0
    # false_signal = 0
    # con = mean_change

    # for i in range(len(df['open'])):               next day signals
    #      try:
    #         if(df['change'][i] > con):
    #             if(df['day_change'][i] > 0 and df['day_change'][i+1] < 0):
    #                 correct_signal += 1
    #             elif(df['day_change'][i] < 0 and df['day_change'][i+1] > 0):
    #                 correct_signal += 1
    #             else:
    #                 false_signal += 1
    #         else:
    #             pass
    #     except:
    #         pass    
    # print(correct_signal,false_signal,len(df['change']))

    # for i in range(len(df['open'])):             volatility check
    #     try:
    #         if(df['volatility'][i] > con):
    #             correct_signal += 1
    #         else:
    #             false_signal += 1
    #     except:
    #         pass    
    # print(correct_signal,false_signal,len(df['change']))
    

print(topg(50))
print(topl(50))
getdata(name='HFCL')
