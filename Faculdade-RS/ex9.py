#Refazer para fixar
#recebimento dos dados e gravação em arquivo
g_arq=open("alturas.txt","w")
for c in range(3):
    nome= input("Qual é o seu nome: ")
    altura= float(input("Qual a sua altura: "))
    g_arq.write(nome+"-"+str(altura)+"\n")
g_arq.close()


#Leitura dos dados e conversão
lista=[]
soma=0
N_maior=""
Maior=0
l_arq=open("alturas.txt","r")
for c in l_arq:
    saida= c[:-1].split("-")
    nome=saida[0]
    altura=float(saida[1])
    dados=(nome,altura)
    soma+=altura
    lista.append(dados)
    print("print da lista")
    print(lista)
    media=soma/len(lista)
    if(altura>=media):
        Maior=altura
        N_maior=nome
        
print(f"A pessoa mais alta se chama: {N_maior} com {Maior} de altura")

#testes lógicos

