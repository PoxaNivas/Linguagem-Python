p1=float(input("P1: "))
p2=float(input("P2: "))
p3=float(input("P3: "))
freq=float(input("Freq: "))
g1= (p1+p2+p3)/3

if freq<75:
    print(f"reprovado por falta. {freq}")
else:
    if g1<4:
        print(f"Reprovado por média. {g1}")
    else:
        if g1>7:
            print(f"Aprovado por média.{g1} ")
        else:
            g2= float(input("G2: "))
            final=(g1+g2)/2
            if final>=5:
                print(f"aprovado em G2: {final}")
            else:
                print(f"Reprovado em G2: {final}")
   