import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers  = ['PG', 'MSFT', 'F', 'GE']
myData = pd.DataFrame()
for t in tickers:
    myData[t] = wb.DataReader(t, data_source = 'yahoo', start = '1995-1-1')['Adj Close']
myData.info()
print(myData.head())
print(myData.tail())

print(myData.iloc[0]) #Extrai os dados da primeira linha

#Colocar na base 100
(myData / myData.iloc[0] * 100).plot(figsize=(10, 4))
#plt.show()

#Mostrando sem ajustar o valor inicial
myData.plot(figsize = (10, 4))
#plt.show()

#Buscar pelo rotulo
print(myData.loc['2022-1-13'])

#Buscar pela linha
print(myData.iloc[0])

#Retorno simples das ações
retornoSimples = (myData / myData.shift(1)) - 1
print(retornoSimples.head())

weights = np.array([0.25, 0.25, 0.25, 0.25])
print(np.dot(retornoSimples, weights))  #Multiplicando as matrizes ( Valor * Peso)

retornoAnual = retornoSimples.mean() * 250
print(retornoAnual)

print(np.dot(retornoAnual, weights))

retornoAnualCarteira = str(round(np.dot(retornoAnual, weights), 4) * 100) + '%'
print(retornoAnualCarteira)

#Retorno da Carteira com pesos diferentes
weights2 = np.array([0.4, 0.4, 0.05, 0.15])
retornoAnualCarteira2 = str(round(np.dot(retornoAnual, weights2), 4) * 100) + '%'
print(retornoAnualCarteira2)
