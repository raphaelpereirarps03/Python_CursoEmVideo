from datetime import datetime

print("Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas peessoas atingiram a maioridade e quantas ainda não.")

anoAtual = datetime.today().year
contadorMaior = 0
contadorMenor = 0
for c in range(0, 7):
    anoNasc = int(input("Entre com o ano de nascimento do {}º aluno: ".format(c + 1)))
    if anoAtual - anoNasc >= 21:
        contadorMaior += 1
    else:
        contadorMenor +=1

print("Total de pessoas maiores de idade: {}".format(contadorMaior))
print("Total de pessoas menores de idade: {}".format(contadorMenor))
