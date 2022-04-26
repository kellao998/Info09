from datetime import date
ano=int(input("Em que ano você nasceu? "))
idade=date.today().year-ano

if idade<18:
    print("voce ainda tem idade para se alistar, em {} anos podera se alistas".format(18-idade))
elif idade==18:
    print("voce deve se alistar")
else:
    print("voce ja passou do tempo de alistamento")
    
