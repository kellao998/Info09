
import math

a1=int(input("digite um numero: "))
escolha=int(input("Digite:\n 1 para binario\n 2 para octal\n 3 para hexadecimal\n "))
if escolha==1:
    print("o numero {} em binario fica {}".format(a1, bin(a1)))
elif escolha==2:
    print("o numero {} em octal fica {}".format(a1, oct(a1)))
elif escolha==3:
    print("o numero {} em hexadecimal fica {}".format(a1, hex(a1)))
else:
    print("oção inválida")
    
