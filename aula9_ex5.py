nota1=float(input("digite sua nota 1: "))
nota2=float(input("digite sua segunda nota: "))

if (nota1+nota2)/2>=7.0:
    print("Sua nota é {} você foi aprovado!".format((nota1+nota2)/2))
elif (nota1+nota2)/2<=6.9 and (nota1+nota2)/2>=5.0:
    print("sua média fi {} você está em recuperação".format((nota1+nota2)/2))
else:
    print("sua média foi {} voce foi reprovado".format((nota1+nota2)/2))
    