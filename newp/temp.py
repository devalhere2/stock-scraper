import csv
import os

def getlink(name):
    my_dic = csv.DictReader(open('deval-stock/Equity.csv'))
    for i in my_dic:
        if i['Security Id'] == name:
            num = i['Security Code']
            return [f'https://api.bseindia.com/BseIndiaAPI/api/getScripHeaderData/w?Debtflag=&scripcode={num}&seriesid=',f'https://api.bseindia.com/BseIndiaAPI/api/StockTrading/w?flag=&quotetype=EQ&scripcode={num}']
