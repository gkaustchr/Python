import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt

data = pd.read_excel('../recurso/Housing.xlsx')
data.info()
print(data[['House Price', 'House Size (sq.ft.)']])

x = data['House Size (sq.ft.)']
y = data['House Price']

plt.scatter(x, y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size')
plt.show()

x1 = sm.add_constant(x)
reg = sm.OLS(y, x1).fit()
print(reg.summary())

#variaveis da regressao Linear
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(slope) #Inclinação Betta
print(intercept) #Intercepto Alpha
print(r_value ** 2) #R quadrado
print(p_value) #P
print(std_err) #Erro padrão

