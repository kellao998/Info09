numero=float(input("digite um numero"))
square=numero**2

if numero %2 == 0:
    print("o numero que voce digitou ao quadrado é {} ".format(square))
else:
    triple=numero**3
    print("o numero que voce digitou ao cubo é {}".format(triple))