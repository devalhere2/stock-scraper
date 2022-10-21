import datetime
from datetime import timedelta
import requests
import pandas as pd
import json

def getdata(time = 5,num = 10,name = '9'):
    e = datetime.datetime.now()
    dayname = e.strftime('%A')


    h = e.hour
    m = e.minute
    s = e.second
    if(dayname != 'Sunday' and  dayname != 'Saturday'):
        print('inside')
        if (h > 15):    
            epochf = int(datetime.datetime(e.year, e.month, e.day, 15, 31, 0).timestamp())
            epochi = int(epochf - int(num)*60*time)
            datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution={time}&from={epochi}&to={epochf}' 
            dataget = requests.get(datalink)
        

        elif(h < 9):
            e = datetime.datetime.today() - timedelta(days=1)
            epochf = int(datetime.datetime(e.year, e.month, e.day, 15, 31, 0).timestamp())
            epochi = int(epochf - int(num)*60*time)
            datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution={time}&from={epochi}&to={epochf}' 
            dataget = requests.get(datalink)
            
        elif( h == 15 and m > 31):
            epochf = int(datetime.datetime(e.year, e.month, e.day, 15, 31, 0).timestamp())
            epochi = int(epochf - int(num)*60*time)
            datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution={time}&from={epochi}&to={epochf}' 
            dataget = requests.get(datalink)
            

        elif(h == 9 and m < 15):
            e = datetime.datetime.today() - timedelta(days=1)
            epochf = int(datetime.datetime(e.year, e.month, e.day, 15, 31, 0).timestamp())
            epochi = int(epochf - int(num)*60*time)
            datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution={time}&from={epochi}&to={epochf}' 
            dataget = requests.get(datalink)

        else:
            epochf = int(datetime.datetime(e.year, e.month, e.day, e.hour, e.minute, e.second).timestamp())
            epochi = int(epochf - int(num)*60*time)

            datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution={time}&from={epochi}&to={epochf}' 
            dataget = requests.get(datalink)
        
        with open('data.json','w') as f:
            f.write(dataget.text)
        
        dataget = json.dumps(dataget.json())

        df = pd.read_json(dataget)
        
        return df
    else:
        return "Market is close today due to Weekend"

def topg(x = 25):

    datalink = f"https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize={x}&pageno=1&sort=intraday&sortby=percentchange&sortorder=desc&marketcap=largecap%2Cmidcap&duration=1%20day" 
    dataget = requests.get(datalink)
    data = dataget.json()

    df_topg = pd.DataFrame(columns=['Company_Name','Market_Cap','Previous_close','open','High','Change','Current'])
    for i in range(len(data['searchresult'])):
            df_topg.loc[i] = [data['searchresult'][i]['ticker'] ,data['searchresult'][i]['marketCap'], data['searchresult'][i]['previousClose'] ,data['searchresult'][i]['open']  ,data['searchresult'][i]['high'], data['searchresult'][i]['percentChange'] ,data['searchresult'][i]['current']]
    df_topg['Closeness'] = (df_topg['High']/df_topg['Current'] - 1)*100 
    df_topg['avg_close'] = df_topg['Closeness'].mean()
    return df_topg

def topl(x = 25):

    datalink = f'https://etmarketsapis.indiatimes.com/ET_Stats/losers?pagesize={x}&exchange=nse&pageno=1&sort=intraday&sortby=percentchange&sortorder=asc&marketcap=largecap%2Cmidcap&duration=1%20day'
    dataget = requests.get(datalink)
    data = dataget.json()

    
    df_topl = pd.DataFrame(columns=['Company_Name','Market_Cap','Previous_close','open','Low','Change','Current'])
    for i in range(len(data['searchresult'])):
            df_topl.loc[i] = [data['searchresult'][i]['ticker'] ,data['searchresult'][i]['marketCap'],data['searchresult'][i]['previousClose'],data['searchresult'][i]['open'] ,data['searchresult'][i]['low']      , data['searchresult'][i]['percentChange'],data['searchresult'][i]['current']]
    df_topl['Closeness'] = (df_topl['Current']/df_topl['Low'] - 1)*100  
    df_topl['avg_close'] = df_topl['Closeness'].mean()
   
    return df_topl

def intraday(name = '9'):
    try:
        e = datetime.datetime.now()
        epochi = int(datetime.datetime(e.year -1, e.month  , e.day, 15, 31, 0).timestamp())
        epochf = int(datetime.datetime(e.year, e.month, e.day, 15, 31, 0).timestamp())
        
        datalink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution=1D&from={epochi}&to={epochf}' 
        dataget = requests.get(datalink)
        
        data = dataget.json()
        
        epochi = int(datetime.datetime(e.year , e.month, e.day, 9, 20, 0).timestamp())
        epochf = int(datetime.datetime.now().timestamp())
        
        datachangelink = f'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={name}&resolution=60&from={epochi}&to={epochf}'
        dataget = requests.get(datachangelink)
        with open('datachange.json','w') as f:
                f.write(dataget.text)
        datachange = dataget.json()



        df = pd.DataFrame(columns=['open','close','high','low'])
        for i in range(len(data['t'])):
                df.loc[i] = [data['o'][i],data['c'][i],data['h'][i],data['l'][i]]
        df['change'] = abs(((df['close'] - df['open'])/ df['open'])*100)
        df['volatility'] = abs(((df['high'] - df['low'])/ df['low'])*100)
        df['day_change'] = ((df['close'] - df['open'])/ df['open'])*100
        
        mean_change = df['change'].mean()
        mean_volatality = df['volatility'].mean()
        
        today_change =   abs( ((datachange['c'][-1] - datachange['o'][0] )/ datachange['o'][0])*100)

        whereitlies = 0
        for i in range(len(df['open'])):
            try:
                if today_change > df['change'][i]:
                    whereitlies += 1
                else:
                    pass
            except:
                pass

        df['c1'] = abs((df['high'] - df['open'])/df['open'])*100
            
    
        final_cal = (whereitlies/len(df['c1']) ) *100

        return [f'Today_Change = {today_change}',f'Mean_Change = {mean_change}',f'Volatility = {mean_volatality}',f'Change is Higher than {round(final_cal,2)} % of days']
    except:
        return "Today is a Weekend"

    
