from time import sleep
print("""Crie um programa que leia duas notas de um alune e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
1 - Média abaixo de 5.0: REPROVADO;
2 - Média entre 5.0 e 6.9: RECUPERAÇÃO;
3 - Média 7.0 ou superior: APROVADO.
""")

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2) / 2

print("\033[1;31;43mCALCULANDO...\033[m")
sleep(2)

print("A média da sua nota é: \033[4;34m{}\033[m".format(media))
if media < 5:
    print("Infelizmente você está \033[1;33;41mREPROVADO!\033[m 😢")
elif media < 7:
    print("Você tem mais uma chance. Está de \033[1;33;44mRECUPERAÇÃO!\033[m 😱")
else:
    print("PARABÉNS! Você está \033[1;42mAPROVADO!\033[m 😄")