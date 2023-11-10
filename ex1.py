t_pos=0
t_neg=0
t_par=0
t_impar=0
aux=0
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
'''
t_pos=0
t_neg=0
t_par=0
t_impar=0
a = int (input())
if (a>0):
    t_pos+=1
elif (a<0):
    t_neg+=1
if(a%2==0):
    t_par+=1
else:
    t_impar+=1
b = int (input())
if (b>0):
    t_pos+=1
elif(b<0):
    t_neg+=1
if (b%2==0):
    t_par+=1
else:
    t_impar+=1
c = int (input())
if (c>0):
    t_pos+=1
elif(c<0):
    t_neg+=1
if (c%2==0):
    t_par+=1
else:
    t_impar+=1
d = int (input())
if (d>0):
    t_pos+=1
elif(d<0):
    t_neg+=1
if (d%2==0):
    t_par+=1
else:
    t_impar+=1
e = int (input())
if (e>0):
    t_pos+=1
elif (e<0):
    t_neg+=1
if (e%2==0):
    t_par+=1
else:
    t_impar+=1
print(f"{t_par} valor(es) par(es)")
print(f"{t_impar} valor(es) impar(es)")
print(f"{t_pos} valor(es) positivo(s)")
print(f"{t_neg} valor(es) negativo(s)")

'''
