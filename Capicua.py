numero= int (input("Informe o valor inteiro de 4 digitos "))
if numero <1111 or numero>9999: print("Valor inválido. O número digitado não está dentro do intervalo [1111,9999] ")
else:
    milhar = numero//1000
    resto=numero%1000
    centena=resto//100
    resto=resto%100
    dezena=resto//10
    unidade=resto%10
    invertido=unidade*1000 + dezena *100 + centena*10 + milhar

    print("Valor ao contráio: ",invertido)
    if numero ==invertido: print('Capicua')
    else:print("não é capicua")