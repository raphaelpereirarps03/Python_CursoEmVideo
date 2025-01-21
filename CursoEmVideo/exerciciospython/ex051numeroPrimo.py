print("Escreva um programa que leia um número inteiro e diga se ele é primo ou não")

numero = int(input("Entre com um número: "))

contadorDivisoes = 0
for c in range (numero, 0, -1):
    if numero % c == 0:
        contadorDivisoes += 1

if contadorDivisoes==2:
    print("{} é um número primo!".format(numero))
else:
    print("{} não é um número primo!".format(numero))