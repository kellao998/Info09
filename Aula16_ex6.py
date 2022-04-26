print(22 * "-")
print("Código   Cargo")
print(22 * "-")
print("1        Enfermeiro(a)")
print("2        Nutricionista")
print("3        Médico(a)")
salariomed=0
nutri = 0
while True:   
   cargo = int(input("Informe um código: "))
   if cargo >= 1 and cargo <= 3:
      salario = float(input("Salário R$: "))
      if cargo == 2:
         salariomed += salario
         nutri+=1

      resp = input("Deseja continuar [S|N]? ")
      if resp.upper() == "N":
         break      
   else:
      print("Código inválido.")
medio=salariomed/nutri
print("Salario médio dos nutricionistas é {:.2f}".format(medio))