# Função com parametro
def retornaFive(x):
    x = 5
    return x
print(retornaFive(14))

# Fução sem parametro
def hello():
    return "Hello World"
print(hello())

#Funções nativas do python

# Classe da Variavel
print(type(10))

print(int(10.00))
print(float(10))
print(str("Gabriel"))
print(len("Gabriel Kaustchr"))#Retorna numero de caracteres

#Funções numéricas

print(max(100, 2000, 50, 15, 2, 0)) #Retorna o maior valor
print(min(100, 2000, 50, 15, 2, 0)) #Retorna o menor valor
print(abs(-50)) #Retorna o numero absoluto
soma = [1,2,3,4]
print(sum(soma)) #Retorna a soma da lista
print(round(3.14161592, 4)) #Aredonda para 4 digitos
print(pow(2, 8)) #Potencia
