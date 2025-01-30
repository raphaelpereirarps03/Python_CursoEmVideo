print("Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.")


valores = []
for cont in range (0, 5):
    valor = int(input("Entre com um valor: "))
    if cont == 0 or valor > valores[len(valores) - 1]:
        valores.append(valor)
        print("Valor adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f"Valor adicionado na posição {pos} da lista")
                break
            pos += 1
print("-=-" * 30)
print(f"Os valores digitados em ordem foram {valores}")