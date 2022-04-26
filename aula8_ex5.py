import random

from sklearn.utils import shuffle
a1=input("aluno 1 ")
a2=input("aluno 2 ")
a3=input("aluno 3 ")
a4=input("aluno 4 ")
lista=[a1,a2,a3,a4]
sorteio=shuffle(lista)
print("a ordem de apresentação será: ")
print(sorteio)

