print("Faça um programa que leia o peso de cinco pessoas. No final, mostre quais foram os o maior e o menor peso lidos")

peso = float(input("Entre com o 1º peso (em KG): "))
maiorPeso = peso
menorPeso = peso
for c in range(1, 5):
    peso = float(input("Entre com o {}º peso (em KG): ".format(c + 1)))
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso

print("O maior peso lido foi {}Kg e o menor peso lido foi {}Kg.".format(maiorPeso, menorPeso))
