idade = int(input("Idade: "))


mais_novo  = idade 
mais_velho = idade

while True:   
   idade = int(input("Idade: "))
   if idade < 0: 
      break

   if idade < mais_novo:   
      mais_novo = idade
   elif idade > mais_velho:
      mais_velho = idade

print("Menor idade: {}".format(mais_novo))
print("Maior idade: {}".format(mais_velho))
media = (mais_novo + mais_velho) / 2
print("Média das duas idades = {:.2f}".format(media))
