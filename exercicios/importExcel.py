import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"D:\Kaustchr\Documentos\acao.xlsx")
print(x)
#Grafico de Pontos
plt.plot(x['Date'], x['Open'])
plt.title(x['Ticket'][1])
plt.show()

#Grafico de Barras
plt.hist( x['Open'], bins = 10)
plt.title(x['Ticket'][1])
plt.show()


#Grafico de Pizza
plt.pie(x['Open'])#labels="nome da fatia"
plt.title(x['Ticket'][1])
plt.show()








