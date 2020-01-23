import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"D:\Kaustchr\Documentos\acao.xlsx")
print(x)
plt.plot(x['Date'], x['Open'])
plt.title(x['Ticket'][1])
plt.show()








