#Tipos primitivos:
# str : String
# float : Real
# int : Inteiro
# bool: Booleano
algo = input("Digite algo: ")
print("Informações de: ", algo)
print("Tipo primitivo: ", type(algo))
print("É numérico?", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É um alfanumérico?", algo.isalnum())
print("É representável como um valor ASCII 7-bit US?", algo.isascii())
print("É um dígito? (ou símbolo de acordo com a Unicode)", algo.isdigit())
print("Todos os caracteres são minúsculos?", algo.islower())
print("Todos os caracteres são maiúsculos?", algo.isupper())
print("É decimal?", algo.isdecimal())
print("É um identificador válido de acordo com as regras de nomenclatura da linguagem?", algo.isidentifier())
print("É imprimível?", algo.isprintable())
print("É somente espaços?", algo.isspace())
print("É um título? (Todo primeiro caractere de cada palavra for maiúsculo e os demais minúsculos)", algo.istitle())
