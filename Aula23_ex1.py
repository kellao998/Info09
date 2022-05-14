

from random import randrange

linha=int(input("numero de linhas: "))
coluna=int(input("numero de colunas: "))



a=[[randrange(1,11)for i in range(coluna)] for j in range(linha)]
b=[[randrange(1,11) for i in range(coluna)]for j in range(linha)]

abaixodp=0
acimadp=0

for i in range(linha):
    for j in range(coluna):
        if i>j:
            abaixodp+=a[i][j]
        if i<j:
            acimadp+=b[i][j]

print("matriz A:")
for i in range(linha):
    for j in range(coluna):
        print(a[i][j], end=' ')
    print()

print("matriz B")
for i in range(linha):
    for j in range(coluna):
        print(b[i][j], end=' ')
    print()

print(f"soma = {abaixodp+acimadp}")
        



