import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^FTSE'] #Não São mais esses codigos
indiceData = pd.DataFrame()
for t in tickers:
   indiceData[t] = wb.DataReader(t, data_source='yahoo', start='1997-1-1')['Adj Close']

#print(indiceData.head())
