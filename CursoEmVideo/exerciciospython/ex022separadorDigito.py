print("Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos digitos separados")
numero = int(input("Entre com um número de 0 à 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Unidades: {}".format(u))
print("Dezenas: {}".format(d))
print("Centenas: {}".format(c))
print("Milhares: {}".format(m))
