print("""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o número 9;
B) Primeira incidência do número 3;
C) Quais foram os números pares.
""")

numeros = tuple(int(input("Entre com um número: ")) for _ in range(4))

print(f"Os número digitados foram {numeros}")
print(f"O número 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O número 3 apareceu primeiro na {numeros.index(3) + 1}ª posição")
else:
    print(f"Não existe nenhum número 3 na tupla")

pares = tuple(num for num in numeros if num % 2 == 0)
print(f"Os números pares são: {pares}")