#TUPLAS SÃO IMUTAVEIS! NÃO PODE ALTERAR OU EXCLUIR ELEMENTOS

num = (10, 20, 30, 40, 50, 60, 70)
print(num)

nume = 10, 11, 12, 13, 14, 15, 16
print(nume)

lista = [num, nume] #Lista de Tuplas
print(lista)

(idade, peso) = "24,70.2".split(',') #Cria um tupla com itens separados por virgulas
print(idade)
print(peso)


#FUNÇÃO QUE RETORNA VARIOS VALORES COM TUPLAS
def areadoQuadrado(x):
    a = pow(x, x)
    p = x * 4
    print("Calculando . . .")
    return a,p
(area, perimetro) = areadoQuadrado(4) #Colocando retorno em tuplas
print(area)
print(perimetro)
