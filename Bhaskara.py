import math

a=float (input("Por favor digite o valor de A: "))
b=float (input("Por favor digite o valor de B: "))
c=float (input("Por favor digite o valor de C: "))

delta=(math.pow(b,2)-4*a*c)
if delta<0:
    print("Não há raízes reais")
else:
    if delta==0:
        x=-b/(2*a)
        print(f"Raiz é {x}")
    else:
        x1=(-b-math.sqrt(delta))/(2*a)
        print("X1 ",x1)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("X2 ",x2)
