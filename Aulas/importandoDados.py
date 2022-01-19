import numpy as np
import pandas as pd

#Series
series = pd.Series(np.random.random(5), name="Coluna 01")
#print(series)

#DataFrame
from pandas_datareader import data as wb

acaoApple = wb.DataReader("OIBR4.SA", data_source="yahoo", start="2010-1-1") #AAPL é o ticket da ação desejada
print(acaoApple)
print(acaoApple.info()) #Informações do DataFrame
print(acaoApple.head()) #Informações das 5 primeiras linhas
print(acaoApple.tail()) #Informações das 5 ultimas linhas

print(acaoApple.head(10)) #Informações das 10 primeiras linhas
print(acaoApple.tail(20)) #Informações das 20 ultimas linhas
