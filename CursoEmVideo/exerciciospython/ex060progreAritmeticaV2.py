print("Refaça o desafio 50 lendo o primeiro termo e a razão de uma PA, para mostrar os 10 primeiros ftermos da progressão utilizando a estrutura while")
c=0

primeiroTermo = int(input("Entre com o primeiro termo da progressão aritmética: "))
razao = int(input("Entre com a razão da PA: "))

print("Os 10 primeiros termos de uma progressão aritmética que tem como primeiro termo {} e a razão de {}, são: ".format(primeiroTermo, razao))
while c < 10:
    print("{}".format(primeiroTermo), end = " → " if c != 9 else "")
    primeiroTermo += razao
    c += 1

