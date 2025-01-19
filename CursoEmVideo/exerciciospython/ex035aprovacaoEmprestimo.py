import random
from time import sleep
print("Crie um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. ")
print("Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado")

salarioEmpregado = float(input("Entre com o salário do comprador: R$"))
valorCasa = float(input("Entre com o valor do imóvel: R$"))
anosPagamento = int(input("Em quantos anos ele vai pagar? "))

qtdParcelasMensais = anosPagamento * 12
valorParcelas = valorCasa / qtdParcelasMensais
print("\033[33;41mCALCULANDO...\033[m")
sleep(2)
print("O valor das prestações mensais ficariam em \033[34mR${:.2f}".format(valorParcelas))
print("\033[33;41mPROCESSANDO...\033[m")
sleep(2)
if valorParcelas > (salarioEmpregado * 30 / 100):
   print("\033[31mEMPRÉSTIMO NEGADO!\033[m Pois \033[31mR${:.2f}\033[m é equivalente ou excede 30% do salário do comprador (\033[33mR${:.2f}\033[m)".format(valorParcelas, salarioEmpregado))
else:
    print("\033[32mEMPRESTIMO APROVADO!\033[m".format(valorParcelas))