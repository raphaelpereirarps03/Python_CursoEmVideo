print("Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte")

zerovinte = ("zero", "um", "dois", "três", "quatro","cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinte", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    numero = int(input("Entre com um número de 0 à 20: "))
    if numero <= 20 and numero >= 0:
        break
    else:
        print("Número inválido, tente novamente!")
for cont in range (0, len(zerovinte)):
    if numero == cont:
        print(f"Você escolheu o número {zerovinte[cont]}")