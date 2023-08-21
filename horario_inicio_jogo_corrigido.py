horaInicial = int(input("Informe a hora incial do jogo: "))
minutoInicial= int(input("Informe o minuto inicial do jogo: "))
horaFinal = int (input ("Informe a hora final do jogo: "))
minutoFinal= int (input("Informe o minuto final do jogo: "))

horaInicial= horaInicial* 60+ minutoInicial
horaFinal = horaFinal* 60 + minutoFinal

duracao = int
if horaInicial < horaFinal: duracao = horaFinal-horaInicial
else: duracao = 24*60 - horaInicial + horaFinal

print("Horas: ", duracao//60)
print("Minutos: ", duracao%60)