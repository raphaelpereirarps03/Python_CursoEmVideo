print("Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista")

valores = []
posMaior = ""
posMenor = ""
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))
    if cont == 0:
        maior = valores[cont]
        # posMaior = cont
        menor = valores[cont]
        # posMenor = cont
    elif valores[cont] > maior:
        maior = valores[cont]
#         posMaior = cont
    elif valores[cont] < menor:
        menor = valores[cont]
#         posMenor = cont

for c, v in enumerate(valores):
    if v == maior:
        posMaior += str(f"{c}...")
for c, v in enumerate(valores):
    if v == menor:
        posMenor += str(f"{c}...")
# print("Cheguei ao final da lista")
print(f"O maior valor digitado foi {maior} nos índices {posMaior} \nE o menor valor digitado foi {menor} nos índices {posMenor}")
