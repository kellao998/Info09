

def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor =int(n)
            ok = True
        else:
            print("erro, Digite um número válido ")
        if ok:
            break
    return valor
n=leiaint("digite um numero: ")
print(f"voce digitou o numero {n}")
