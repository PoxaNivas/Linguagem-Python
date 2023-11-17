import random

#Função aleatória com int
for c in range(3):
    N1= random.randint(0,9)
    print(f" Número inteiro aleatório: {N1}")
print("\n")

#Função aleatória com fluatuantes
for c in range(3):
    N2= random.uniform(0,1)
    print(f" Número fuatuante aleatório: {N2:.3f}")
print("\n")

#Função aleatória com palavras
lista_op = ["maça","banana","Pitaya"]
for c in range(4):
    op= random.choice(lista_op)
    print(f"Palavra aleatória sorteada: {op}")
print("\n")

#Função para medir o tamanho da string
aux = input("Digite uma palavra: ")
print(f"O tamano da palavra é:{len(aux)}")
print(f"O tamano da lista é:{len(lista_op)}")

