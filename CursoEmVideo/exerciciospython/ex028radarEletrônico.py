print("Faça um programa que leia a velocidade atual de um veículo. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.\nA multa custará R$70,00 por cada Km acima do limite.")

velocidadeAtual = int(input("Qual é a velocidade atual do veículo?"))
if velocidadeAtual > 80:
    multa = (velocidadeAtual - 80) * 7
    print("Calma aí apressadinho, você está acima da velocidade permitida na via (80Km/h)! Você receberá uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia e dirija com segurança!")
