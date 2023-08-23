print("Programa de IMC")
altura= float(input("Por favor,digite sua altura: "))
peso= float(input("Por favor,digite seu peso:  (em KG)"))
IMC= peso/(altura**2)
print(f"Seu IMC é {IMC}")

if IMC <=18.6:
    print("Abaixo do peso")
elif IMC <25:
    print("Peso ideal")
elif IMC <30:
    print("Sobrepeso")
elif IMC <35:
    print("Obesidade grau I")
elif IMC <40:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")