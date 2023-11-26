import matplotlib.pyplot as plt

#Listas
precip= [];temp_max = [];temp_min = [];h_inso=[];temp_med=[];umid = [];vel = []

#variáveis
mes_i=0; ano_i=0
mes_f=0; ano_f=0


with open("dados3.txt", "r") as data:
    cab= data.readline()
    print(cab)
    for c in data:
        valores = c.split(",")
        data= valores[0][3:10]
        data1=data.split("/")
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
'''
for c in range(len(precip)):
        print(f"Contagem {c}")
        print(precip[c],"|",temp_max[c],"|")

'''

print(data1)