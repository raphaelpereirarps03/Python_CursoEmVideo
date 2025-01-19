print("""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
 da passagem, cobrando R$0,50 por Km para viagens de até 200Km em R$0,45 para viagens mais longas""")

kmViagem = float(input("Entre com a distância da viagem (em KM): "))
print("Você está prestes a começar uma viagem de {}Km.".format(kmViagem))
if kmViagem <= 200 :
    precoViagem = kmViagem * 0.50;
else:
    precoViagem = kmViagem * 0.45
print("E o preço da sua passagem será de R${:.2f}.".format(precoViagem))