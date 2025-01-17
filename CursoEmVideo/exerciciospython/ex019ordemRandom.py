from random import sample
print("Na mesma turma do exercício anterior, o professor agora quer sortear uma ordem de apresentação de um trabalho. Como faremos isso?")
aluno1 = input("Entre com o nome do primeiro aluno: ")
aluno2 = input("Entre com o nome do segundo aluno: ")
aluno3 = input("Entre com o nome do terceiro aluno: ")
aluno4 = input("Entre com o nome do quarto aluno:")

listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]

print(sample(listaDeAlunos, len(listaDeAlunos)))
