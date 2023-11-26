# Entradas
temp= 0
temp_m = 0

q_quente = 0
mes_quente = 0

temp_quente = 0
mes_frio = 0
temp_frio = 38

#validação
for cont in range(12):
    mes = int(input(f"Por favor, digite o número mês (de 1 a 12) : "))
    if mes < 1 or mes > 12:
        print("\nMês fora do intervalo [1,12]\n")
        mes = int(input(f"Por favor, redigite o somente número do mês (de 1 a 12) :\n "))
    temp = float(input("Por favor, digite a temperatura: "))
    if temp < -60 or temp > 50:
        print("\nTemperatura inválida. Valor informado está fora do intervalo [-60ºC,50ºC] \n")
        temp = float(input("Por favor, redigite somente a temperatura: "))

#analise
    temp_m += temp
    if temp > 38:
        q_quente+= 1
        aux = temp
        if temp_quente < aux:
            temp_quente = aux
            mes_quente = cont
    else:
        aux = temp
        if temp_frio>aux:
            temp_frio = aux
            mes_frio = cont

temp_m = (temp_m/12)
print(f"Temperatura média anual: {temp_m:.2f}")
print(f"No intervalo informado tiveram: {q_quente} dias que ultrapassaram 38º graus")

if mes_frio == 0:
    print(f"Janeiro foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 1:
    print(f"Fevereiro foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 2:
    print(f"Março foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 3:
    print(f"Abril foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 4:
    print(f"Maio foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 5:
    print(f"Junho foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 6:
    print(f"Julho foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 7:
    print(f"Agosto foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 8:
    print(f"Setembro foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 9:
    print(f"Outubro foi o mês mais frio, temperatura: {temp_frio}")
elif mes_frio == 10:
    print(f"Novembro foi o mês mais frio, temperatura: {temp_frio}")
else:
    print(f"Dezembro foi o mês mais frio, temperatura: {temp_frio}")

# analise mes_frio
if mes_quente == 0:
    print(f"Janeiro foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 1:
    print(f"Fevereiro foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 2:
    print(f"Março foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 3:
    print(f"Abril foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 4:
    print(f"Maio foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 5:
    print(f"Junho foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 6:
    print(f"Julho foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 7:
    print(f"Agosto foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 8:
    print(f"Setembro foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 9:
    print(f"Outubro foi o mês mais quente, temperatura: {temp_quente}")
elif mes_quente == 10:
    print(f"Novembro foi o mês mais quente, temperatura: {temp_quente}")
else:
    print(f"Dezembro foi o mês mais quente, temperatura: {temp_quente}")
