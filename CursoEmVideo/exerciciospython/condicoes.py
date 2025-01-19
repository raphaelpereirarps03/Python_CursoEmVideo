print("Criar um programa que exiba se um carro é novo ou velho")
tempo = int(input("Quantos anos tem o seu carro? "))
if tempo<=3:
    print("Carro novo!")
else:
    print("Carro velho!")
print("Fim do programa")
print("")
#Outra forma de escrever o programa acima, mas de forma mais simples com e com menos linhas:
tempo = int(input("Quantos anos tem o seu carro? "))
print("Carro novo" if tempo<=3 else "Carro velho")
print("Fim do programa")
print("")
#É semelhante aos ifs ternários de outras linguagens de programação, como por exemplo o JavaScript. Mas vale lembrar:
#NÃO EXISTE IF TERNÁRIO EM PYTHON

#IF Simples
nome = str(input('Qual é o seu nome?')).strip()
if nome.lower() == "raphael":
    print("Que nome lindo você tem!")
print("Bem vindo(a), {}!".format(nome))
print("")
#IF Composto
nome = str(input('Qual é o seu nome?')).strip()
if nome.lower() == "raphael":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normalzinho...hehe...")
print("Bem vindo(a), {}!".format(nome))
print("")
#If Aninhado (mais de 1 if)
nome = str(input('Qual é o seu nome?')).strip()
if nome.lower() == "raphael":
    print("Que nome lindo você tem!")
elif nome.lower() == "joão" or nome.lower() == "maria":
    print("Seu nome é bem comum no Brasil")
else:
    print("Seu nome é tão normalzinho...hehe...")
print("Bem vindo(a), {}!".format(nome))
print("")