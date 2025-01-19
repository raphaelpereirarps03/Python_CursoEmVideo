print("Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo")
print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

a = float(input("Entre com o segmento A do triângulo: "))
b = float(input("Entre com o segmento B do triângulo: "))
c = float(input("Entre com o segmento C do triângulo: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("É possível formar um triângulo com esses segmentos!")
else:
    print("Não é possível formar um triângulo com esses segmentos!")