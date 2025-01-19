print("Escreva um programa que leia 3 número e mostre qual é o maior valor e o menor")
valor1 = int(input("Entre com o primeiro valor: "))
maior = valor1
menor = valor1
valor2 = int(input("Entre com o segundo valor: "))
if valor2 < menor:
    menor = valor2
if valor2 > maior:
    maior = valor2
valor3 = int(input("Entre com o primeiro valor: "))
if valor3 < menor:
    menor = valor3
if valor3 > maior:
    maior = valor3
print("O maior valor é {}. E o menor valor é {}".format(maior, menor))
