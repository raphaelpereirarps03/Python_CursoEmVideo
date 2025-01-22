print("Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo ou não, desconsiderando espaços")

fraseOriginal = str(input("Entre com uma frase qualquer: ")).strip()

fraseMinuscula = fraseOriginal.lower()

fraseConvertida = fraseMinuscula.replace(" ", "")
fraseInvertida = fraseConvertida[::-1]

if fraseConvertida == fraseInvertida:
    print("A frase '{}' é um palíndromo".format(fraseOriginal))
else:
    print("A frase '{}' não é um palíndromo".format(fraseOriginal))
