mes=int(input("Por favor, informe o mês: "))
if mes ==2:
    dias=28
elif mes==4 or mes==6 or mes ==9 or mes==11:
    dias=30
else:
    dias=31
print(f"Total de dias: {dias}")