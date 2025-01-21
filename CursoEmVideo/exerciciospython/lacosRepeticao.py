for i in range (1, 6):
    print("Hello Laço!")

for j in range (0, 6):
    print(j)

#Vale lembrar que quando trabalhamos com range, o último parâmetro não é incluso na contagem, então no caso de 0 à 6 a iteração irá de 0 à 5, a com 6 contagens mesmo (0, 1, 2, 3, 4, 5)

for k in range (0, 101, 10):
    print(k)
#Aqui, o programa irá exibir uma contagem de 0 à 100 pulando de 10 em 10, então o 3º parâmetro será o passo do programa

inicio = int(input("Entre com o início do laço: "))
fim = int(input("Entre com o fim do laço: "))
passo = int(input("De quanto em quanto você quer que esse programa ande: "))
for contador in range(inicio, fim + 1, passo):
    print(contador)
#Podemos trabalhar com variáveis também nos laços

