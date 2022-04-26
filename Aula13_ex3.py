soma = 0
contado = 0
for c in range(0,501):
    if c % 2==1:
        if c % 3==0:
            soma += c
            contado +=1

            print(c)


print("a soma de todos os {} valores é {}".format(contado, soma))
