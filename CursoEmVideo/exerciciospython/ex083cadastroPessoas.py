print("""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
""")
programa = True
pessoas = list()
dados = list()
nomesPesados = ""
nomesLeves = ""
while programa == True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        resposta = str(input("Deseja continuar? [S/N]")).strip()[0]
        if resposta in 'Nn':
            print("Programa encerrado!")
            programa = False
            break
        elif resposta in 'Ss':
            break
        else:
            print("Resposta inválida, tente novamente!", end=" ")

# for pessoa in pessoas:
#     print(pessoa)
# print("Fim")

maisPesado = pessoas[0][1]
maisLeve = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] > maisPesado:
        maisPesado = pessoa[1]
    elif pessoa[1] < maisLeve:
        maisLeve = pessoa[1]

print(maisPesado)
print(maisLeve)
print(f"Ao todo você cadastrou {len(pessoas)} pessoas")
print(f"O maior peso cadastrado foi de {maisPesado}Kg. Peso de ", end="")
for pessoa in pessoas:
    if pessoa[1] == maisPesado:
        print(f"{pessoa[0]}", end=", " if pessoa != pessoas[-1] else "")

print(f"\nO menor peso cadastrado foi de {maisLeve}Kg. Peso de ", end="")
for pessoa in pessoas:
    if pessoa[1] == maisLeve:
        print(f"{pessoa[0]}", end=", " if pessoa != pessoas[-1] else "")