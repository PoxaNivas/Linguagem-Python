#Sobre Strings e concatenação
texto = input("Digite um texto: \n")
texto2 = input("Digite o segundo texto: \n")
print("Junção dos dois textos:", texto+" " +texto2)
print("Repetição dos textos",9*(texto+"espaço"))

#Sobre Strings e fatiamento
nome=input("Digite seu nome completo: \n")
fatiamento=nome.split()
tamanho=len(fatiamento)
print("Sobrenome:",fatiamento[1])