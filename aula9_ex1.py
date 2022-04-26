imprestimo=int(input("qual a sua renda mensal? "))
tempo=int(input(" digite em quantos anos vc pretende pagar? "))
casa=int(input("qual o valor da cada pretendida? "))
meses=tempo*12
parcelas=casa/meses
pagamento=(imprestimo/100)*30

if parcelas<pagamento:
    print("o valor mensal a ser pago será de : {} reais".format(parcelas))
else:
    print("impéstimo negado")



