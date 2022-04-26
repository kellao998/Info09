
mulheres = 0
homens_acima18 = 0
print("QUANDO ACABREM OS ALUNOS DIGITE '-1'")
while True:
    idade = int(input("Idade(apenas numeros): "))
    if idade < 0:
        break
    sexo = input("Sexo(F/M): ")
    if sexo == "F" or sexo == "f":
        mulheres += 1
    elif sexo == "M" or sexo == "m":
        if idade > 18:
            homens_acima18 += 1
print(f"Total de mulheres: {mulheres}")
print(F"Total de homens acima de 18 anos: {homens_acima18}")