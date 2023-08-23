import random

escolha= input("Escolha entre: 1-Pedra, 2-Papel e 3-Tesoura: \n")
jogada=random.randint(1,3)
jogada=random.choice(["Pedra","Papel","Tesoura"])
print(f"Computador escolheu: {jogada}")
if escolha==jogada:
    print("Empate")
elif escolha== "Pedra":
    if jogada== "Tesoura":
        print("Pedra quebra tesoura! Você ganhou")
    else:
        print("Papel cobre pedra! Você perdeu")
elif escolha== "Papel":
    if jogada== "Pedra":
        print("Papel cobre Pedra! Você ganhou")
    else:
        print("Tesoura corta Papel! Você perdeu")
elif jogada== "Papel":
    print("Tesoura corta Papel! Você ganhou")
else:
    print("Pedra quebra Tesoura! Você perdeu")