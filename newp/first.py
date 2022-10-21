import requests
import pandas as pd
# link = 'https://api.bseindia.com/BseIndiaAPI/api/getScripHeaderData/w?Debtflag=&scripcode=509488&seriesid='
# data = requests.get(link)
# print(data.text)

datalink = f"https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize=25&pageno=1&sort=intraday&sortby=percentchange&sortorder=desc&marketcap=largecap%2Cmidcap&duration=1%20day" 
dataget = requests.get(datalink)
data = dataget.json()
print(dataget.text)
# df_topg = pd.DataFrame(columns=['Company_Name','Market_Cap','Previous_close','open','High','Change','Current'])
# for i in range(len(data['searchresult'])):
#         df_topg.loc[i] = [data['searchresult'][i]['ticker'] ,data['searchresult'][i]['marketCap'], data['searchresult'][i]['previousClose'] ,data['searchresult'][i]['open']  ,data['searchresult'][i]['high'], data['searchresult'][i]['percentChange'] ,data['searchresult'][i]['current']]
# df_topg['Closeness'] = (df_topg['High']/df_topg['Current'] - 1)*100 
# df_topg['avg_close'] = df_topg['Closeness'].mean()
# df_topg