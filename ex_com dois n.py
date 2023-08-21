import math

n1= float (input ("Por favor, digite o valor de N1: "))
n2= float (input ("Por favor, digite o valor de N2: "))
soma= n1+n2
media= (n1+n2)/2
diferenca= n1-n2
distancia= math.fabs(n1-n2)
maior_n= (n1+n2+distancia)/2
menor_n= (n1+n2-distancia)/2
print(" A soma dos dois números é ",soma)
print(" A média dos dois números é ",media)
print(" A diferença entre os dois números é ",diferenca)
print(" A distância dos dois números é ",distancia)
print(" O maior número dos dois números é ",maior_n)
print(" O menor número dos dois números é ",menor_n)