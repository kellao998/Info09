nome = input("Nadador 1: ")
tempo = float(input("Tempo do nadador 1: "))


melhor_nadador = nome
melhor_tempo = tempo
pior_nadador = nome
pior_tempo = tempo


soma_tempo = 0
soma_tempo += tempo
tempo_12_15s = 0

if 12 <= tempo <= 15:
    tempo_12_15s += 1

for nadador in range(2, 8):

    nome = input("Nadador " + str(nadador) + ": ")
    tempo = float(input("Tempo do nadador " + str(nadador) + ": "))

    if tempo < melhor_tempo: 
        melhor_nadador = nome  
        melhor_tempo = tempo  
    elif tempo > pior_tempo:  
        pior_nadador = nome  
        pior_tempo = tempo  


    soma_tempo += tempo


    if 12 <= tempo <= 15:
        tempo_12_15s += 1

print(f"{melhor_nadador} é o melhor nadador com {melhor_tempo} seg.")
print(f"{pior_nadador} é o pior nadador com {pior_tempo} seg.")
media = soma_tempo / 7
print(f"Média dos tempos = {media:.2f} seg.")
print(f"Atletas entre 12 seg e 15 seg: {tempo_12_15s}")