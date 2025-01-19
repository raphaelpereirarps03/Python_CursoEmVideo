print("Escreva um programa que leia um número inteiro positivo e diga se ele é par ou impar")
numero = int(input("Entre com um número qualquer: "))

if numero % 2 == 0:
    print("O número {} é par!".format(numero))
else:
    print("O número {} é ímpar!".format(numero))
