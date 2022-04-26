r1=float(input("digite um valor"))
r2=float(input("digite um valor"))
r3=float(input("digite um valor"))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("as retas acima podem formar um triangulo")
else:
    print("as retas não forma um triangulo")
