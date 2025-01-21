print("Refaça o  desafio 009 mostrando a tabuada de um número que o usuário informar, só que agora utilizando laço for")

numero = int(input("Entre com um número para exibir sua respectiva tabuada: "))

for c in range(1,11):
    print("{} x {} = {}".format(numero, c,  numero * c))