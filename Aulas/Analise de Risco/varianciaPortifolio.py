import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'BEI.DE']

secData = pd.DataFrame()

for t in tickers:
    secData[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1')['Adj Close']
secRetornoLog = np.log(secData / secData.shift(1))

#Protifolio de apenas 2 empresa e com a mesma porcentagem

print('Variância do Portifólio')
weights = np.array([0.5, 0.5]) #Colocando pessoas para as ações  = 50% para cada ação
portfVarianca = np.dot(weights.T, np.dot(secRetornoLog.cov() * 250, weights))
print(str(round(portfVarianca, 4) * 100) + '%')

print('Volatilidade do Portifólio')
portfVolatilidade  = (np.dot(weights.T, np.dot(secRetornoLog.cov() * 250, weights))) ** 0.5
print(str(round(portfVolatilidade, 4) * 100) + '%')
