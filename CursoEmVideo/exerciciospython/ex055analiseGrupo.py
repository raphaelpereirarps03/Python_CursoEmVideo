print("""Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
 => A média de idade do grupo;  
 => Qual é o nome do homem mais velho;
 => Quantas mulheres têm menos de 20 anos
 """)

nome = str(input("Entre com o nome da 1º pessoa: "))
idade = int(input("Entre com a idade da 1º pessoa: "))
sexo = int(input("Qual é seu sexo?\n 1- Masculino / 2 - Feminino \n"))

qtdMulheres20 = 0
mediaIdade = idade
idadeHomemMaisVelho = 0
if sexo == 1:
    if idade > idadeHomemMaisVelho:
        nomeHomemMaisVelho = nome
        idadeHomemMaisVelho = idade
elif sexo == 2:
    if idade < 20:
        qtdMulheres20 += 1
else:
    print("Sexo não informado ou opção inválida")

for c in range(1, 4):
    nome = str(input("Entre com o nome da {}º pessoa: ".format(c + 1)))
    idade = int(input("Entre com a idade da {}º pessoa: ".format(c + 1)))
    sexo = int(input("Qual é seu sexo?\n 1- Masculino / 2 - Feminino \n"))

    mediaIdade += idade
    if sexo == 1:
        if idade > idadeHomemMaisVelho:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
    elif sexo == 2:

        qtdMulheres20 += 1
    else:
        print("Sexo não informado ou opção inválida")

mediaIdade = mediaIdade / 4

print("A média de idade do grupo é {}".format(mediaIdade))
print("O nome do homem mais velho é {}, com {} anos".format(nomeHomemMaisVelho, idadeHomemMaisVelho))
print("A quantidade de mulheres com a idade inferior à 20 anos é {}".format(qtdMulheres20))