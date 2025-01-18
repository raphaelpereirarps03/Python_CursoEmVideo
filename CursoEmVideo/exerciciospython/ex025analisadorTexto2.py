print("""Crie um programa que leia o nome de uma frase via teclado e mostre:
1 - Quantas vezes aparece a letra 'A';
2 - Em que posição ela aparece a primeira vez;
3 - Em que posição ela aparece pela última vez.""")
frase = str(input("Entre com uma frase: ")).strip()
print("A letra A aparece {} vezes".format(frase.lower().count("a")))
print("A letra A aparece pela primeira vez na posição {}".format(frase.lower().find("a")))
print("A letra A aparece pela última vez na posição {}".format(frase.lower().rfind("a")))