print("Faça um programa que leia a largura e a altura de uma parede, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²")
altura = float(input("Entre com a altura da parede em metros: "))
largura = float(input("Entre com a largura da parede em metros: "))
area = altura * largura
qtdTinta = area / 2
print("Altura = {}m \n Largura = {}m \n Área = {}m² \n quantidade necessária de tinta para pintá-la (Em litros (l)): {:.1f}l".format(altura, largura, area, qtdTinta))
