print("""Crie um programa que leia a o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo

\033[34m=>\033[m \033[31mAbaixo de 18.5: Abaixo do peso\033[m;
\033[34m=>\033[m \033[32mEntre de 18.5 e 25: Peso ideal\033[m;
\033[34m=>\033[m \033[33mEntre 25 e 30: Sobrepeso\033[m;
\033[34m=>\033[m \033[35mEntre 30 e 40: Obesidade\033[m;
\033[34m=>\033[m \033[1;31mAcima de 40: Obesidade mórbida\033[m.
""")

peso = float(input("Entre com o seu peso (em Kg): "))
altura = float(input("Entre com a sua altura: "))
imc = peso / (altura ** 2)

print("\nSeu IMC ficou em \033[4;34m{:.2f}\033[m".format(imc))
if imc < 18.5:
    print("Você está \033[31mABAIXO DO PESO!\033[m")
elif imc < 25:
    print("\033[1;32mPARABÉNS\033[m, você está com o \033[1;32mPESO IDEAL!\033[m")
elif imc < 30:
    print("\033[1;33mATENÇÃO!\033[m Você está com \033[33mSOBREPESO!\033[m")
elif imc < 40:
    print("\033[1;31mPERIGO!\033[m Você está \033[31mOBESO!\033[m")
else:
    print("\033[4;33;41mPERÍGO EXTREMO! VOCÊ ESTÁ COM OBESIDADE MÓRBIDA!\033[m")
