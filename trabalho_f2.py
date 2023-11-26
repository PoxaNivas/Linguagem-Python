import matplotlib.pyplot as plt

#Listas
data_l=[];precip= [];temp_max = [];temp_min = [];h_inso=[];temp_med=[];umid = [];vel = []

#variáveis
mes_i=0; ano_i=0
mes_f=0; ano_f=0

#Função para validar intervalo da data
def validar_data():
    aux= True
    while aux==True:
        data= input("Digite o mês e o ano MM/AAAA\n")
        aux= data.split("/")
        mes= int (aux[0])
        ano= int (aux[1])
        if mes <1 or mes>12 or ano <1961 or ano> 2016:
            print("\nData informada está fora do dataset\n")
            aux= True
        else:
            aux= False
    return mes,ano

#Parte inicial e validação de entrada
print("\n")
print("Seja bem-vindo(a) ao programa de dados meteorológicos \n")
print("Primeiramente, digite o mês e ano inicial: \n")
mes_i,ano_i=validar_data()

print("\n Agora digite o mês e ano final:\n")
mes_f,ano_f=validar_data()

with open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r") as data:
    cab= data.readline()
    print(cab)
    for c in data:
        valores = c.split(",")
        dat= valores[0][3:10]
        data=dat.split("/")
        data1= (int(data[0]), int(data[1]))
        print("Carregou os dados")
        print(f"Valores data 1: {data1[0]},{data1[1]}")
        if mes_i == data1[0] and ano_i==data1[1] or mes_f==data1[0] and ano_f==data1[1] :
            print("Entrou no if")
            aux= valores[0]
            data_l.append(aux)
            aux= (float (valores[1]))
            precip.append(aux)
            aux= (float (valores[2]))
            temp_max.append(aux)
            aux= (float (valores[3]))
            temp_min.append(aux)
            aux= (float (valores[4]))
            h_inso.append(aux)
            aux= (float (valores[5]))
            temp_med.append(aux)
            aux= (float (valores[6]))
            umid.append(aux)
            aux= (float (valores[7]))
            vel.append(aux)

#Visualização de intervalos em modo texto
print("Digite a opção de visualização desejada:\n")
print(" 1) todos os dados, \n 2) apenas os de precipitação, \n 3) apenas os de temperatura, \n 4) apenas os de umidade e vento para o período informado. \n")
op = int (input())
print(f"Mês inicial: {mes_i}, ano inicial {ano_i}, mês final {mes_f} e ano final {ano_f}")

if op== 1:
    for c in range(len(precip)):
        print(f"Contagem {c}")
        print(data_l[c],"|",precip[c],"|",temp_max[c],"|")


#Gráfico
'''
if op == 1:
    plt.title("Gráfico com todos os dados")
    plt.plot()
elif op ==2:
    plt.title("Gráfico de precipitação")
    plt.plot(precip, label ="linha de exemplo")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.show()
    plt.legend()
elif op ==3:
    plt.plot(temp_med)
elif op ==4:
    plt.plot(umid,vel)



'''
