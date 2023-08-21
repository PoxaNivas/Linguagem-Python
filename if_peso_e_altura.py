print("Calculador de peso ideal \n")
print("Por favor, informe seu gênero. 1- Masculino, 2- Feminino ")
sexo= int(input())
altura= float(input("Por favor, digite sua altura "))
if(sexo==1):
    peso_ideal=(altura*72.7)-58
    print("Seu peso ideal é: ",peso_ideal)
if(sexo==2):
    peso_ideal=(altura*62.1)-44.7
    print("Seu peso ideal é: ",peso_ideal)
if(sexo!=1 and sexo!=2):
    print("Resposta inválida. Peso não calculado.")