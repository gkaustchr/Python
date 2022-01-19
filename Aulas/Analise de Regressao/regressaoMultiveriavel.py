import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_excel('../recurso/Housing.xlsx')
#print(data.head())

# Variaveis independentes
x = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']]
y = data['House Price']

x1 = sm.add_constant(x)
reg = sm.OLS(y, x1).fit()
print(reg.summary())

# Variaveis independentes sem o Ano de Construção
x = data[['House Size (sq.ft.)', 'Number of Rooms']]
x1 = sm.add_constant(x)
reg = sm.OLS(y, x1).fit()
print(reg.summary())

# Variaveis independentes sem o Numero de quartos
x = data[['House Size (sq.ft.)', 'Year of Construction']]
x1 = sm.add_constant(x)
reg = sm.OLS(y, x1).fit()
print(reg.summary())

# Variaveis independentes sem o tamanho
x = data[['Number of Rooms', 'Year of Construction']]
x1 = sm.add_constant(x)
reg = sm.OLS(y, x1).fit()
print(reg.summary())
