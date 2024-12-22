print("Faça um algorítmo que leia o preço de um produto e exiba seu novo preço com 5% de desconto.")
preco = float(input("Entre com o preço de um produto em reais (R$): "))
print("Preço pré-desconto: R${} \nPreço pós-desconto de 5%: R${}".format(preco, (preco - (preco * 5 / 100))))
