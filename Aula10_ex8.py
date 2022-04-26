from time import sleep
f=str(input("digite uma frase: ")).strip()
sleep(1)
print("Analisando a frase...")
sleep(2)
print("sua frase contem {} letras 'A' ".format(f.count('a')))
print("a letra 'A' aparece primeiro apos {} letras".format(f.find('a')))
print("e aparece por ultima apos a letra {}".format(f.rfind('a')))

