from math import hypot, pow, sqrt
#usando só a função pronta, hypot
print("Entre com um programa que leia o cateto oposto e o cateto adjascente de um triangulo retângulo e exiba sua respectiva  hipotenusa: ")

catOposto = float(input("Entre com o valor do cateto oposto: "))
catAdjasc = float(input("Entre com o valor do cateto adjascente: "))

print("A hipotenusa do triangulo retângulo fornecido é {:.2f}".format(hypot(catAdjasc, catOposto)));

#Outra forma de fazer esse exercício:
catOposto = float(input("Entre com o valor do cateto oposto: "))
catAdjasc = float(input("Entre com o valor do cateto adjascente: "))

hipotenusa = sqrt(pow(catOposto, 2) + pow(catAdjasc, 2))

print("A hipotenusa do triangulo retângulo fornecido é {:.2f}".format(hipotenusa));

#OU
catOposto = float(input("Entre com o valor do cateto oposto: "))
catAdjasc = float(input("Entre com o valor do cateto adjascente: "))

hipotenusa = (catOposto ** 2 + catAdjasc ** 2)**(1/2)

print("A hipotenusa do triangulo retângulo fornecido é {:.2f}".format(hipotenusa));

