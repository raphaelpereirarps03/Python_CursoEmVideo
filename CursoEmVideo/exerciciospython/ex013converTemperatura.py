print("Faça um leia uma temperatura em ºC e converta para ºF e exiba o resultado da conversão")
celsius = float(input("Entre com uma temperatura ºC: "))
fahrenheit = ((celsius * 9)/5 + 32)

print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF".format(celsius, fahrenheit))
