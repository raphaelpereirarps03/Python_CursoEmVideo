print("""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra;
B) Quantos prodtuso custam mais de R$1000;
C) Qual é o nome do produto mais barato
""")
produto = 1
programa = True
continua = nomeProdutoBarato = nomeProduto = ""
precoProdutoBarato = qtdProdutosCaros = precoTotal = precoProduto = 0
while programa:
    continua = ""
    print("-" * 30)
    print(f"{f' Cadastro Produto {produto} ':^30}")
    print("-" * 30)
    nomeProduto = str(input("Qual é o nome do produto? "))

    precoProduto = float(input("Qual é o preço do produto? R$"))
    precoTotal += precoProduto
    if precoProduto >= 1000:
        qtdProdutosCaros += 1
    if produto == 1:
        nomeProdutoBarato = nomeProduto
        precoProdutoBarato = precoProduto
    else:
        if precoProduto < precoProdutoBarato:
            nomeProdutoBarato = nomeProduto
            precoProdutoBarato = precoProduto
    while continua != "s" and continua != "n":
        continua = str(input("Quer continuar? [S/N]")).strip().lower()[0]
        if continua == "n":
            programa = False
            break
        elif continua == "s":
            produto += 1

        else:
            print("Opção inválida, tente novamente")
print(f"Você cadastrou {produto} produtos")
print(f"A quantidade produtos que custam mais de R$1000,00: {qtdProdutosCaros}")
print(f"O produto mais barato custa R${precoProdutoBarato:.2f} e seu nome é {nomeProdutoBarato}")
print(f"Total a se pagar: R${precoTotal:.2f}")