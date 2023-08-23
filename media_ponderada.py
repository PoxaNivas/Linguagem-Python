n1= float(input("Por favor, digite a primeira nota: "))
n2= float(input("Por favor, digite a segunda nota: "))
n3= float(input("Por favor, digite a terceira nota: "))

if n1 <0 or n1>10:
    print("Erro. A primeira nota fora do intervalo de 0 a 10")
if n2 <0 or n2>10:
    print("Erro. A segunda nota fora do intervalo de 0 a 10")
if n3 <0 or n3>10:
    print("Erro. A terceira nota fora do intervalo de 0 a 10")
else:
    maior=n1
    if n2>maior:maior=n2
    if n3>maior:maior=n3
total=maior*+0.5+0.25*(n1+n2+n3-maior)
print("A média é ",total)