import random

#Gerando numeros aleatorios ente 0 e 1
prob = random.random()
print(round(prob, 4))


#Gerar numero aleatorios inteiros determinados
dado = random.randint(1, 6)
print(dado)


#Gerar um array de numeros aleatorios determinados
import numpy as np

array = np.random.randint(1, 7, (3,3))
print(array)
