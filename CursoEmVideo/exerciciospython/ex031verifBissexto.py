from datetime import date
print("Crie um programa que leia um ano e diga se ele é bissexto ou não. Se a pessoa entrar com 0, pegará o ano atual")
ano = int(input("Digite um ano (Se quiser o ano atual, digite 0): "))
if ano == 0 :
    ano = date.today().year
    print(ano)
if (ano % 4 != 0) or ((ano % 100 == 0) and (ano % 400 != 0)):
    print("Não é bissexto!")
else:
    print("É bissexto!")
