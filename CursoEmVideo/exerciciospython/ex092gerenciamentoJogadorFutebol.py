print("Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ter o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.")
dadosJogador = {}
gols = []
dadosJogador['nome'] = str(input("Nome Jogador: "))
qtdJogos = int(input(f"Quantas partidas {dadosJogador['nome']} jogou? "))
for cont in range(0, qtdJogos):
    gol = int(input(f"Quantos gols na partida {cont + 1}? "))
    gols.append(gol)
    gol = 0
dadosJogador['gols'] = gols
dadosJogador['total'] = sum(gols)
print("-=" * 30)
print(dadosJogador)
print('-=' * 30)
for k, v in dadosJogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-=' * 30)
print(f"O jogador {dadosJogador['nome']} jogou {qtdJogos} partidas:")
for cont in range(0, qtdJogos):
    print(f"   =>  Na partida {cont + 1}, fez {gols[cont]} gols")
print(f"Foi um total de {dadosJogador['total']} gols")
