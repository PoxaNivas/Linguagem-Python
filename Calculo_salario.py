#entradas
salario_b=float(input("Por favor, digite seu salário bruto: "))
dep= int(input("Por favor, informe a quantidade de dependentes: "))

#cálculos INSS
if salario_b <=1.212:
    inss=(salario_b*0.075)
elif salario_b <=2427.35:
    inss=(salario_b*0.09)-18.18
elif salario_b <=3641.03:
    inss=(salario_b*0.12)-91
elif salario_b <=7087.22:
    inss=(salario_b*0.14)-163.82
else:
    inss=828.39


#Cálculos IRRF
base=(salario_b-inss)- (dep*189.59)
if base <=1903.98:
    irrf=0
elif base <=2826.65:
    irrf=(base*0.075)-142.80
elif base <=3751.05:
    irrf=(base*0.15)-354.80
elif base <=4664.68:
    irrf=(base*0.225)-636.16
else:
    irrf=(base*0.275)-869.36

#Salário líquido
salario_l= (salario_b-inss)-irrf

#Saídas
#Desconto do INSS
#Desconto do IRRF


print(f"O salário ficou:{salario_l} ")
print(f"O desconto do INSS resultou em: {inss}")
print(f"O desconto do IRRF resultou em: {irrf}")
