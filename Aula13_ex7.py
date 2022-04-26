r=str(input("Digite seu sexo [M/F] ")).strip().upper()

while r!='M' and r!='F':

    print("Você não digitou M ou F")
    r=str(input("Digte seu sexo [M/f]: ")).strip().upper()