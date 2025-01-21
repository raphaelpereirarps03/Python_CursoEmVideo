print("Escreva um programa que leia 6 números inteiros e realize a soma apenas daqueles que forem pares. Impares, desconsiderar")

soma = 0
numerosParesStr = ""
for c in range (0, 6):
    numero = int(input("Entre com um número inteiro qualquer: "))
    if numero % 2 == 0:
        soma += numero
        numerosParesStr += str("{}, ".format(numero))

print("A soma dos números {}é igual a {}".format(numerosParesStr, soma))