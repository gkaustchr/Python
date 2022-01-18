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


#Analise PG
print("P&G")
print(secRetornoLog['PG'].mean())
print(secRetornoLog['PG'].mean() * 250)
print(secRetornoLog['PG'].std()) #Calcula o Desvio Padrão diário
print(secRetornoLog['PG'].std() * 250 ** 0.5) #Fazendo a potencia de 250, Pq o desvio padrão é a Raiz quadrada da variancia

#Analisando a Beiersdorf
print("Beiersdorf")
print(secRetornoLog['BEI.DE'].mean())
print(secRetornoLog['BEI.DE'].mean() * 250)
print(secRetornoLog['BEI.DE'].std()) #Calcula o Desvio Padrão Diario
print(secRetornoLog['BEI.DE'].std() * 250 ** 0.5) #Desvio Padrão Anual, lembrando de executar a potencia de 250 pra achar o desvio Padrão da variancia


#Analisando as duas Ações
print('Analisando ...')
print('Analisando a Média Anual...')
print(secRetornoLog[['PG', 'BEI.DE']].mean() * 250)

print('Analisando o Desvio Padrão Anual...')
print(secRetornoLog[['PG', 'BEI.DE']].std() * 250 ** 0.5 )
