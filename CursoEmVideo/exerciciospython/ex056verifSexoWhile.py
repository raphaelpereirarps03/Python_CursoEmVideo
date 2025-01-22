print("Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.")

sexo = ""
while sexo != 'M' and sexo != 'F':
    sexo = str(input("Digite seu sexo: [M/F] ")).upper()
    if sexo != 'M' and sexo != 'F':
        print("Opção inválida, tente novamente. Lembrando [M - Masculino/F - Feminino]")

if sexo == 'M':
    print("Você digitou {}. Logo, é do sexo masculino!".format(sexo))
else:
    print("Você digitou {}. Logo, você é do sexo feminino!".format(sexo))