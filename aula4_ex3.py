from math import sqrt

a=float(input("qual o valor de A"))
b=float(input("qual o valor de B"))
c=float(input("qual o valor de C"))
d=b**2 - 4*a*c
x1=(-b+d**(1/2)) / (2*a)
x2=(-b-d**(1)) / (2*a)
print("o valor de x1 é {}".format(x1))
print("valor de x2 é {}".format(x2))
print("valor de Delta é {}".format(d))