import datetime
print("Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade")
anoNasc = int(input("Entre com o ano de seu nascimento: "))

sexo = int(input("""Qual é o seu sexo?
1 - Masculino
2 - Feminino
Entre com o número respectivo, 1 ou 2: """))

if sexo == 1:
    print("Seu sexo biológico é 'Masculino', você precisa se alistar. ")
    anoAtual = datetime.date.today().year
    idade = anoAtual - anoNasc
    print("Você nasceu em {}. Em {} você tem ou terá {} ano(s) ".format(anoNasc, anoAtual, idade))
    if idade < 18:
        print("Você ainda vai se alistar daqui à {} ano(s)".format(18 - idade))
        print("Seu ano de alistamento será {} ".format(anoAtual + (18 - idade)))
    elif anoAtual - anoNasc == 18:
        print("Você está na hora de se alistar!")
    else:
        resposta = str(input("Você já se alistou? Sim ou Não? ")).strip().lower()
        if resposta == "sim":
            print("Você não precisa se alistar e seu alistamento foi em {}".format(
                anoAtual - ((anoAtual - anoNasc) - 18)))
        elif resposta == "não" or "nao":
            print(
                "Seu alistamento foi em {}. Você precisa se alistar \033[1;31mURGENTEMENTE\033[m. Você está {} ano(s) atrasado(s)".format(
                    (anoAtual - ((anoAtual - anoNasc) - 18)), (anoAtual - anoNasc) - 18))
        else:
            print("Resposta inválida. Tente novamente!")
elif sexo == 2:
    print("Seu sexo biológico é 'Feminino', você não precisa se alistar. ")
else:
    print("Opção inválida. Tente novamente!")




