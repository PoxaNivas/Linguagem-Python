n1= int (input("Por favor, digite um número "))
aux1=n1//1000 
aux2=(n1-aux1*1000)//100
aux3=((n1-aux1*1000)-aux2*100)//10
aux4=(((n1-aux1*1000)-aux2*100)-aux3*10)//1
inverso= int (aux4*1000+aux3*100+aux2*10+aux1*1)
print("O inverso é ", inverso)

"""
Outra possibilidade (professora)
valor= int (input())
milhar= valor//1000
resto=valor%1000
centena= resto//100
resto= resto%100
dezena=resto//10
resto=resto%10
unidade=resto//10

"""

"""
"""