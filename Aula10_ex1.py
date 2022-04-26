from datetime import date

idade=int(input("Que ano você nasceu? "))

ano=date.today().year-idade

if ano<=9:
    print("você tem {} anos e podera participar da categoria MIRIM".format(ano))
elif ano<=14:
    print("você tem {} anos e sua categoria é INFANTIL".format(ano))
elif ano<=19:
    print("você tem {} anos e sua categoria é JUNIOR".format(ano))
elif ano<=25:
    print("você tem {} anos e podera participar da categoria SENIOR".format(ano))
else:
    print("voce tem {} ano e podera participar da categoria MASTER".format(ano))
