numero = [1,2,3,4,5,6,7,8,9,10]
for n in range(0, len(numero)):
    z = numero[n]
    y = round((z * 1.8392), 2)
    print(y)

#Loop trabalhando com Listar
for num in range(len(numero)):
    print(numero[num])


#Mostrar numeros pares
for x in range(12):
    msg = ""
    if x % 2 == 0:
        print(x)
    else:
        print(" impar ")

