print("Seja bem-vindo(a) ao classificador de notas:\n ")
nota= float(input("Por favor, digite a nota "))
if nota <0 or nota>10: 
    print("Erro. Nota fora dos padrões")
    print("A nota deve estar no intervalo [0,10]\n")
else:
    if nota>=9 and nota <=10: print("Conceito A\n")
    if nota>=7 and nota <=8.9:print("Conceito B\n")
    if nota>=5 and nota <=6.9:print("Conceito C\n")
    if nota>=3 and nota <=4.9:print("Conceito D\n")