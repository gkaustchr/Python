#Exercicio 1
#Saber quando gastei no mercado usando Dicionário e Loop

preco = {
    "Macarrao": 4.5,
    "Lasanha":  10.99,
    "Hamburguer": 12.99,
    "Arroz": 18.10,
}
quantidade = {
    "Macarrao": 4,
    "Lasanha":  2,
    "Hamburguer": 2,
    "Arroz": 1,
}

total = 0
for i in preco:
   total += preco[i] * quantidade[i]

print(total)
