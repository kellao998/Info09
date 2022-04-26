from random import randint, shuffle
from time import sleep

print("pense em um numero de 1 a 10")
numero=int(input("qual numero você pensou "))
computador=randint(0, 10)
print("processando...")
sleep(2)
print("o numero sorteado foi {} ".format(computador))
if numero==computador: 
    print("Parabéns você acertou!")
else:
     print("Não foi desta vez, tente novamente")

