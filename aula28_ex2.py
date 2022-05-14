from MinhasFuncoes import *

linhas = int(input('quantidade de linhas: '))
colunas = int(input('quantidade de colunas: '))
intervalo_inicial = int(input('intervalo inicial: '))
intervalo_final = int(input('intervalo final: '))

M = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
print(f'Matriz gerada: {M}')

if len(M) == len(M[0]):
    print(f'Traço da matriz gerada: {calcula_traco_matriz(M)}')

else:
    print('Não foi possível calcular o traço pois M não é quadrada.')