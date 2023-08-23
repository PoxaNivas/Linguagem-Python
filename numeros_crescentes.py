n1= int (input("Por favor, digite o primeiro número: "))
n2= int (input("Por favor, digite o segundo número: "))
n3= int (input("Por favor, digite o terceiro número: "))

maior=n1
if n2>maior:maior=n2
if n3>maior:maior=n3

menor=n1
if n2<menor:menor=n2
if n3<menor:menor=n3

meio=n1
if n2>menor and n2<maior:meio=n2
if n3>menor and n3<maior:meio=n3


print("Os números digitados em ordem crescente são: ",menor,meio,maior)
print("Os números digitados em ordem descrente são: ",maior,meio,menor)