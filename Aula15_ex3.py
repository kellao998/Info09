maiorIdade = 0
menorIdade = 0
mediaIdade = 0
maisVelho = str

for c in range(0,4):
    nome = str(input('Informe o seu nome: '))
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe o seu genero entre: Masculino e Feminino: ')).lower()
    if idade > maiorIdade and sexo == 'masculino':
        maiorIdade = idade
        maisVelho = nome
    elif idade <= 20 and sexo == 'feminino':
        menorIdade += 1
    mediaIdade += idade

print('A idade média do grupo é de: {}'
      '\nO nome do homem mais velho é: {}'
      '\nA quantidade de mulheres com menos de 20 anos é: {}'.format(mediaIdade/2, maisVelho, menorIdade))