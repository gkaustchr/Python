import pandas as pd
import quandl

print("CSV ______")
myData = pd.read_csv("recurso/Data_02.csv")
print(myData)

myData = pd.read_csv("recurso/Data_02.csv", index_col="Date")
#Alterando Data para a primeira coluna no lugar do ID gerado pelo Python
print(myData)


print("EXCEL ______")
myData03 = pd.read_excel("recurso/Data_03.xlsx")
print(myData03)

myData03 = myData03.set_index("Year")
#Alterando o index para o YEAR
print(myData03)
