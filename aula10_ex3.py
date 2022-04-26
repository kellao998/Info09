p=float(input("digite seu peso: "))
a=float(input("digite sua altura: "))
imc=p/(a*a)
if imc<=18.5:
    print("seu IMC é {} abaixo do peso".format(imc))
elif imc>18.5 and imc<25:
    print("seu IMC é {}, peso ideial".format(imc))
elif imc>25 and imc<30:
    print("seu IMC é {} você esta com sobrepeso".format(imc))
elif imc>30 and imc<40:
    print("seu IMC é {} você tem obesidade".format(imc))
else:
    print("seu IMC é {} e você tem obsidade morbida")
    