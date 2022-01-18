import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'BEI.DE']

secData = pd.DataFrame()

for t in tickers:
    secData[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1')['Adj Close']

print(secData.tail())

secRetornoLog = np.log(secData / secData.shift(1))
print(secRetornoLog)

#Calcular a variancia da PG
print('Variança P&G')
print(secRetornoLog['PG'].var()) #Var calcula a variancia
print(secRetornoLog['PG'].var() * 250)

print('Variança Beiersdorf')
print(secRetornoLog['BEI.DE'].var())
print(secRetornoLog['BEI.DE'].var() * 250) #Calcula a variancia Anual


#Calculando a Covariancia
print('Covariânça PG x BEI.DE')
print(secRetornoLog.cov())
print(secRetornoLog.cov() * 250) #Calcula a covariancia anual

#Calculando a Covariancia com metodo Corr
print('Covariânça PG x BEI.DE com o metodo Corr')
print(secRetornoLog.corr()) #Correlação


