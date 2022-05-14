cont = 1
pos = 1
times = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá', 'Internacional',
          'Avaí', 'Red Bull Bragantino', 'Palmeiras', 'Flamengo', 'Coritiba',
          'São Paulo', 'Botafogo', 'Fluminense', 'América-MG', 'Ceará',
          'Athletico', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')

print(f'Lista de times do Brasileirão: {times}')
print('--'*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('--'*15)
print(f'Os 4 últimos são: {times [-4:]}')
print('--'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('--'*15)
if times=='Chapecoence':

    print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
else:
    print(f'Chapecoence não se encontra na lista')