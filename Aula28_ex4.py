from MinhasFuncoes import *

linhas = int(input('quantidade de linhas: '))
colunas = int(input('quantidade de colunas: '))
intervalo_inicial = int(input('intervalo inicial: '))
intervalo_final = int(input('intervalo final: '))

matriz = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
constante = int(input('Informe a constante que multiplicará a matriz gerada: '))
print(f'Matriz gerada: {matriz} \nMatriz C (k * A): {multiplica_matriz_por_constante(matriz, constante)}')