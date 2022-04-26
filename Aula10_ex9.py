from time import sleep

l=str(input("INFORME O LOGIN: "))
s=str(input("INFORME A SENHA: "))
sleep(1)
print("Analisando dados...\n...aguarde...")
l1='fabio'
s1='joao1'
l2='fabian'
s2='fabian123'
sleep(2)
if l== l1 and s==s1 or l==l and s==s2:
    print("login aceito\n SEJA BEM VINDO")

else:
    print("login e/ou senha invalida\n tente novamente")
