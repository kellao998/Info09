import random
from random import randrange

N = int(input("Digite um valor N (tal que N > 1): "))
if N > 1:
    
    L = [randrange(1, 11) for i in range(N)]
    print(f"Lista: {L}")
    produto_elementos = 1
    for num in L:
        produto_elementos *= num
    media_geo = produto_elementos ** (1 / N)
    print(f"Média geométrica da lista: {media_geo:.2f}")
else:
    print("Valor informado deve ser maior que 1.")