import numpy as np
import matplotlib.pyplot as plt

receitaEsperada = 170
desvioPadrao = 20
interacoes = 1000

receitasFuturas = np.random.normal(receitaEsperada, desvioPadrao, interacoes)
print(receitasFuturas)

plt.figure(figsize=(10, 6))
plt.plot(receitasFuturas)
plt.show()

cmv = - (receitasFuturas * np.random.normal(0.6, 0.1))

plt.figure(figsize=(10, 6))
plt.plot(cmv)
plt.show()

print(cmv.mean())
print(cmv.std())

lucroBruto = receitasFuturas + cmv
print(lucroBruto)

plt.figure(figsize=(10, 4))
plt.plot(lucroBruto)
plt.show()

print(max(lucroBruto))
print(min(lucroBruto))
print(lucroBruto.mean())
print(lucroBruto.std())

plt.figure(figsize=(10, 4))
plt.hist(lucroBruto, bins= 20)
plt.show()
