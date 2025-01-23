print("Escreva um programa que leia um número N inteiro qualquer e mostra na tela os 'N' primeiros elementos da Sequência de Fibonacci. ")
c = 0
anterior = 0
atual = 1

numero = int(input("Entre com a quantidade de elementos da sequência de Fibonacci vocêr quer ver: "))

while c < numero:
    print("{}".format(anterior), end=" → " if c < numero - 1 else "")
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    c += 1

