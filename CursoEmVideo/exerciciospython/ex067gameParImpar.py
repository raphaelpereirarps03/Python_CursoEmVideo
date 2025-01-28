from random import randint
print("Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.")
escolhaJogador = ""
vitorias = 0
numeroJogador = 9999
while True:
    escolhaJogador = ""
    while escolhaJogador != "I" and escolhaJogador != "P":
        escolhaJogador = str(input("""[P] - Par \n[I] - Impar \nEscolha: """)).strip().upper()[0]
        if escolhaJogador != "I" and escolhaJogador != "P":
            print("Opção inválida, tente novamente!")
        else:
            break

    while numeroJogador > 10:
        numeroJogador = int(input("Qual valor você quer jogar no par ou ímpar? "))
        if numeroJogador > 10:
            print("Opção inválida, tente novamente!")
        else:
            break

    numeroComputador = randint(0, 10)
    total = numeroJogador + numeroComputador

    if total % 2 == 0 and escolhaJogador == "P":
        print(f"Você jogou {numeroJogador} e o computador {numeroComputador}. Total = {total}. DEU PAR E VOCÊ ESCOLHEU PAR! Você ganhou, parabéns!")
        vitorias += 1
    elif total % 2 == 0 and escolhaJogador == "I":
        print(f"Você jogou {numeroJogador} e o computador {numeroComputador}. Total = {total}. DEU PAR E VOCÊ ESCOLHEU IMPAR! Você PERDEU! Vitórias: {vitorias}")
        print("GAME OVER! PROGRAMA ENCERRADO!")
        break
    elif total % 2 != 0 and escolhaJogador == "I":
        print(f"Você jogou {numeroJogador} e o computador {numeroComputador}. Total = {total}. DEU IMPAR E VOCÊ ESCOLHEU IMPAR! Você ganhou, parabéns!")
        vitorias += 1
    else:
        print(f"Você jogou {numeroJogador} e o computador {numeroComputador}. Total = {total}. DEU IMPAR E VOCÊ ESCOLHEU PAR! Você PERDEU! Vitórias: {vitorias}")
        print("GAME OVER! PROGRAMA ENCERRADO!")
        break
