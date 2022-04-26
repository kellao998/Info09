veloc=int(input("o veiculo passou a "))
if veloc>80:
    print("Você foi multado ")
    multa=(veloc-80)*7
    print("o valor da multa é {:.2f} reais".format(multa))
    
