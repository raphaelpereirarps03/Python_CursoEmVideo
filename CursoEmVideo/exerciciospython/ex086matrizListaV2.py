print("""Aprimore o exercício 85 para mostrar no final:
A) A soma de todos os valores PARES digitados;
B) A toma dos valores da 3ª COLUNA
C) O maior valor da 2ª LINHA
""")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = maior = somaColuna = 0

for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()
print('-=' *30)
print(f'A soma dos valores pares é {somaPares}')
for l in range(0, 3):
    somaColuna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somaColuna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
