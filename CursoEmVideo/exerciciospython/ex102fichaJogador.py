print("Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.")


def ficha(nomeJogador = "<desconhecido>", gols = 0):
    return print(f"O jogador {nomeJogador} fez {gols} gol(s) no campeonato")


#programa principal
print("-" * 30)
nome = str(input("Nome do Jogador: ")).strip()
qtdGols = (input("Total de gols: "))
if nome and qtdGols:
    ficha(nome, int(qtdGols))
elif nome:
    ficha(nomeJogador = nome)
elif qtdGols:
    ficha(gols = qtdGols)
else:
    ficha()
