import quandl
import pandas as pd

#myData = quandl.get("FRED/GDP")
#print(myData.head())
#print(myData.tail())

#Manipulando CSV
print("****  CSV  ****")
myData_01 = quandl.get("FRED/GDP")
myData_01.to_csv("recurso/Data_02_teste.csv") #Salvando um CSV

myData = pd.read_csv("recurso/Data_02.csv") #Importando CSV
print(myData.info())#Pegando informações do CSV
print(myData)  #Lendo CSV
print(myData.head())

#Manipulando EXCEL
print("****  EXCEL  ****")
#myData_02 = pd.read_csv("recurso/Data_02.csv") #Importando CSV
#myData_02.to_excel("recurso/Data_03_teste.xlsx") #Salvando um EXCEL

myData_02 = pd.read_excel("recurso/Data_03.xlsx") #Importando EXCEL
print(myData_02.head())  #Lendo EXCEL
