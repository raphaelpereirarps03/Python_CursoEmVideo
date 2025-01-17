from math import trunc
print("Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.")
numero = float(input("Entre com um número real qualquer para separarmos sua parte inteira: "))
print("O numéro digitado foi {} e sua parte inteira é {}".format(numero, trunc(numero)))

#Segunda forma de resolução sem nem usar math
numero = float(input("Entre com um número real qualquer para separarmos sua parte inteira: "))
print("O numéro digitado foi {} e sua parte inteira é {}".format(numero, int(numero)))
#Pego apenas a parte inteira do número, transoformando ele de float para int    