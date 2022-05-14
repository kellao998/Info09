
N = int(input("Digite um número ímpar, maior que 1: "))
if N <= 1 or N % 2 == 0:
    print("Número informado não atende os critérios definidos.")
else:
    L = []
    for x in range(N):
        num = int(input("Digite um número maior ou igual a zero: "))
        L.append(num)

    
    centro = int(len(L) / 2)
    elemento_central = L[centro] 
    fatorial = 1  
    for n in range(2, elemento_central + 1):
        fatorial *= n 
    print(f"Lista: {L}")
    print(f"Portanto, {elemento_central}! = {fatorial}")