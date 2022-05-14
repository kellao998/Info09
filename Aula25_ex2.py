
palavras = ('tela', 'memoria', 'ram', 'computador', 'laser',
            'carro', 'europa', 'canada', 'jacuzi', 'iate', 'bicicleta',
            'salão', 'rua', 'santa', 'cruz', 'vida')


vogais = ('a', 'e', 'i', 'o', 'u')

print()

for palavra in palavras:  
    print(f'A palavra \33[33m{palavra.upper()}\33[m tem as vogais: ', end='')
    for letra in palavra: 
        for vogal in vogais:  
            if vogal == letra:  
                print(f'\33[34m{vogal}\33[m', end=' ')
    print()