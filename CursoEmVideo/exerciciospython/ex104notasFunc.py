print(""" Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
-> A quantidade de notas;
-> A maior nota;
-> A menor nota;
-> A média da turma;
-> E a situação(opcional).
Adicione também as docstrings da função.
""")

def notas(*num, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos (aceita N notas)
    :param situacao: valor opcional que indica se deve ou não exibir a situação da turma
    :return: dicionário com várias informações sobre situação turma
    """
    notas = [*num]
    tamanhoNotas = len(notas)
    media = sum(notas) / tamanhoNotas
    if 0 >= media <= 4:
        textSituacao = "RUIM"
    elif media < 7:
        textSituacao = "RAZOÁVEL"
    else:
        textSituacao = "BOA"
    for p, n in enumerate(notas):
        if p == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    infos = {'total': tamanhoNotas, 'maior': maior, 'menor': menor, 'media': media, 'situacao': textSituacao}
    if situacao == False:
        infos.pop('situacao')
    return infos


#programa principal
resp = notas(5.5, 9.5, 6.5, 7.5, 1.6, 8.4, situacao=True)
print(resp)
