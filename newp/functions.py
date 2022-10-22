import csv
import requests
import json

def getlink(name):
    my_dic = csv.DictReader(open(r'C:\Users\deval\Desktop\CS\python\deval-stock\Equity.csv'))
    for i in my_dic:
        if i['Security Id'] == name:
            num = i['Security Code']
            return num

def getdata(num):
    link1 = f'https://api.bseindia.com/BseIndiaAPI/api/getScripHeaderData/w?Debtflag=&scripcode={num}&seriesid='
    link2 = f'https://api.bseindia.com/BseIndiaAPI/api/StockTrading/w?flag=&quotetype=EQ&scripcode={num}'

    data1 = requests.get(link1)
    data2 = requests.get(link2)
    # j1 = json.loads(data1.text)
    # j2 = json.loads(data2.text)
    print(data1.text)