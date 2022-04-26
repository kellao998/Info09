import math

salario=float(input("qual o seu salario? "))

if salario>1250.00:
    reajuste=salario+(salario/100*15)
    print("seu salario ficara {:.2f} reais".format(reajuste))
else:
    final=salario + (salario /100*10)
    print("seu salario ficara {:.2f} reais".format(final))