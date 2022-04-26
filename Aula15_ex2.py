maior = 0
menor = 1000

for c in range(0, 5):
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(maior, menor))
