soma=0

valor1=int(input("digite um numero: "))
valor2=int(input("digite o ultimo numero: "))

valor_intervalo=len(range(valor1,valor2))
for i in range(valor1,valor2):
   soma+=i
media=soma/valor_intervalo

print("media geral {}".format(media)) 