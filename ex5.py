#Funções

def Tabuada():
    '''Função usada para multiplicar números digitados pelo user'''
    i = int(input("Digite o número inicial\n"))
    f = int(input("Digite o número final\n"))
    for c in range (i,f):
        print("\n")
        for d in range(1,11):
            print(f"{c} X {d} =",c*d)

def adiciona():
    '''Função usada para realizar adição de números digitados pelo user. A mesma estrutura pode ser usada para multiplicação e divisão, desde que seja realizado ajustes para os casos especiais'''
    a=int (input("Por favor, digite o primeiro número: \n"))
    b=int (input("Por favor, digite o segundo número: \n"))
    print(f"{a} + {b} =",a+b)

def subtrai():
    a=int (input("Por favor, digite o primeiro número: \n"))
    b=int (input("Por favor, digite o segundo número: \n"))
    print(f"{a} - {b} =",a-b)

print("Seja bem-vindo(a) a calculadora do Nih\n")
op = int (input("Escolha uma opção: 1- Tabuada 2- Adição 3- Subtração\n"))
print(op)
if(op==1):
    Tabuada()
elif(op==2):
    adiciona()
elif(op==3):
    subtrai()
else:
    print("Opção inválida.")
