#Exercícios sobre listas

lista = []
lista1= ['a','b','c']

print(lista)
print(lista1)

print("Adicionando elementos a lista")
lista= lista+[1]
print(lista)

print("Concatenando listas")
lista2=lista+lista1
print(lista2)
lista3=["o"]

print("Multiplicando elementos da lista")
lista3*=3
lista3.append("mas que calor")
print(lista3)

print("Teste lógico com a lista")
if ("d" in lista1):
    print("achou")
else:
    print("Elemento não encontrado")

print("Excluindo elementos da lista")
lista3.pop(1)
print(lista3)

#Operações em listas
lista4=[1,2,3,4,5,680,6,5,55,0]
print(f"Lista atual{lista4}")

print("Soma dos números:")
soma=sum(lista4)
print(soma)

print("Maior número: ")
mai_n=max(lista4)
print(mai_n)

print("Menor número")
men_n=min(lista4)
print(men_n)

print("Números ordenados")
lista4.sort()
print(lista4)

print("Números ordenados de forma decrescente")
lista4.reverse()
print(lista4)