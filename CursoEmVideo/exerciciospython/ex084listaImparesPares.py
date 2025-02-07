print("Crie um programa que onde o usuário possa digitar sete valores e cadastre-os em uma lista única, que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e impares em ordem crescente")

valores = list()
impares = list()
pares = list()

for cont in range (0, 7):
    valor = 0
    valor = (int(input(f"Entre com o {cont + 1}º valor: ")))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
impares.sort()
pares.sort()
valores.append(impares[:])
valores.append(pares[:])
print(f"Todos os valores digitados {valores}")
print(f"Os valores impares são {valores[0]}")
print(f"Os valores pares são {valores[1]}")