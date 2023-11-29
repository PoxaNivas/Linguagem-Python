#Sobre formatação
import random

for c in range(3):
    N1= int (random.randint(0,9))
    print(f"Número com 0 casas {N1}")
    print(f"Número com 3 casas{N1:3}")
    print(f"Número com 4 casas {N1:4}")
    print(f"Número com 0 casas em decimais {N1}")
    print(f"Número com 3 casas em decimais {N1:.3f}")
    print(f"Número com 4 casas em decimais {N1:.4f}")
