
#variável total para somar todos os minutos, variável de entrada, horas, minutos e fim do jogo (que serão reutilizadas para mostrar os novos valores)
#entradas
print("Seja bem-vindo(a) ao cronometro de partida.\n")
I_hora = int (input("Por favor, digite a hora início do jogo: "))
I_minuto= int (input("Por favor, agora digite os minutos: "))
F_hora= int (input("Por favor, digite a hora final do jogo: "))
F_minuto= int (input("Por favor, agora digite os minutos finais: "))

#cálculos
if F_hora>I_hora or F_hora==I_hora and F_minuto==I_minuto:print("Horário início e término idênticos.")
R_hora= int
R_minuto=int
T_inicio=int
T_final= int
T_inicio= (I_hora*60)+I_minuto
T_final= (F_hora*60)+F_minuto
R_hora=(T_final-T_inicio)//60
R_minuto= (T_final-T_inicio)%60

if R_hora>=25:print("Partida excedeu o tempo previsto")
else: print("A partida durou ",R_hora, " horas e ",R_minuto, " minutos")




#converter 24 horas para minutos e subtrair o fim pelo início e depois converter para horas e minutos
