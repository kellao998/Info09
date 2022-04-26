from datetime import date
ano_atual=date.today().year
ano=0
maiores=0
menor=0
for c in range (0,7):
    ano=int(input("digite o ano do seu nascimento: "))
    idade=ano_atual - ano
    if idade>18:
        maiores=maiores+1
    else:
        menor=menor+1

print("maiore de idade {}". format(maiores))
print("menores de idade {}".format(menor))



