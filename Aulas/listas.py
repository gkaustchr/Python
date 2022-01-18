participantes = ["Gabriel", "Rafael", "Daniel", "Joel"]
print(participantes)
print(participantes[1])
print(participantes[-1]) #Retorna o ultimo indice

participantes[-1] = "Josiel"
print(participantes)

del participantes[2]
print(participantes)

participantes.append("Joel")
print(participantes)

participantes.extend(["Daniel", "Gael"]) #Aumenta a lista com outra lista
print(participantes)

print("O primeiro participante é " + participantes[0] + ".")

print(len(participantes)) #Retorna o numero de elementos da lista

print(participantes[1:3]) #Retorna os valores no intervalo de 1 a 3

print(participantes[:2]) #Retorna os valores no intervalo de 0 a 2

print(participantes[-2:]) #Retorna os valores no intervalo de -2 a -1

print(participantes.index("Rafael")) #Retorna o indice do valor procurado

outrosNomes = ["Pedro", "Thiago", "João"]
todosNomes = [participantes, outrosNomes]
print(todosNomes)

participantes.sort() #Ordena a lista
print(participantes)

participantes.sort(reverse = True) #Ordena de forma inversa
print(participantes)

numerica = [10, 40, 30, 5, 18, 53]
print(numerica)
numerica.sort()
print(numerica)
numerica.sort(reverse = True)
print(numerica)
