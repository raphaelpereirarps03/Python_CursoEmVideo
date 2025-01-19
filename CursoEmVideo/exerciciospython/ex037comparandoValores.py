print("Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem")
valor1 = int(input("Entre com o 1º valor: "))
valor2 = int(input("Entre com o 2º valor: "))
if valor1>valor2:
    print("O 1º valor, {}, é o maior.".format(valor1))
elif valor2>valor1:
    print("O 2º valor, {}, é o maior.".format(valor2))
else:
    print("Não existe maior, eles são iguais.")