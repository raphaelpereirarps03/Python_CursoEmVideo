print("Faça um programa que leia quanto dinheiro em reais uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. (Seguindo a cotação do dia 21/12/2024.)")
print("Cotação do Dólar no dia 21 de Dezembro de 2024: U$1,00 = R$6.09")
reais = float(input("Entre com o valor em Reais (R$): "))
dolares = reais / 6.09
euros = reais / 6.38
ienesJ = reais / 0.039
print("Com R${}(Reais), você pode obter ${:.2f}(Dólar Americano); ₤{:.2f}(Euro); ¥{:.2f}(Yen Japonês)".format(reais, dolares, euros, ienesJ))
