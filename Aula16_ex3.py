loguin=input("qual o seu nome: ")
erros = 0
while erros < 3:
    
    senha = int(input("Senha: "))
    if senha == 123456:
        print("Olá, {}, Seja bem-vindo ao nosso banco!".format(loguin))
        break
    else:
     
        erros += 1

        if erros < 3:

            print(f"Senha incorreta! Você ainda tem {3 - erros} tentativa(s).")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
            break