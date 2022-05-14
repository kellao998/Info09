from random import randint


lista=list()
jogos=list()
print('-'*40)
print('   JOGO DA MEGA SENA   ')
print('-'*40)

qnt=int(input("quantos jogos você deseja que eu sorteie? "))
tot=1

while tot<=qnt:
    cont=0    
    while True:
            num=randint(1,60)
            if num not in lista:
                lista.append(num)
                cont+=1
            if cont>=6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
    print('-='*3,f"SORTEANDO {qnt} JOGOS",'-='*3)
for i , l in enumerate(jogos):
    print(f'jogo {i}: {l}')

