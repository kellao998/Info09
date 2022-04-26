a=float(input("digite a sua altura: "))
b=float(input("digite sua altura: "))
c=float(input("digite sua altura: "))

if a<b and a<c and b>a and b<c:
    print("o maior usuario mede {:.2f} seguidos de {:.2f}, {:.2f}".format(c,b,a))
elif b<a and c<a and a>b and b>c:
    print("o maior usuario mede {:.2f} seguidos de {:.2f}, {:.2f}".format(a,b,c))
elif a<b and c<b and a>c and b>c:
    print("o maior usuario mede {:.2f} seguidos de {:.2f}, {:.2f}".format(c,a,b))
elif b<a and c<a and a>c and c>b:
    print("o maior usuario mede {:.2f} seguidos de {:.2f}, {:.2f}".format(a,c,b))
elif a<b and c<b and b>a and b>c:
    print("o maior usuario mede {:.2f} seguidos de {:.2f}, {:.2f}".format(b,a,c))
elif a<b and c<b and b>c and c>a:
    print("o maior usuario mede {:.2f} seguidos de {:.2f}, {:.2f}".format(b,c,a))
else:
    print("voce digitou algo inválido")
