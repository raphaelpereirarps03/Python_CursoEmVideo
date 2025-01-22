print("Faça um programa que leia um número inteiro qualquer e mostre seu fatorial")

numero = int(input("Entre com um número: "))
sub = 1
resultFatorial = numero * sub
while sub < numero:
    resultFatorial *= sub
    sub += 1

print("{}! = {}".format(numero, resultFatorial))
