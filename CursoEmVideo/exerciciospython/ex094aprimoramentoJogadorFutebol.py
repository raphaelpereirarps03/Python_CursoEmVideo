print("Aprimore o desafio 92 para que ele funcione com vários jogadoresm incluindo o sistema de visualização de detalhes do aproveitamento de cada jogador.")

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totalPartidas = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, totalPartidas):
        partidas.append(int(input(f"Quantos gols na partida {c + 1}?")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
print('-' * 40)
print('-=' * 30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para encerrar o programa)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! Não existe jogador com o código {busca}")
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 40)
print(" <<< VOLTE SEMPRE >>>")