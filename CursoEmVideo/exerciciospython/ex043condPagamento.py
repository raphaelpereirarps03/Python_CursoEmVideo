print(f"""Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
=> À vista dinheiro/cheque: 10% de desconto;
=> À visto no cartão: 5% de desconto;
=> Em até 2x no cartão: preço normal;
=> 3x ou mais no cartão: 20% de juros.""")

precoProduto = float(input("\nEntre com o preço do produto: R$"))
formaPgto = int(input("""Entre com a forma de pagamento: 
1 - À vista dinheiro: 10% de desconto; 
2 - À vista cheque: 10% de desconto; 
3 - À vista cartão: 5% de desconto;
4 - Cartão 2x sem juros: preço normal ;
5 - Cartão 3x igual ou superior: 20% de juros.
"""))

if formaPgto > 0 and (formaPgto <= 2):
    valorPgto = precoProduto - ((precoProduto * 10) / 100)
elif formaPgto == 3:
    valorPgto = precoProduto - ((precoProduto * 5) / 100)
elif formaPgto == 4:
    valorPgto = precoProduto
elif formaPgto == 5:
    valorPgto = precoProduto + ((precoProduto * 20)/100)
else:
    print("Opção inválida, tente novamente!")

print("O preço final do seu produto ficou em R${:.2f}".format(valorPgto))