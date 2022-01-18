import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

acaoApple = wb.DataReader("AAPL", data_source="yahoo", start="2000-1-1")
print(acaoApple.head())

#Criando a Coluna "Retorno Simples com o Valor de Hoje / Valor de Ontem - 1
# Formula = (Adj Close / Adj Close(n-1) - 1
#shift(1) é a quantidade de linhas que o codigo deve retornar para pegar o valor
acaoApple["Retorno Simples"] = (acaoApple["Adj Close"] / acaoApple["Adj Close"].shift(1)) - 1
print("______ TAXA DE RETORNO HISTÓRICO DA APPLE desde 2000 ____________")
print(acaoApple["Retorno Simples"].head(20))

#Gerar um grafico dos dados
acaoApple["Retorno Simples"].plot(figsize=(8, 5))
plt.show()

#Calcular o retorno médio da Taxa de Retorno Simples
mediaRetornoSimples = acaoApple["Retorno Simples"].mean()
print("Média de Retorno Simples é: {}" .format(round(mediaRetornoSimples, 4)))

#Multiplicando o retorno médio diário para ANUAL (Ano tem 252 dias uteis)
mediaRetornoSimplesAnual = acaoApple["Retorno Simples"].mean() * 252
print("Média do Retorno Simples Anual é: {}%" .format(round(mediaRetornoSimplesAnual * 100, 4)))
