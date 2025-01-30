print("""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente. Ao final mostre o conteúdo das 3 listas geradas. """)

valores = []
pares = []
impares = []
programa = True

while programa == True:
    valor = int(input("Entre com um valor: "))
    valores.append(valor)
    # print("Valor adicionado a lista de todos os números digitados")
    if valor % 2 == 0:
        pares.append(valor)
        print("Valor adicionado a lista de números PARES")
    else:
        impares.append(valor)
        print("Valor adicionado a lista de números ÍMPARES")
    while True:
        resp = input("Deseja continuar? [S/N]").strip().upper()[0]
        if resp == "N":
            print("Programa encerrado!")
            programa = False
            break
        elif resp == "S":
            break
        else:
            print("Opção inválida, tente novamente!", end=" ")
print(f"Todos os valores digitados: {valores} \nValores pares: {pares} \nValores ímpares: {impares}")