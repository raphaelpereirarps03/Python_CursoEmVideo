from ex110PacoteMoeda.utilidadesCeV import moeda, dado

print("Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado")

p = dado.leiaDinheiro("Digite o preço: R$")
moeda.resumo(p, 22, 35, True)
