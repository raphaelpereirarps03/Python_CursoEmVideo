from time import sleep

print("Refaça o desafio 50, lendo o primeiro termo e a razão de uma PA, para mostrar os 10 primeiros termos de uma progressão utilizando a estrutura while")

programa = True
c = 0
respContinuacao = 10
contadorVezes = 0
termos = []

primeiroTermo = int(input("Entre com o primeiro termo da progressão aritmética: "))
razao = int(input("Entre com a razão da PA: "))

print("Os 10 primeiros termos de uma progressão aritmética que tem como primeiro termo {} e a razão de {}, são: ".format(primeiroTermo, razao))

while programa:
    while c < respContinuacao:
        sleep(0.35)
        print("{}".format(primeiroTermo), end = " → " if c != respContinuacao - 1 else "\n")
        termos.append(primeiroTermo)
        primeiroTermo += razao
        c += 1

    respContinuacao = int(input("Mais quantos termos vocêr quer mostrar? \033[1:31m\nDIGITE 0 SE QUISER ENCERRAR O PROGRAMA: \033[m\n"))
    if respContinuacao == 0:
        contadorVezes += c
        print("Programa encerrado e foram exibidos {} termos".format(contadorVezes))
        print("Todos os termos exibidos: ", termos)
        programa = False
    else:
        contadorVezes += c
        c = 0
