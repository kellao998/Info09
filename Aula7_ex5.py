
num1=float(input("digite um numero positivo"))
num2=float(input("digite mais um numero positivo"))
non=int(input("# voce deseja que o programa execute a função # \n 1 - média ponderada com pesos 2 e 3 \n 2 - o quadrado da soma dos 2 numeros\n 3 - o cubo do menor número\n ESCOLHA UMA OPÇÃO:"))

media=(num1*2+num2*3)/(2+3)
quadrado=(num1+num2)**2


if non==1:
    print("a média ponderada é {:.2f}".format(media))
else:
    if non==2:
        print("o quadrado é {:.2f}".format(quadrado))
    else:
        if non==3:
            if num1<num2:
                print("o cubo do menor numero é {:.2f}".format(num1**3)) 
            else:      
             print("o cubo do menor numero é {:.2f}".format(num2**3))
if non==0 or non>4:
    print("opção invalida.")

