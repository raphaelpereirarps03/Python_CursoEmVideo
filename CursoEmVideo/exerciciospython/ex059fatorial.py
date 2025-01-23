print("Faça um programa que leia um número inteiro qualquer e mostre seu fatorial")

numero = int(input("Entre com um número: "))
sub = numero
resultFatorial = 1
print("Calculando {}! = ".format(numero), end='')
while sub > 0:
    print("{}".format(sub), end=' x ' if sub > 1 else " = {}".format(resultFatorial))
    resultFatorial *= sub
    sub -= 1
