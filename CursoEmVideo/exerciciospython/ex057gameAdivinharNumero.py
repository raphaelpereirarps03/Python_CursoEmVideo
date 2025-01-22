import random

from time import sleep
print("Melhore o programa 27 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. ")

numeroJogador = 100
tentativasJogador = 0

print("\033[7mMÁQUINA\033[m 🤖: \033[1;34mHAHAHAHA, EU VOLTEI! VAMOS JOGAR UM JOGO DE ADIVINHAÇÃO. EU VOU 'PENSAR EM UM NÚMERO DE 1 À 10, E VOCÊ DEVERÁ ADIVINHAR.'\033[m 😈")
sleep(2)
print("\033[7mMÁQUINA\033[m 🤖: \033[1;34mVAMOS COMEÇAR?\033[m 😈")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(2)
numeroComputador = random.randint(0, 10)
print("\033[7mMÁQUINA\033[m 🤖: \033[1;34mPRONTO, PENSEI!\033[m 😈")
sleep(2)

while numeroComputador!= numeroJogador:
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;31mESTA É A SUA {}º CHANCE!\033[m 😎".format(tentativasJogador + 1))
    numeroJogador = int(input("\033[1;35mADIVINHE QUAL É NÚMERO DE 0 À 1 QUE A MÁQUINA ESTÁ PENSANDO:\033[m "))
    if numeroJogador == numeroComputador:

        print("✅" * 50)
        print("\033[7mMÁQUINA\033[m 🤖: \033[1;32mDROGAAAAAAA! VOCÊ ME VENCEU! EU ESTAVA PENSANDO NO NÚMERO {} E VOCÊ ACERTOU NA {}º TENTATIVA\033[m 😡".format(numeroComputador, tentativasJogador + 1))
        print("✅" * 50)
    else:
        print("❌" * 15)
        print("\033[7mMÁQUINA\033[m 🤖: \033[1;31mHAHAHAHA! EU VENCI!\033[m 😎")
        tentativasJogador += 1
        print("❌" * 15)
        sleep(1)
        print("\033[7mMÁQUINA\033[m 🤖: \033[1;34m TENTE NOVAMENTE!'\033[m 😈")


