import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

acaoApple = wb.DataReader("AAPL", data_source="yahoo", start="2000-1-1")
print(acaoApple.head())

# Formulado do Retorno Logaritmico é  log(Preço_Fechamento / Preço_Fechamento_Anterior)
acaoApple['log_return'] = np.log(acaoApple['Adj Close'] / acaoApple['Adj Close'].shift(1))
print(acaoApple['log_return'])

#Grafico
acaoApple['log_return'].plot(figsize=(8, 5))
plt.show()

#Taxa de retorno médio Logaritmico
logRetornoDiario = acaoApple['log_return'].mean()
print(logRetornoDiario)

logRetornoAnual = acaoApple['log_return'].mean() * 250
print(logRetornoAnual)

logRetornoAnualFinal = str(round(logRetornoAnual, 4) * 100) + '%'
print(logRetornoAnualFinal)
