from time import sleep


n=str(input("Qual o seu primeiro nome: "))

print("Analisando as informações...\nAguarde...")
sleep(2)

nome=n.split()

print("seu nome completo é {}\n primeiro nome: {}\n ultimo nome: {}".format(n, nome[0], nome[len(nome) - 1]))
