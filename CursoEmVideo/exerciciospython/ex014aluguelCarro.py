print("Escreva um programa que pergunte a quantidade de Km rodados percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.")

dias = int(input("Entre com a quantidade dias alugados: "))
kms = float(input("Entre com a quantidade de Km rodados: "))

precoFinal = (dias * 60) + (kms * 0.15)
print("O preço total a se pagar pelo veículo alugado será de {:.2f}".format(precoFinal))
