#Ler um arquivo externo com delimitador

c=0
print("Programa para ler um arquivo externo com delimitador: ")
arquivo= open("planta_iris.data","r")
arq= open("dados1.txt","w")

dados=[]
for linha in arquivo:
    valores= linha.split(',')
    c+=1
    if(c>1):
        ultima = valores [4][:-1]
        #tupla com todos os dados 
        tupla= (float (valores[0]),float (valores[1]),float (valores[2]),float (valores[3]),ultima)
        print(tupla)

        #tupla só com valores para cálculos
        tupla_c=(float (valores[0]),float (valores[1]),float (valores[2]),float (valores[3]))
        print(tupla_c)
        dados.append(tupla_c)
'''
print("\n")
print("Print da tupla c")
for linha in dados:
    for c in range(4):
        arq.write(linha[c])
arquivo.close()
'''

print("\n")
print("Print da tupla c")
for linha in dados:
    for c in range(4):
        arq.write(str(linha[c])+",")
    arq.write("\n")
arquivo.close()


