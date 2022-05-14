produtos = ('TV Sansung 48', 1099.00, 'PS5', 3500.00, 'Bicicleta aro 28, em inox', 4000.00, 
            'negresco', 4.50, 'Leiteem pó', 5.99, 'barra de twix', 5.99,
            'notebook, 17', 4.480, 'camiseta do Gremio', 119.99, 'camiseta do Internacional', 99.99,
            'pao sovado KG', 3.99, 'pirulito 7 belo', 1.50, 'Farinha', 4.30)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for idx, prodPreco in enumerate(produtos):
    if idx % 2 == 0:
      
        print(f'{prodPreco:.<30}', end='')
    else:
       
        print(f'R${prodPreco:>8.2f}')
        
print('-' * 40)
