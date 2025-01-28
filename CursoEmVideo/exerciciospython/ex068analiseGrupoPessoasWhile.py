print("""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá se perguntar se o usuário quer ou não continuar. No final, mostre: 
A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.
""")
continua = ""
pessoa = 1
programa = True
qtdMulheresMenores = qtdHomens = qtdPessoasMaiores = 0
while programa:
    continua = ""
    print("-" * 30)
    print(f"{f' Cadastro Pessoa {pessoa} ':^30}")
    print("-" * 30)
    idade = int(input("Quantos anos você tem? "))
    if idade >= 18:
        qtdPessoasMaiores += 1
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().lower()[0]
    if sexo == "m":
        qtdHomens += 1
    if sexo == "f" and idade < 20:
        qtdMulheresMenores += 1
    while continua != "s" and continua != "n":
        continua = str(input("Quer continuar? [S/N]")).strip().lower()[0]
        if continua == "n":
            programa = False
            break
        elif continua == "s":
            pessoa += 1
        else:
            print("Opção inválida, tente novamente")
print(f"Você cadastrou {pessoa} pessoas")
print(f"A Quantidade pessoas maiores de 18 anos cadastradas: {qtdPessoasMaiores}")
print(f"A Quantidade total de homens cadastrados: {qtdHomens}")
print(f"A Quantidade de mulheres menores de 20 anos de idade cadastradas: {qtdMulheresMenores}")
