from random import randint
print("Crie um programa que vai gerar cinco números aleatórios e coloca-los em um tupla. Depois disso, mostra a listagem de números gerados e também indique o menor e vaior valor que estão na tupla.")
numeros = tuple(randint(1, 100) for _ in range(5))
for cont in range (0, 5):
    if cont == 0:
        maior = numeros[cont]
        menor = numeros[cont]
    elif numeros[cont] > maior:
        maior = numeros[cont]
    elif numeros[cont] < menor:
        menor = numeros[cont]
print(f"A tupla gerada foi: {numeros}")
print(f"O número maior foi {maior} e o número menor foi {menor}")
