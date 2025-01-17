from math import radians, cos, sin, tan
print("Faça um programa que irá ler um valor de um ângulo em graus e retorna o seno, cosseno e a tangente dele")
graus = radians(float(input("Entre com um valor em graus do ângulo: ")))
print("O valor de {}º possui:\nO SENO de {:.2f}º;\nO COSSENO {:.2f}º;\nE a TANGENTE {:.2f}º;".format(graus, sin(graus), cos(graus), tan(graus)))

#Para o cálculo de sen, cos, e tan, se usa a medida de graus radianos, então, convertemos o valor fornecido em float (real, flutuante), depois transformamos esse valor flutuante em radianos
