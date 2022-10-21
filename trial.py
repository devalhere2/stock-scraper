import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
from functions import getdata , topg, topl
import datetime

# datalink = "https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize=25&pageno=1&sort=intraday&sortby=percentchange&sortorder=desc&marketcap=largecap%2Cmidcap&duration=1%20day" 
# dataget = requests.get(datalink)

# with open('topg.json','w') as f:
#         f.write(dataget.text)

# with open('topg.json','r') as f:
#        data =  json.load(f)


# df_topg = pd.DataFrame(columns=['Company_Name','Market_Cap','Change','High','Current'])
# for i in range(len(data['searchresult'])):
#         df_topg.loc[i] = [data['searchresult'][i]['nseScripCode'] ,data['searchresult'][i]['marketCap']  , data['searchresult'][i]['percentChange'],data['searchresult'][i]['high']  ,data['searchresult'][i]['current']]
# df_topg['Closeness'] = (df_topg['High']/df_topg['Current'] - 1)*100  

# print(topg().sort_values(by='Closeness'))
# print(topg())
# print(getdata(name ='TTML'))

print(topg())