"""
Tuplas: Parecido com os arrays de outras linguagens de programação, são semelhantes as variáveis simples, porém, com a diferença de que podem assumir mais de 1 valor.

Variável simples:
a = 1
A variável A está armazenando o número 1, se eu fizer isso:
a = 5
A variável A joga o 1 fora, e armazena o número 5 em seu lugar, descartando totalmente o valor anterior.

Tuplas = Variáveis compostas:

() - Tupla
[] - Lista
{} - Dicionário

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') OU lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
O python consegue enteder que é uma tupla mesmo sem os parenteses

**** OBS: TUPLAS SÃO IMUTÁVEIS!!! ****
SE VOCÊ DEFINE UMA TUPLA DE UMA FORMA, ATÉ O FIM DA EXECUÇÃO, ELA SERÁ DAQUELE JEITO. SE VOCÊ QUISER MUDAR ELA, VOCÊ TEM QUE PARAR O PROGRAMA, MUDAR ELA, E RODAR DE NOVO. EM TEMPO DE EXECUÇÃO, ELA NÃO SE ALTERA, FAMOSA GABRIELA: "EU NASCI ASSIM, VOU MORRER ASSIM, SEMPRE GABRIELA"

"""
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print("Para exibir todos os valores da tupla: ")
print(lanche)

print("""Para exibir só um valor da tupla, você especifíca o índice:
 Exemplo para exibir só 'Hambúrguer': print(lanche[0])
 Exemplo para exibir só 'Pudim': print(lanche[3])
 Exemplo para exibir só 'Suco': print(lanche[-3])""")
print(lanche[0])
print(lanche[3])
print(lanche[-3])

print("""Para exibir só intervalos fazemos igual com o fatiamento, você especifíca o índice que começa e onde termina, ignorando o terminal né:
 Exemplo para exibir só de 'Hambúrguer' até a 'Pizza' : print(lanche[0:3])
 Exemplo para exibir só 'Hambúrguer' e 'Suco': print(lanche[:2])
 Exemplo para exibir de 'Suco' até 'Pudim': print(lanche[1:])
 Exemplo para exibir do começo ao fim, porém, pulando de 2 em 2 índices
 """)

print(lanche[0:3])
print(lanche[:2])
print(lanche[1:])
print(lanche[::2])

#Provando que tuplas são imutáveis
print("""Vamos provar que tuplas são imutáveis:
lanche [1] = 'Refrigerante', ou seja, índice 1 deixa de armazenar 'Suco' e passa a armazenar 'Refrigerante'
Assim que rodar isso, vai dar problema no código. E a mensagem informando o tipo de erro é: \033[1:31mTypeError: 'tuple' object does not support item assignment\033[m
""")
# lanche [1] = 'Refrigerante'

print("""Para exibir de forma mais bonita, de forma formatada, podemos utilizar 'for'. Exemplo:
<>
for comida in lanche:
    print(f"Eu vou comer {comida}")
print('NOOOSSA, comi pra caramba!')
<>

OUTRA MANEIRA DE FAZER ISSO:
<>
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print("Nooossa, comi pra caramba!")
<>

MENEIRAS DIFERENTES, RESULTADOS IGUAIS, OS EXEMPLOS ANTERIORES É UMA FORMA MAIS SIMPLES, SEM PRECISAR PEGAR  A POSIÇÃO

outro exemplo mas agora trabalhando com posições:
<>
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}, posição {cont}")
<>

consigo o mesmo resultado se utilizar:
<>
for pos, comida in enumerate(lanche):
    print(f"Eu vour comer {comida} na posição {pos}")
<>
""")

for comida in lanche:
    print(f"Eu vou comer {comida}")
print('NOOOSSA, comi pra caramba!\n')

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print("Nooossa, comi pra caramba!\n")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}, posição {cont}")
print("\n")

for pos, comida in enumerate(lanche):
    print(f"Eu vour comer {comida} na posição {pos}")
print("\n")


print("""Para exibir em ordem alfabética e comparando com a normal, para provar que continuamos não mudando a tupla, apenas reoganizamos ela, sem mexer em sua estrutura base: 
<>
    print(sorted(lanche))
    print(lanche)
<>
""")

print(sorted(lanche))
print(lanche)

print("""Podemos JUNTAR (NÃO É SOMAR NEM NADA DO TIPO, É UMA ESPÉCIE DE CONCATENAÇÃO DE TUPLAS) TUPLAS:
<>
    a = (1, 9, 8)
    b = (5, 6, 7, 9)
    c = a + b
    print(a)
    print(b)
    print(c)
    c = b + a
    print(c)
<>

A ordem importa como podemos ver
""")
a = (1, 9, 8)
b = (5, 6, 7, 9)
c = a + b
print(a)
print(b)
print(c)
c = b + a
print(c)

print("Diferente do Java, ou de outras linguagens de programação, o python aceita todos os tipos dentro de uma mesma tupla, diferentes dos vetores do java por exemplo que só aceitam um único tipo. Exemplo:")
pessoa = ("Raphael", 21, 1.75, 70, True)
print(f"Nome da pessoa: {pessoa[0]}; Idade: {pessoa[1]}; Altura: {pessoa[2]}; Peso {pessoa[3]}Kg; Namorando: {pessoa[4]}")

print("Você pode apagar qualquer coisa com o comando 'del', inclusive tuplas, porém, não pode apagar valores da tupla com o del. LEMBRANDO: TUPLAS SÃO IMUTÁVEIS ")