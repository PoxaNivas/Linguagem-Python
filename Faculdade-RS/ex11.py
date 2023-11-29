import matplotlib.pyplot as plt
#gráfico de linha
#Dados

x = [0,1,2,3,4,5]
y = ['Marry Kay','Avon','Jequiti','Natura','Boticário','VIP']

print("Gerador de gráficos")
op = int (input("Escolha a opção desejada 1-gráfico em linha ou 2- gráfico em barra: \n"))
if (op==1):
    plt.title("Gráfico em linha")
    plt.plot(x,label="linha exemplo 1")
    plt.legend()
    plt.show()
else:
    plt.bar(x,y,color="blue",label="barras exemplo")
    plt.xlabel("Quantidade")
    plt.ylabel("Produto escolhido")
    plt.show()