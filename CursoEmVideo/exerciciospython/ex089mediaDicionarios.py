print("Crie um programa que leia nome e média de um aluno, guardando também a situação final em um dicionário. No final, mostre o conteúdo da estrutura na tela.")
dadosAluno = {}
dadosAluno['nome'] = str(input("Entre com o nome do aluno: "))
dadosAluno['media'] = float(input("Entre com a média do aluno: "))
if dadosAluno['media'] <= 4:
    dadosAluno['situacao'] = "Reprovado"
elif dadosAluno['media'] < 6:
    dadosAluno['situacao'] = "Recuperação"
else:
    dadosAluno['situacao'] = "Aprovado"
print("-=" * 30)
for k, v in dadosAluno.items():
    print(f"    -> {k} é igual à {v}")
