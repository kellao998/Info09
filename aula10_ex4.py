p=float(input("qual o valor do produto? "))
f=int(input("qual a forma de pagamento? \n 1 - à vista dinheiro/cheque: 10% de desconto.\n 2 - a vista no cartão 5% de desconto\n 3 - em até duas vezes no cartão no preço da etiqueta\n 4 - à vista no cartão 5% de desconto\n "))


if f==1:
    print("sua compra custará {:.2f} reais".format(p-(p/100*10)))
elif f==2:
    print("sua compra custará {:.2f} reais".format(p-(p/100*5)))
elif f==3:
    print("sua compra custará {:.2f} reais em duas vezes de {:.2f} reais".format(p, p/2))
elif f==4:
    print("sua compra custará {:.2f} reais".format(p-(p/100*5)))
else:
    print("opcão inválida")

