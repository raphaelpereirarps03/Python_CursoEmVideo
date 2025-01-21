from time import sleep
print("Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1segundo entre eles ")

print("{:=^70}".format(" Contagem Regressiva Para o Ano Novo!!!"))

for c in range(10, 0, -1):
    print("{}...".format(c))
    sleep(1)
print("✨🎆🥳🎆 FELIZ ANO NOVOOOOOO 🎆🥳🎆✨")
