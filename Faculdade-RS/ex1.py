t_pos=0
t_neg=0
t_par=0
t_impar=0
aux=0

#entrada de dados sem mensagem para não atrapalhar o beecrowd
for c in range(5):
    aux=int (input())
    if (aux>0):
        t_pos+=1
    elif (aux<0):
        t_neg+=1
    if(aux%2==0):
        t_par+=1
    else:
        t_impar+=1
print(f"{t_par} valor(es) par(es)")
print(f"{t_impar} valor(es) impar(es)")
print(f"{t_pos} valor(es) positivo(s)")
print(f"{t_neg} valor(es) negativo(s)")
