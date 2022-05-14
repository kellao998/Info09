from time import sleep

def maior(* num):
    cont =maior=0
    print('\nAnalisando os valores')
    sleep(1)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont==0:
            maior = valor
        else:
            if valor > maior:
                maior=valor
        cont += 1
    print(f' os valores informados {cont} valores')
    sleep(0.4)
    print(f'maior valor informado {maior}')


maior(1,2,3,4,5,6,7)
maior(12,2,4,6,7,8,32)

