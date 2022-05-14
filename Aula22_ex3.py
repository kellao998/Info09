import random


RIFA = []
while True:
    nome = input("Informe um nome: ")
    RIFA.append(nome)
    resp = input("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break

r=random.shuffle(RIFA) 
sorteado = random.choice(r) 
print(f"Os participantes da rifa são: {RIFA}.")
print(f"{sorteado} foi o(a) sorteado(a)!")