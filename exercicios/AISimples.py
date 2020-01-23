import pandas as pd

arquivo = pd.read_excel(r'D:\Kaustchr\Documentos\acao.xlsx')
arquivo.head()
#Reescrever 1 no lugar de Subiu e 0 no lugar de Caiu
arquivo['Ticket'] = arquivo['Ticket'].replace('CSNA3', 6)
arquivo['Situacao'] = arquivo['Situacao'].replace('CAIU', 0)
arquivo['Situacao'] = arquivo['Situacao'].replace('SUBIU', 1)
arquivo['Percentual'] = arquivo['Percentual'].replace('-', 0)
arquivo.head()

#Cria uma coluna so com a Situacao
situacao = arquivo['Situacao']
#Cria a tabela sem a coluna Situacao
tabela = arquivo.drop('Situacao', axis = 1)
print(situacao)
print(tabela)

from sklearn.model_selection import train_test_split

#Criando a porcentagem de teste e  de treino
tabela_treino, tabela_teste, situacao_treino, situacao_teste = train_test_split(tabela, situacao, test_size = 0.2)

from sklearn.ensemble import ExtraTreesClassifier
#Fazendo o treino
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(tabela_treino, situacao_treino)
#Exibindo resultado
resultado = modelo.score(tabela_teste, situacao_teste)
print("Porcentagem de Acerto: ", resultado)

situacao_teste[10:100]
tabela_teste[10:100]

#Testar se a AI está funcionando
previsoes = modelo.predict(tabela_teste[2:10])
print(previsoes)
print(situacao_teste[2:10])