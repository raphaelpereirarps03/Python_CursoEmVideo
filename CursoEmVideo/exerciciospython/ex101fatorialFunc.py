import math
print("Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: O primeiro, que indicará o número a calcular e o outro chamado 'show', que será um valor lógico (opcional) indicando se será mostrado ou não o processo de cálculo de fatorial")


def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número
    :param numero: O número a ser calculado
    :param show: (opcional), mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    if show:
        for c in range(numero, 0, -1):
            print(f"{c}", end=" x " if c > 1 else " = ")

    return print(math.factorial(numero))


valor = int(input("Entre com um valor para calcular seu Fatorial: "))
while True:
    resp = str(input("Deseja exibir o cálculo? [S/N]")).strip().upper()[0]
    if resp in "SN":
        break
    else:
        print("Opção inválida. Tente novamente! Digite apenas S ou N.", end=" ")
print(f"{valor}! = ", end="")
if resp == "S":
    fatorial(valor, True)
else:
    fatorial(valor)
