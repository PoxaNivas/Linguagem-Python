import math


#impares
for cont in range(21):
    if cont%2==1:
        continue
    else:
        print(cont)

#crescente
print("\n")
print("Crescente")
for cont in range(0,11):
    print(cont)

#decrescente
print("\n")
print("Descrescente")
for cont in range (10,0,-1):
    print(cont)
print("\n")
for cont in range(0,51):
    print(f"{cont:5}: sua raiz quadrada {math.sqrt(cont):.3f}")

