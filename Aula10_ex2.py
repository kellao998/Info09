r1=float(input("digite um valor"))
r2=float(input("digite um valor"))
r3=float(input("digite um valor"))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("as retas acima podem formar um triangulo")
else:
    print("as retas não forma um triangulo")
print("e seu formato é: ")
if r1==r2==r3:
    print("O triangulo é equilatero")
elif r1==r2 or r1==r3 or r2==r3:
    print("o triangulo é isoceles")
else:
    print("todos os lados do seu triangulo são diferentes")
    