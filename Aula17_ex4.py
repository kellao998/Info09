prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

dec = (prim + (10 - 1) * raz)  

counter = prim
while counter <= dec:
    print("{}".format(counter))
    counter += raz