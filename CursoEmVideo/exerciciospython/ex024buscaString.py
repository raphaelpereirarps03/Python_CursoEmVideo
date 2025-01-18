print("Crie um programa que leia o nome completo de uma pessoa e diga se ela tem 'Silva' no nome")
nomeCompleto = str(input("Entre com o seu nome completo: ")).strip()
print("Seu nome tem 'Silva'? {}".format("silva" in nomeCompleto.lower()))