print("Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista")

valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    if cont == 0:
        maior = valores[cont]
        posMaior = cont
        menor = valores[cont]
        posMenor = cont
    elif valores[cont] > maior:
        maior = valores[cont]
        posMaior = cont
    elif valores[cont] < menor:
        menor = valores[cont]
        posMenor = cont
print(f"O maior valor digitado foi {maior} no índice {posMaior} e o menor valor digitado foi {menor} no índice {posMenor}")
