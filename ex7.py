#sobre introdução a gravação em arquivos

print("Teste utilizando arquivos externos.")
ref_arquivo= open ("dados.txt","a")
cont=1
while cont<=3:
    nome = input ("Informe o nome: ")
    ref_arquivo.write(nome+"\n")
    cont=cont+1
ref_arquivo.close()
'''' 
#leitura de arquivos utilizando o read
#A função read() é usada para ler todo o conteúdo de um arquivo como uma única string. Ela não leva argumentos e lê desde a posição atual do cursor até o final do arquivo. Por exemplo:
print("Leitura de dados utilizando o read: \n")
with open("dados.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#leitura de arquivos utilizando o readlines
#A função readlines() lê todas as linhas do arquivo e retorna uma lista onde cada elemento é uma linha do arquivo. Por exemplo
print("Leitura de dados utilizando o readlines: \n")
with open("dados.txt","r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)
'''
#leitura de arquivos utilizando o for
print("Leitura de dados: \n")
ref_arquivo=open("dados.txt","r")
for linha in ref_arquivo:
    print(linha)
ref_arquivo.close()