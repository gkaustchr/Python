import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['PG', 'BEI.DE']

secData = pd.DataFrame()

for t in tickers:
    secData[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1')['Adj Close']
secRetornoLog = np.log(secData / secData.shift(1))

#Protifolio de apenas 2 empresa e com a mesma porcentagem
weights = np.array([0.5, 0.5])

portfVarianca = np.dot(weights.T, np.dot(secRetornoLog.cov() * 250, weights)) #variancia do portifolio
#Risco diversificavel  = variância do portifolio - variância anual ponderada

print('Variância da P&G')
print(secRetornoLog[['PG']].var() * 250)
pgVariancia = secRetornoLog['PG'].var() * 250

print('Variância da BEIERSDORF')
print(secRetornoLog[['BEI.DE']].var() * 250)
beideVariancia = secRetornoLog['BEI.DE'].var() * 250

print("Risco Diversificavel do Portifólio")
riscoDiversificavel = portfVarianca - (weights[0] ** 2 * pgVariancia) - (weights[1] ** 2 * beideVariancia)
print(str(round(riscoDiversificavel * 100, 4)) + '%')


#Risco não diversificavel ou sistematico
print('Risco não diversificavel')
riscoNaoDiversificave = portfVarianca - riscoDiversificavel #Usando o risco Diversificavel para achar o risco não diversificavel
print(riscoNaoDiversificave)

print('Risco Não Diversificavel')
riscoNaoDiversificave = (weights[0] ** 2 * pgVariancia) + (weights[1] ** 2 * beideVariancia)
print(riscoNaoDiversificave)
