
esc=int(input("****************************************\n CALCULO DE GRANDEZAS ELÉTRICAS\n ****************************************\n 1 Tensao (em volt)\n 2 resistencia (em ohm)\n 3 corrente(em ampéres)\n****************************************\n"))



if esc==1:
    corrente=float(input("digite a corrente "))
    resistencia=float(input("digite a resistencia "))
    print("A tensão é {} volts".format((corrente*resistencia)))

elif esc==2:
    tensao=float(input("informe a tensão: "))
    corrente=float(input("informe a corrente: "))
    print("a resistencia é {} Ohm".format(tensao/corrente))
elif esc==3:
    tensao=float(input("informe a tensão: "))
    resistencia=float(input("digite a resistencia "))
    print("a corrente é {} amperes".format(tensao/resistencia))
else:
    print("opão invalida")
