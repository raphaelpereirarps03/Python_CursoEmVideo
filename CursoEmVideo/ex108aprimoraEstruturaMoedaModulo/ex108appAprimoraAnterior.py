import moeda

print("Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado")

p = float(input("Digite um preço: R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}")
