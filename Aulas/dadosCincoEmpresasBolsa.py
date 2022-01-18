from pandas_datareader import data as wb
import pandas as pd

tickers = ["PG", "MSFT", "T", "F", "GE"]
newData = pd.DataFrame()
for i in tickers:
    newData[i] = wb.DataReader(i, data_source="yahoo", start="2010-1-1")["Adj Close"]
print(newData.tail())
print("-----------------------------------------------")
print("FECHAMENTO AJUSTADO DA MICROSOFT de 2010 a 2021")
print(newData["MSFT"].tail(10))
