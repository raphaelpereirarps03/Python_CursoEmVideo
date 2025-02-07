def area (largura, comprimento):
    a = largura * comprimento
    print(f"A área do terreno de {largura} x {comprimento} é de {a:.1f}m²")


print("Controle de Terrenos")
print('-' * 30)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)