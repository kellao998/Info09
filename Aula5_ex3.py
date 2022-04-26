import math
angulo=float(input("informe o angulo"))
seno=math.sin(math.radian(angulo))
print("o angulo tem {}, o seno tem {:.2f}".format(angulo, seno))
cosseno=math.cos(math.radians(angulo))
print("o angulo de {} tem o cosseno de {:.2f}".format(angulo,cosseno))
tangen=math.tan(math.radians(angulo))
print("o angulo de {} tem a tangente de {:.2f}".format(angulo, tangen))
