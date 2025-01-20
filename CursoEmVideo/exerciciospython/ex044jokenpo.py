from time import sleep
import random
print("Crie um programa que faça o computador jogar Jokenpô com você")

print("\033[1;35m-=-\033[m" * 15)
print("\033[7mMÁQUINA\033[m 🤖: \033[1;34mVAMOS JOGAR \033[1;31mJO\033[m\033[1;32mKEN\033[m\033[1;33mPO\033[m \033[1;34m?\033[m 😈")
print("\033[1;35m-=-\033[m" * 15)
sleep(1)
print("\n\033[31mJO...\033[m")
sleep(1)
print("\033[32mKEN...\033[m")
sleep(1)
print("\033[33mPO!\033[m\n")

sleep(1)
escolhaMaquina = random.randint(1, 3)

escolhaJogador = int(input("""\033[1;33;41mRÁPIDO!\033[m 
\033[31m1 - PEDRA\033[m
\033[32m2 - PAPEL\033[m
\033[33m3 - TESOURA\033[m
\033[1;34mESCOLHA O QUE JOGAR: \033[m"""))


if escolhaJogador == escolhaMaquina:
    if escolhaJogador == 1:
        escolhaJogadorStr = "\033[1;31mPEDRA\033[m"
    elif escolhaJogador ==2:
        escolhaJogadorStr = "\033[1;32mPAPEL\033[m"
    else:
        escolhaJogadorStr = "\033[1;33mTESOURA\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {} """.format(escolhaJogadorStr, escolhaJogadorStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;35mEMPATE! Vamos mais uma vez, hehehe!\033[m 😄 ")
elif escolhaJogador == 1 and escolhaMaquina == 3:
    escolhaJogadorStr = "\033[1;31mPEDRA\033[m"
    escolhaMaquinaStr = "\033[1;33mTESOURA\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {}""".format(escolhaJogadorStr, escolhaMaquinaStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;32mDROGAAAAA! VOCÊ ME VENCEU!\033[m 😡")
elif escolhaJogador == 2 and escolhaMaquina == 1:
    escolhaJogadorStr = "\033[1;32mPAPEL\033[m"
    escolhaMaquinaStr = "\033[1;31mPEDRA\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {}""".format(escolhaJogadorStr, escolhaMaquinaStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;32mDROGAAAAA! VOCÊ ME VENCEU!\033[m 😡")
elif escolhaJogador == 3 and escolhaMaquina == 2:
    escolhaJogadorStr = "\033[1;33mTESOURA\033[m"
    escolhaMaquinaStr = "\033[1;32mPAPEL\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {}""".format(escolhaJogadorStr, escolhaMaquinaStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;32mDROGAAAAA! VOCÊ ME VENCEU!\033[m 😡")
elif escolhaJogador == 1 and escolhaMaquina == 2:
    escolhaJogadorStr = "\033[1;31mPEDRA\033[m"
    escolhaMaquinaStr = "\033[1;32mPAPEL\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {}""".format(escolhaJogadorStr, escolhaMaquinaStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;31mHAHAHAHA! EU VENCI!\033[m 😎")
elif escolhaJogador == 2 and escolhaMaquina == 3:
    escolhaJogadorStr = "\033[1;32mPAPEL\033[m"
    escolhaMaquinaStr = "\033[1;33mTESOURA\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[1;34m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {}""".format(escolhaJogadorStr, escolhaMaquinaStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;31mHAHAHAHA! EU VENCI!\033[m 😎")
elif escolhaJogador == 3 and escolhaMaquina == 1:
    escolhaJogadorStr = "\033[1;33mTESOURA\033[m"
    escolhaMaquinaStr = "\033[1;31mPEDRA\033[m"
    print("""\n\033[1;34mESCOLHA JOGADOR:\033[m {} \n\033[1;34mESCOLHA\033[m \033[7mMÁQUINA\033[m: {}""".format(escolhaJogadorStr, escolhaMaquinaStr))
    print("\033[7mMÁQUINA\033[m 🤖: \033[1;31mHAHAHAHA! EU VENCI!\033[m 😎")
else:
    print("\033[1;34mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m")
