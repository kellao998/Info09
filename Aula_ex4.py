viagem=float(input("quantos Km de distancia é a viagem? "))
if viagem<=200:
    print("sua viagem custará {:.2f} reais".format(viagem*0.50))
else:
    print("sua viagem custará {:.2f} reais".format(viagem*0.45))
    