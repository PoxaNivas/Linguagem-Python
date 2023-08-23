ano= int (input("Por favor, informe o ano de referência: "))
mes= int (input("Por favor, agora digite o mês de refência: "))
if mes <1 or mes>12:
    print("Mês inválido. Por favor, digite um valor dentro do intervalo [1,12]")
else:
    if (ano%4==0 and ano%100!=00) or (ano%400==0):
        if mes==2:
            print("Ano: 366 dias. Mês: 29 dias. ")
        elif mes== 4 or mes== 6 or mes== 9 or mes==11:
            print("Ano: 366 dias. Mês: 30 dias. ")
        else:
            print("Ano: 366 dias. Mês: 31 dias. ")
    else:
        if mes==2:
            print("Ano: 365 dias. Mês: 28 dias. ")
        elif mes== 4 or mes== 6 or mes== 9 or mes==11:
            print("Ano: 365 dias. Mês: 30 dias. ")
        else:
            print("Ano: 365 dias. Mês: 31 dias. ")
