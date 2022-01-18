def jurosSimples():
    #   Fórmula J = C × i × t
    #   M = C + J
    #   'Montante0' 'Juros1' 'Capital2' 'Taxa3' 'Tempo4'
    indice = 0
    result = 0
    formula = ['0', 'Juros1', "Capital2", "Taxa3", "tempo4"]
    formula[0] = input("Digite o valor do Montante se existir R$: ")
    formula[1] = input("Digite o valor do Juros Simples se existir R$: ")
    formula[2] = input("Digite o valor do Capital se existir R$: ")
    formula[3] = input("Digite a taxa %: ")
    formula[4] = input("Digite o tempo da aplicação: ")
    print(formula)

    for i in range(len(formula)):
        if(formula[i].isalpha()):
            indice = i
        elif(formula[i].isnumeric()):
            formula[i] = float(formula[i])
    print((formula[indice]))

    if(indice == 0):
        result = (formula[2] * (formula[3]/100) * formula[4]) + formula[2]
        print(result)
    if(indice == 1):
        result = (formula[2] * (formula[3]/100) * formula[4])
        print("Juros total foi de R$ {}".format(round(result,2)))
    if(indice == 2):
        if(formula[1] == 0):
            result = formula[0] / ((formula[3]/100) * formula[4] + 1)
            print("O capital aplicado foi de R$ {}".format(round(result,2)))
        else:
            result = formula[0] - formula[1]
            print("O capital aplicado foi de R$ {}".format(round(result,2)))

    if(indice == 3):
        if(formula[0]==0):
            result = formula[1] / (formula[2] * formula[4])
            print("A taxa de juros aplicada foi de {}%".format(round(result*100,2)))
    if(indice == 4):
        if(formula[0]==0):
            result = formula[1] / (formula[2] * formula[3])
            print("O tempo de aplicação foi de {} meses".format(round(int(result*100),0)))


def jurosCompostos():
    print("Juros Simples")
def taxaJuros():
    print("Juros Simples")
def pagamentoPostecipados():
    print("Juros Simples")

def funcoes(i):
    if i == 1:
        jurosSimples()
    if i == 2:
        jurosCompostos()
    if i == 3:
        taxaJuros()

menu = int(input("Escolha a Conta: \n"
                 "1 - Juros Simples\n"
                 "2 - Juros Compostos\n"
                 "3 - Taxa de Juros\n"
                 "4 - Pagamento Antecipado\n"
                 "Escolha o número da Operação: "))
funcoes(menu)


