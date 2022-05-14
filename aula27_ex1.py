

from datetime import date



def voto(ano):
    
    atual = date.today().year
    idade = atual - ano
    if idade<16:
        return f'com {idade} anos: não vota'
    elif 16<= idade <18 or idade >65:
        return f'com {idade} anos: voto opcional'
    else:
        return f'com {idade} anos: voto obrigatório'


nasc=int(input("em que anos você nasceu? "))
print(voto(nasc))

