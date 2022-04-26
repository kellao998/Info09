c=int(input("Qual o seu cargo?\n 1 - Programador de Sistemas;\n 2 - Analista de Sistemas;\n 3 - Analista de Dados;\n ESCOLHA UMA OPÇÃO: "))
if c==1:
    s=float(input("Qual o seu salário? "))
    print("seu salario é {} reais, e com base no aumento informado será {} reais".format(s, s + (s/100*30)))
elif c==2:
    s=float(input("Qual o seu salário? "))
    print("seu salario é {} reais, e com base no aumento informado será {} reais".format(s, s+(s/100*20)))
elif c==3:
    s=float(input("Qual o seu salário? "))
    print("seu salario é {} reais, e com base no aumento informado será {} reais".format(s, s+(s/100*10)))
else:
    print("Cargo inválido")
    