print("Crie um programa que leia duas notas de um aluno, calcule e exiba sua média")
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média entre as notas {:.1f} e {:.1f} é {:.1f}.".format(nota1, nota2, media))
