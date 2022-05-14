'''def exibirmensagem():
    print('Python é facil')


exibirmensagem()

def exibirvarias(pessoas='fulano', mensagem='Bem-Vindo'):
    print(f'{mensagem}, {pessoas}')

exibirvarias()'''

'''def somarelementos(inteiros):
    soma=0
    for valor in inteiros:
        soma+=valor
    return soma
  
somarelementos([3,4,5,6,7,8,9,10,11,15])'''




'''def fatorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*fatorial(n-1)

lista=[0,1,2,3,4,5,6]

for valor in lista:
    print(fatorial(valor))'''


'''import math


def calcularmedia(lista):
    soma=0
    for valor in lista:
        soma+=valor
    return float(soma/len(lista))

def calculode(lista):
    n=len(lista)
    m=calcularmedia(lista)
    soma=0
    from math import pow
    for valor in lista:
        soma+=pow(valor-m,2)
    return math.sqrt(1/(n-1)*soma)

lista=[3,6,2,9,10,45,36,78,42,100]

print(calculode(lista))'''



'''def teste(n):
    b+=4
    c=2
    print(f"A dentro da função vale {a}")
    print(f"B dentro da função vale {b}")
    print(f"C dentro da função vale {c}")


    a=5
    teste(a)
    print(f"A fora da função vale {a}")
    #print(f"B dentro da função vale {b}")
    #rint(f"C dentro da função vale {c}")'''



    


