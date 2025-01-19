import datetime
print("Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade")
anoNasc = int(input("Entre com o ano de seu nascimento: "))


print(datetime.date.today().year)
print(datetime.date.today().year - anoNasc)
if datetime.date.today().year - anoNasc < 18:
    print("Você ainda vai se alistar daqui à {} ano(s)".format((datetime.date.today().year - anoNasc)))
elif datetime.date.today().year - anoNasc == 18:
    print("Você está na hora de se alistar!")
else:
    print("Você precisa se alistar urgentemente! Está atrasado {} ano(s).".format((datetime.date.today().year - anoNasc) - 18))
