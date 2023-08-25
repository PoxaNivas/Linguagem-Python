texto1= input("Digite uma frase: ")
texto2= input("Digite uma palavra: ")
if texto2 in texto1:
    print(f"{texto2} está na frase")
else:
    print(f"{texto2} não está na frase ")

print(f"O comprimento da frase é {len(texto1)}")
print("Posições do texto e seus respectivos caracteres ")
print(f"Posição 0 {texto1[0]}")
print(f"Posição -1 {texto1[-1]}")
for caractere in (texto1):
    print(caractere)

for pos in range(len(texto1)):
    print(f"{pos}: {texto1[pos]}")