print("Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão")

primeiroTermo = int(input("Entre com o primeiro termo da progressão aritmética: "))
razao = int(input("Entre com a razão da PA: "))


print("Os 10 primeiros termos, de uma progressão aritmética que tem como primeiro termo {} e a razão de {}, são: ".format(primeiroTermo, razao))
for c in range(0, 10):
    print(primeiroTermo)
    primeiroTermo += razao
