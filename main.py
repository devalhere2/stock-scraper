from functions import getdata
import ta
import pandas as pd



df = getdata(name='TITAN',time=3,num=20)
  
# df = pd.read_json('data.json')
# df.drop('s',axis=1,inplace=True)
# df.set_index('t',inplace=True)
# df.sort_index(ascending=False,inplace=True)
# df.to_excel('data.xlsx')
print(df)