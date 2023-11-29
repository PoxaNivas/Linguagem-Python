import matplotlib.pyplot as plt

#Listas que serão utilizadas na preparação dos dados
dados=[];data_l=[];precip= [];temp_max = [];temp_min = [];h_inso=[];temp_med=[];umid = [];vel = [];temp_mes_grafico = [];ano_grafico=[]

#variáveis inputs do user
mes_i=0; ano_i=0
mes_f=0; ano_f=0
op=0; ano=0

#dicionário
dados_chuvoso = {}
temp_mes= {}
dados_temp_min={}

#Função para carga e preparação dos dados
def carga_dados():
    with open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r") as data:
        cab= data.readline()
        print(cab)
        for c in data:
            valores = c.split(",")
            dat= valores[0][3:10]
            data=dat.split("/")
            data1= (int(data[0]), int(data[1]))
            if mes_i <= data1[0] <= mes_f and ano_i <= data1[1] <= ano_f:
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
        return dados

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

#Função para definir o mês mais chuvoso
def mes_chuvoso():
    #dicionário
    with open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r") as data:
        cab= data.readline()
        for c in data:
            valores = c.split(",")
            data = valores[0]
            precipitacao= float(valores[1])
            dados_chuvoso[data]= precipitacao
        mes_men_chuvoso= min(dados_chuvoso,key=dados_chuvoso.get)
        men_precipitacao= dados_chuvoso[mes_men_chuvoso]

        return mes_men_chuvoso,men_precipitacao


#Função para calcular temperatura mínima
def cal_temp_min():
    with open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r") as data:
        next(data)
        print("\nDescobrindo a temperatura mínima nos últimos anos (2006-2016)\n")
        temp_mes= {}
        op = int(input("Por favor, digite o número referente ao mês desejado (1-12): \n"))
        while op < 1 or op > 12:
            op = int(input("Por favor, digite o número referente ao mês desejado (1-12): \n"))

        for c in data:
            valores = c.split(",")
            dat = valores[0][3:10]
            data_parts = dat.split("/")
            data1 = (int(data_parts[0]), int(data_parts[1]))

            if op == data1[0] and 2006 <= data1[1] <= 2016:
                chave = f"{data1[0]}/{data1[1]:02d}"
                temp = float(valores[4])
                temp_mes[chave] = temp
                dados_temp_min[chave] = temp

        soma_val = sum(dados_temp_min.values())
        media_geral = soma_val / len(dados_temp_min) if len(dados_temp_min) > 0 else 0

        print("A média das temperaturas mínimas por mês foi:")
        for chave, temp in sorted(temp_mes.items()):
            print(f"{chave} -> {temp}")
            temp_mes_grafico.append(temp)
            ano_grafico.append(chave)

        print(f"A média geral das temperaturas mínimas para o mês escolhido foi: {media_geral:.2f}")

        return

#Parte inicial e validação de entrada
print("\n")
print("Seja bem-vindo(a) ao programa de dados meteorológicos")
print("Nosso programa utiliza informações climáticas diárias do município brasileiro de Porto Alegre, entre os anos 1961 e 2016. \n")
print("Primeiramente, digite o mês e ano inicial: ")
mes_i,ano_i=validar_data()

print("\n Agora digite o mês e ano final:\n")
mes_f,ano_f=validar_data()

if mes_i==mes_f or mes_i>mes_f:
    print("O mês inicial não pode ser igual ou maior do que o mês final\n")
elif ano_i==ano_f or ano_i>ano_f:
    print("O ano inicial não pode ser igual ou maior do que o ano final\n")

dados=carga_dados()

#Visualização de intervalos em modo texto
while op!=5:
    print("\n Digite a opção de visualização desejada:\n")
    print(" 1) todos os dados, \n 2) apenas os de precipitação, \n 3) apenas os de temperatura, \n 4) apenas os de umidade e vento para o período informado.\n 5) sair\n")
    op = int (input())

    if op== 1:
        print("Data | Precipitação | Temp.Máxima | Temp.Mínima | Horas de insolação | Temp. Média | Umidade do ar | Vel. do vento")
        for c in range(len(precip)):
            print(data_l[c],"|",precip[c],"|",temp_max[c],"|",temp_min[c],"|",h_inso[c],temp_med[c],umid[c],vel[c])
        g_arq=open("dados.txt","w")
        for c in range(len(precip)):
            g_arq.write(str(data_l[c])+ "|"+str(precip[c])+"|"+str(temp_max[c])+"|"+str(temp_min[c])+"|"+str(h_inso[c])+"|"+str(temp_med[c])+"|"+str(umid[c])+"|"+str(vel[c])+"\n")
        g_arq.close()

    elif op ==2:
        print("Data | Precipitação")
        for c in range(len(precip)):
            print(data_l[c],"|", precip[c])
        g_arq=open("dados.txt","w")
        for c in range(len(precip)):
            g_arq.write(str(data_l[c])+"-"+str(precip[c])+"\n")
        g_arq.close()

    elif op ==3:
        print("Data | Temp.Máxima | Temp.Mínima | Temp. Média")
        for c in range(len(precip)):
            print(data_l[c],"|",temp_max[c],"|",temp_min[c],"|",temp_med[c])
        g_arq=open("dados.txt","w")
        for c in range(len(precip)):
            g_arq.write(str(data_l[c])+"|"+str(temp_max[c])+"|"+str(temp_min[c])+"|"+str(temp_med[c])+"\n")
        g_arq.close()

    elif op ==4:
        print("Data | Umidade do ar | Vel. do vento")
        for c in range(len(precip)):
            print(data_l[c],"|",umid[c],"|",vel[c])
        g_arq=open("dados.txt","w")
        for c in range(len(precip)):
            g_arq.write(str(data_l[c])+"|"+str(umid[c])+"|"+str(vel[c])+"\n")
        g_arq.close()
    else:
        print("Você optou por sair.")

#Mês menos chuvoso
mes,precipitacao= mes_chuvoso()
print(f"O mês com a menor precipitação foi: {mes} com o índice de {precipitacao}")

#Média da temperatura mínima
cal_temp_min()

#Gráfico
plt.title("Gráfico de precipitação")

listax=[]
ano=2015
for x in range(len(temp_mes_grafico)):
    x=ano+1

    listax.append(x)
plt.plot(ano_grafico,temp_mes_grafico, label ="")
plt.xlabel("Temperatura mínima")
plt.ylabel("Ano")
plt.legend()
plt.show()
plt.legend()
