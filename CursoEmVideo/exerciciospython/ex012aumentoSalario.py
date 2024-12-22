print("Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.")
salario = float(input("Entre com o seu salário (Em R$): "))
print("Salário antigo: R${} \nSalário atual pós aumento de 15%: R${}".format(salario, (salario + (salario * 15 / 100))))
