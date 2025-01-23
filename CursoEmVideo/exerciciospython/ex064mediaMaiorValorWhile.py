print("Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.")

programa = True
contagem = 0
somatoria = 0
maior = 0
menor = 0

while programa:
    numero = int(input("Entre com um valor inteiro: "))
    if contagem == 0:
        menor = numero
        maior = numero
    elif numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero

    contagem += 1
    somatoria += numero
    repetir = True
    while repetir:
        resposta = str(input("Deseja continuar? [S/N]\n")).strip().upper()[0]
        if resposta == "N":
            print("Programa encerrado!")
            programa = False
            repetir = False
        elif resposta == "S":
            repetir = False
        else:
            print("Resposta inválida, tente novamente!")

media = somatoria / contagem
print("O maior valor digitado: {} \nE o menor valor digitado foi: {}".format(maior, menor))
if maior == menor:
    print("Os dois são iguais")
print("A média de todos os {} valores digitados é igual à: {:.2f}".format(contagem, media))