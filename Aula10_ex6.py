from random import randint
from time import sleep
from tkinter.tix import InputOnly

itens =('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''escolha uma opção
[0] pedra
[1] papel
[2] tesoura''')

jogador=int(input("qual a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(2)
print('-='*11)

print("o computador escolher {}".format(itens[computador]))
print("voce escolheu: {}".format(itens[jogador]))
print('-='*11)
if computador==0:
    if jogador==0:
        print("EMPATE")
    elif jogador==1:
        print("JOGADOR VENCEU")
    elif jogador==2:
        print("O COMPUTADOR GANHOU")
elif computador==1:
    if jogador==0:
        print("COMPUTADOR VENCEU")
    elif jogador==1:
        print("EMPATE")
    elif jogador==2:
        print("VOCÊ GANHOU")
elif computador==2:
    if jogador==0:
        print("VOCÊ VENCEU")
    elif jogador==1:
        print("COMPUTADOR VENCEU")
    elif jogador==2:
        print("EMPATE")
