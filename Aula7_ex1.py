from datetime import date


ano=int(input("digite um ano: "))
if ano %4==0 and ano %100!=0 or ano%400==0:
    print("o ano {} é bissexto.".format(ano))
else:
        print ("o {} ano nâo é BISSEXTO".format(ano))
    