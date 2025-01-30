print("Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibiidos todos os valores únicos digitados em ordem crescente")

valores=[]
resp = ""
programa = True

while programa == True :
    valor = int(input("Digite um número: "))
    if valor in valores:
        print("Valor duplicado. Não vou adicionar")
    else:
        valores.append(valor)
        print("Valor adicionado com sucesso!")
    while True:
        resp = input("Quer continuar? [S/N]").strip().upper()[0]
        if resp == "N":
            print("Programa encerrado!")
            programa = False
            break
        elif resp == "S":
            break
        else:
            print("Opção inválida, tente novamente!", end=" ")

valores.sort()
print("-=-" * 20)
print(f"Você digitou os valores {valores}")
