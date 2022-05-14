from MinhasFuncoes import *

linhas = int(input('quantidade de linhas: '))
colunas = int(input('quantidade de colunas: '))
intervalo_inicial = int(input('intervalo inicial: '))
intervalo_final = int(input('intervalo final: '))

A = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
B = gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
if len(A) == len(B) and len(A[0]) == len(B[0]):
    print(f'Matriz A = {A} \nMatriz B = {B} \nMatriz C (A+B) = {soma_matrizes(A,B)}')
else:
    print('ERRO: as matrizes não são de mesma ordem.')