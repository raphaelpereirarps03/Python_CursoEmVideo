from operator import itemgetter
print("""Crie um programa que leia nome, sexo e idade de várias pessoas. Guardando os dados de cada pessoa em um dicionário e todos os dicionários em um lista. No final, mostre: 
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.
""")

pessoas = list()
dadosPessoas = dict()
somaIdades = 0
programa = True
while programa:
    dadosPessoas['nome'] = str(input("Nome: "))
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()
        if sexo != "M" and sexo !="F":
            print("Opção inválida. Por favor, digite apenas M ou F.", end=" ")
        else:
            dadosPessoas['sexo'] = sexo
            break
    dadosPessoas['idade'] = int(input("Idade: "))
    somaIdades += dadosPessoas['idade']
    pessoas.append(dadosPessoas.copy())
    # dadosPessoas.clear()
    while True:
        continua = str(input("Deseja continuar? [S/N]")).upper().strip()
        if continua != "S" and continua != "N":
            print("Opção inválida. Por favor, digite apenas S ou N.", end=" ")
        elif continua == "S":
            break
        else:
            programa = False
            break

print(f"""A) Ao todo temos {len(pessoas)} pessoas cadastradas;
B) A média de idade é de {somaIdades / len(pessoas):.2f} anos;""")
print(f"C)As mulheres cadastradas foram: ", end="")
for p in pessoas:
    if p['sexo'] == "F":
        print(f"{p['nome']}", end=", " if p != pessoas[-2] else " e ")
print()
print(f"D) Lista das pessoas que estão com a idade acima da média: ")
# Exibição das pessoas com idade acima da média
print("D) Lista das pessoas que estão com a idade acima da média:")
for p in pessoas:
    if p['idade'] > somaIdades / len(pessoas):
        print(f"   Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}")
print("Programa encerrado!")

