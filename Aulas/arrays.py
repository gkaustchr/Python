import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)
print(a.shape) #Mostra quantidade de (linhas, colunas) do array
(linha, coluna) = a.shape #passa o valor de linha e coluna separados

print("Linha")
print(linha)

print("Coluna")
print(coluna)

print(a[0, 2])
a[0, 2] = 0
print(a)
a[0, 2] = 3

#mostra apenas as linas
print(a[0])
print(a[1])
print(a[2])
