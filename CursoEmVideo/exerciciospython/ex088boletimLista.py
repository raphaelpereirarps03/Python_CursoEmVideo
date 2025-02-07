print("Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as duas notas de cada individualmente")
alunos = list()
aluno = list()
notas = list()
nome = ""
programa = True
contAluno = 1

while programa:
    nome = str(input("Entre com o nome do aluno: "))
    aluno.append(nome)
    for cont in range(0, 2):
        notas.append(float(input(f"Entre com a {cont + 1}º nota do aluno {contAluno}: ")))
    aluno.append(notas[:])
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()
    while True:
        resp = str(input("Deseja continuar? ")).strip().upper()[0]
        if resp in 'Nn':
            programa = False
            break
        elif resp in 'Ss':
            break
        else:
            print("opção inválida. Tente novamente!", end=" ")
    contAluno += 1
print("-=" * 30)
print(f'{"Nº":^8}{"Nome":^8}{"Media":>}')
print("-" * 30)
contAluno = 0
for cont in alunos:
    print(f"{contAluno:^8}{cont[0]:^8}{(sum(cont[1]))/len(cont[1]):>8.2f}")
    contAluno += 1
while True:
    print("-" * 30)
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        print("Programa encerrado com sucesso!")
        break
    if opcao <= len(alunos) - 1:
        print(f"Notas de {alunos[opcao][0]} são {alunos[opcao][1]}")
    if opcao > len(alunos) - 1:
        print("\033[31mOpção de aluno inválida. Tente novamente!\033[m")

print("<<< VOLTE SEMPRE >>>")