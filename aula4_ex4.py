
nome=input("qual o seu nome")
sal_base=float(1500)
comissao=float(200)
qntd_vendas=float(input("quantas vendas"))
tot_vendas=float(input("quantas vendas foram realizada"))

sal_final=sal_base + (comissao*qntd_vendas) + tot_vendas*0.05

print("o vendedor {} recebeu o valor de {}".format(nome, sal_final))
