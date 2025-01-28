from math import trunc

print("""Crie um programa que simule o funcionamente de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro), e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE $50, $20, R$10 E R$1""")
valor = float(input("Qual valor vocêr quer sacar? "))
restos = valor
notas1 = notas10 = notas20 = notas50 = notas100 = 0

while restos > 0:
    # if restos >= 100:
    #     notas100 = trunc(restos / 100)
    #     print(f"Notas de R$100 necessárias: {notas100}")
    # restos = restos % 100
    if restos >= 50:
        notas50 = trunc(restos / 50)
        print(f"Total de notas de R$50 necessárias: {notas50}")
    restos = restos % 50
    if restos >= 20:
        notas20 = trunc(restos / 20)
        print(f"Total de Notas de R$20 necessárias: {notas20}")
    restos = restos % 20
    if restos >= 10:
        notas10 = trunc(restos / 10)
        print(f"Total de Notas de R$10 necessárias: {notas10}")
    restos = restos % 10
    if restos >= 1:
        notas1 = trunc(restos / 1)
        print(f"Total de Notas de R$1 necessárias: {notas1}")
    restos = restos % 1


