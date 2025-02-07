from random import randint
from time import  sleep
print("Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai gerar 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta")

jogo = list()
jogos = list()
j = numeroJogo = 0
print('-' * 30)
print(f'{"JOGUE NA MEGA SENA":^30}')
print('-' * 30)
qtdJogos = int(input("Quantos jogos vocêr quer que eu sorteie?"))
for cont in range (0, qtdJogos):
    for valorJogo in range (0, 6):
        while True:
            numeroJogo = randint(1, 60)
            if numeroJogo not in jogo:
                jogo.append(numeroJogo)
                break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print(f'{f' SORTEANDO {qtdJogos} JOGOS ':=^30}')
for cont in jogos:
    sleep(0.5)
    print(f"Jogo {j + 1}: {cont}")
    j += 1
print(f"{f' < BOA SORTE! > ':=^30}")
