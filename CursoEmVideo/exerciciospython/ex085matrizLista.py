print("Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre na tela a matriz devidamente formatada.")

matriz = list()
linhas = list()
colunas = list()
valor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f"Digite um valor para [{linha}:{coluna}]: "))
        colunas.append(valor)

    # linhas.append(colunas[:])
    # colunas.clear()
    matriz.append(colunas[:])
    colunas.clear()

print("-=-" * 10)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f"[ {matriz[linha][coluna]} ]", end=" ")
    print()

