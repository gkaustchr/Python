import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['PG', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']

secLogRetorn = np.log(data / data.shift(1))

cov = secLogRetorn.cov() * 250
#print(cov)

covComMercado = cov.iloc[0, 1]
#print(covComMercado)

varDoMercado = secLogRetorn['^GSPC'].var() * 250
#print(varDoMercado)

pgBetta = covComMercado / varDoMercado
#print(pgBetta)

pgRetornEsp = 0.025 + pgBetta * 0.05
print(pgRetornEsp)
