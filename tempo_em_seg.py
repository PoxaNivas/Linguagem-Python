
tempo= int (input ("Por favor, informe a quantidade de horas em segundos "))
horas= int (tempo//3600)
minutos= int ((tempo%3600)//60)
segundos= int (tempo-(horas*3600)-minutos*60)
print("O evento informado tem: ",horas, " horas", minutos, " minutos ", segundos, " segundos ")