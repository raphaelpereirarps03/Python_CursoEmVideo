print("Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e a soma entre eles")

numero = 0
somatoria = 0
contagem = 0

while numero != 999:
    numero = int(input("Digite um valor: "))
    if numero != 999:
        somatoria += numero
        contagem += 1

print("Você digitou {} números inteiros válidos e a somatória de todos eles é igual à {}".format(contagem, somatoria))
