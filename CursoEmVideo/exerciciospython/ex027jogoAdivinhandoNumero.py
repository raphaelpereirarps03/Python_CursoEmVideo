import random
from time import sleep
print("Escreva um programa que faça o computador 'pensar' em um número número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.")

print("-=-" * 35)
print("Olá! Vamos brincar um pouco? Vou pensar em um número de 0 à 5 e eu quero que você adivinhe. Vamos começar?")
print("-=-" * 35)
numero = random.randint(0, 5);
print("PENSANDO...")
sleep(2)
print("PRONTO!")
palpite = int(input("Em que número eu pensei? "))
print("RUFEM OS TAMBORES...")
sleep(3)
if palpite == numero :
    print("Parabéns!!! Você acertou. ^^ ")
else:
    print("Ganhei, hahaha! Eu pensei no {} e não no {}!".format(numero, palpite))