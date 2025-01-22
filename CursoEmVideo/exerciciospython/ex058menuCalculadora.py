from time import sleep

print("""Crie um programa que leia dois números e mostre na tela um menu: 
[1] - Somar;
[2] - Multiplicar;
[3] - Descobrir Maior;
[4] - Novos número;
[5] - Sair do programa

Seu programa deverá realizar a ação de cada uma opções.
""")

programa = True

while programa == True:
    valor1 = float(input("Entre com o 1º valor: "))
    valor2 = float(input("Entre com o 2º valor: "))
    opcao = int(input("""Escolha uma das opções: 
    [1] - Somar;
    [2] - Multiplicar;
    [3] - Descobrir Maior;
    [4] - Novos números
    [5] - Sair
    """))
    if opcao == 1:
        sleep(1)
        print("Opção 4 - Soma")
        resultSoma = valor1 + valor2
        print("A soma de {} + {} é igual à {} 🤓".format(valor1, valor2, resultSoma))
    elif opcao == 2:
        sleep(1)
        print("Opção 2 - Multiplicação")
        resultMultiplicacao = valor1 * valor2
        print("A multiplicação de {} * {} é igual à {} 😍".format(valor1, valor2, resultMultiplicacao))
    elif opcao == 3:
        sleep(1)
        print("Opção 3 - Exibindo o maior número")
        if valor1 > valor2:
            maior = valor1
            print("Entre {} e {}, o maior valor é {} 😎".format(valor1, valor2, maior))
        elif valor2 > valor1:
            maior = valor2
            print(("Entre {} e {}, o maior valor é {} 😎".format(valor1, valor2, maior)))
        else:
            print("Não existe valor maior, ambos são iguais 😎")
    elif opcao == 4:
        sleep(1)
        print("Opção 4 - Novos números")
        print("Você será redirecionado para o menu novamente. 😉👍")
    elif opcao == 5:
        sleep(1)
        print("Opção 5 - Sair")
        print("Programa Encerrado. Até a próxima! 😉👍" )
        programa = False
    else:
        print("A opção {} é inválida, não existe no menu. Tente novamente! 😊")

    if programa == True and opcao != 4:
        print("Reiniciando programa 😁")
        sleep(1)
