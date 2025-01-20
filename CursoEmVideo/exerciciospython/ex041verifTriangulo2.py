print("Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. Se sim, diga qual é o tipo de triangulo")

print("{:=^60}".format(" Analisador de Triângulos "))


a = float(input("Entre com o segmento A do triângulo: "))
b = float(input("Entre com o segmento B do triângulo: "))
c = float(input("Entre com o segmento C do triângulo: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("É possível formar um triângulo com esses segmentos!")
    if a == b == c:
        print("O triângulo será equilátero (TODOS OS SEGMENTOS IGUAIS)")
    elif (a == b != c) or (b == c != a) or (c == a != b):
        print("O triângulo será isósceles (2 SEGMENTOS IGUALS)")
    else:
        print("O triângulo será escaleno (TODOS OS LADOS SÃO DIFERENTES)")

else:
    print("Não é possível formar um triângulo com esses segmentos!")