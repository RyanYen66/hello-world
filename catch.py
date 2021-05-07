import requests
from io import StringIO
import pandas as pd
from pandas.tseries.offsets import Day, BDay
import numpy as np
import openpyxl
from datetime import date, timedelta


def OutputFiveDayStock (Countday):

    CatchDate = date.today() - timedelta(days = Countday)

    # print today date
    print(CatchDate.strftime('%Y%m%d'))

    TWSElistedDate = CatchDate.strftime('%Y%m%d')

    r = requests.post('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + TWSElistedDate + '&type=ALLBUT0999')
    print(r.text)

    df = pd.read_csv(StringIO(r.text.replace("=", "")), 
        header=["證券代號" in l for l in r.text.split("\n")].index(True)-1)

    # Sorting string

    df.apply(lambda s: pd.to_numeric(s.astype(str).str.replace(",", "").replace("+", "1").replace("-", "-1"), errors='coerce'))

    if Countday == 0:
        df.to_excel("D:\RyanGit\output.xlsx", sheet_name='Today')
    else:
        with pd.ExcelWriter('D:\RyanGit\output.xlsx',mode='a') as writer:  
            df.to_excel(writer, sheet_name='D-'+ str(Countday) +'')
            
for Countday in range(5):
    OutputFiveDayStock (Countday)
    time.sleep(10)