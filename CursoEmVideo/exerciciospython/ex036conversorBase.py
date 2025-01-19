print("Faça um programa que leia um número inteiro qualquer, na base decimal, e peça para o usuário escolher qual será a base de conversão.")
numero = int(input("Entre com um número: "))
escolha = int (input("""Escolha qual será a base de conversão: 
1 - Binário
2 - Octal
3 - Hexadecimal
"""))
if escolha == 1:
    numeroConvertido = bin(numero)
    numeroConvertido = str(numeroConvertido).upper()
    print("O número {} na base decimal, convertido para binário é {}".format(numero, numeroConvertido[2:]))
elif escolha == 2:
    numeroConvertido = oct(numero)
    numeroConvertido = str(numeroConvertido).upper()
    print("O número {} na base decimal, convertido para octal é {}".format(numero, numeroConvertido[2:]))
elif escolha == 3:
    numeroConvertido = hex(numero)
    numeroConvertido = str(numeroConvertido).upper()
    print("O número {} na base decimal, convertido para hexadecimal é {}".format(numero, numeroConvertido[2:]))
else:
    print("\033[31mEscolha inválida!\033[m")