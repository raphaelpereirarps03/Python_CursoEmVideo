from random import randint
from time import sleep
def sorteia():
    return randint(1, 11)

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    return print(soma)


valores = []
for c in range (0, 5):
    valores.append(sorteia())
print("Sorteando 5 valores da lista: ", end="")
for v in valores:
    sleep(0.5)
    print(f"{v} ", end="")
print("PRONTO!")
print(f"Somando os valores pares de {valores}, temos ", end="")
somaPar(valores)
