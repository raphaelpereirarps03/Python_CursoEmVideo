print("Faça um programa que calcule a soma de todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 e 500")
somaImpares = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        somaImpares += c
print("A soma de todos os números impares, múltiplos de 3, de 1 a 500 é {}".format(somaImpares))