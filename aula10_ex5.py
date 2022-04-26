n=float(input("quantas camisetas você adquiriu?"))

if n<=5:
    p=float(input("qual o valor da compra? "))
    print("o valor final de sua compra com o desconto ficará {} reais".format(p-(p/100*3)))
elif n>=5 and n<=10:
     p=float(input("qual o valor da compra? "))
     print("o valor final de sua compra com o desconto ficará {} reais".format(p-(p/100*5)))
elif n>10:
     p=float(input("qual o valor da compra? "))
     print("o valor final de sua compra com o desconto ficará {} reais".format(p-(p/100*7)))
