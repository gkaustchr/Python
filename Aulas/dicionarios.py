#DICIONARIO TRABALHA COM CHAVE: VALOR

animais = {'a1':'Gato', 'a2':'Cachorro', 'a3':'Coelho', 'a4':'Pato', }
print(animais)
print(animais['a3'])

animais['a5'] = "Hamster"
print(animais)

animais['a4'] = "Calopsita"
print(animais)


#LISTAS DENTRO DE DICIONARIOS
empresa = {'dep1': 'Roger' , 'dep2' : ['Ruan', 'Maria', 'Elen']}
print(empresa['dep2'])
print(empresa)

dicionarioVazio = {} #Criando um dicionario vazio
dicionarioVazio['dep1'] = "Marcos"
dicionarioVazio['dep2'] = ["Pedro" , "Julia"]
print(dicionarioVazio)

print(dicionarioVazio.get('dep2')) #Buscar valores de uma chave

dicionarioVazio['dep2'].append("Juliana") #Adicionando itens a lista dentro do dicionario
print(dicionarioVazio['dep2'])
print(len(dicionarioVazio['dep2'])) #Retornando tamanho da lista
