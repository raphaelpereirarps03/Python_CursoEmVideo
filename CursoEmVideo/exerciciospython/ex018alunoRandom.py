from random import choice
print("Escreva um programa que leia 4 nomes de 4 alunos, onde sorteará qual aluno será ganhará a honra de apagar o quadro")
aluno1 = input("Entre com o nome do primeiro aluno: ")
aluno2 = input("Entre com o nome do segundo aluno: ")
aluno3 = input("Entre com o nome do terceiro aluno: ")
aluno4 = input("Entre com o nome do quarto aluno: ")
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
print(choice(listaAlunos))
