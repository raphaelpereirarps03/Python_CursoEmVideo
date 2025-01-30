"""
Listas, diferentes das tuplas, elas são mutáveis, podemos adicionar, remover, editar seus valores
Estrutura bem semelhante às tuplas

lista.append() - Para add algum item na lista, neste caso, ele cria um novo indíce e aloca o valor lá

lista.insert(indice, valor) - Adiciono um valor em qualquer posição, índice, chave e edita a estrutura da lista automaticamente

del lista[indice] - Excluo algum ítem da lista
lista.pop(indice) - Exclui o item da lista (normalmente usado para apagar o último valor da lista)
lanche.remove('valor') - Diferente das funções citadas anteriormente, que buscavam o ítem a ser excluído com base em seu índice, aqui, ele busca com base em seu valor realmente
Todos esses métodos de exclusão reestrturam a lista, seus índices, de forma automática

Podemos criar listas atráves de ranges também.
lista = list(range(inicial, final))

lista.sort - Organiza a lista em ordem crescente de valores, ou alfabética
lista.sort(reverse=True) - Organizamos a lista de forma reversa, então ficaria decrescente ou de Z-A
"""

"""
num = [2, 5, 9, 1] # Crie a lista com esses valores iniciais
num[2] = 3 # Na chave 2, de valor 9, eu vou troca
num.append(7) # Crio uma nova chave, e adiciono o número 7 nela
num.sort(reverse=True)  # Defino em ordem crescente e inverto, ou seja, fica decrescente
num.insert(2, 0) #Insiro o valor 0 no índice 2 da lista
num.pop() #Excluo o último índice e seu respectivo valor da lista
num.pop(2) #Excluo o valor que tiver no indice 2 da lista
print (num) #Resultado da exibição: 7 5 3 2
print(f'Essa lista tem {len(num)} elementos')

#Podemos fazer validações também:
if 5 in num:
    num.remove(5)
else:
    print("Não achei o número 5")
"""
valores = []
# valores.append(5)
# valores.append(8)
# valores.append(2)

#Para exibir de forma formatada:
# for valor in valores:
#     print(f'{valor}', end="... " if valor != valores[len(valores) - 1] else "")
# for cont in range(0, 5):
#     valores.append(int(input("Digite um valor: ")))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print("Cheguei ao final da lista")

#Ao igualarmos uma lista, o python cria uma conexão entre elas, então por neste caso abaixo, invés da alterar, somente o índice 2 da lista B, o Python alterará tanto a lista A quanto a B, pq elas foram igualadas.
# a = [7, 8, 2, 6]
# b = a
# b[2] = 4
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
#Se eu quiser criar uma cópia de A em B realmente, sem ligá-las, eu precisamos fatiar a lista dessa forma. Dessa forma eu pego realmente apenas os valores, sem criar a ligação entre as listas
# b = a[:]
# b[2] = 4
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')

"""
LISTAS PT 2:

Podemos colocar listas dentro de listas:
dados = list()


dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(44)
dados.append('João')
dados.append(13)
dados.append('Julia')
dados.append(18)
print(dados[0]) = Pedro
print(dados[1]) = 25
print(dados[2]) = Maria
print(dados[3]) = 44
print(dados) = ['Pedro', 25, 'Maria',44 ,'João',13 ,'Julia', 18]

pessoas = list()
pessoas.append = (dados[:])
print(pessoas) = ['Pedro', 25, 'Maria',44 ,'João',13 ,'Julia', 18]
pessoas = [['Pedro',25], ['Maria',44], ['João',13], ['Julia',18]]
print(pessoas[0]) = ['Pedro', 25]
print(pessoas[-1]) = ['Julia', 18]
print(pessoas[2]) = ['João', 13]

print(pessoas[0][0]) =  Pedro - Pedindo para exibir o índice 0, da lista do índice 0 da lista de pessoas, ou seja o o nome 'Pedro'

print(pessoas[1][1]) = Maria - Pedindo para exibir o índice 1, da lista do índice 1 da lista de pessoas, ou seja o 'Maria'

print(pessoas[0][1]) = 25 - Pedindo para exibir o índice 1, da lista do índice 0 da lista de pessoas, ou seja o 25, a idade de Pedro

print(pessoas[2][0]) = João - Pedindo para exibir o índice 0, da lista do índice 2 da lista de pessoas, ou seja o nome 'João'

print(pessoas[3][1]) = 18 - Pedindo para exibir o índice 1, da lista do índice 3 da lista de pessoas, ou seja, 18, a idade de Julia
"""

# teste = list()
# teste.append("Gustavo")
# teste.append(40)
# galera = list()
# #galera.append(teste) ==== #Dessa forma, eu não estou criando uma cópia do que tem em teste e colocando na lista galera, eu estou criando uma ligação entre as duas lista, e se eu alterar uma, altero a outro também automaticamente. Para criar uma cópia, precisamos fazer da seguinte forma:
# galera.append(teste[:]) # Aqui eu fiz o fatiamento da forma correta, copiei o dado que estava em teste, e coloquei na lista de galera. Ao alterar qualquer coisa de teste, não afetará a lista "Galera"
# teste[0] = "Maria"
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
#
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[0]) #Exibir todos os dados de João
# print(galera[2][1]) #Exibir a idade de Joaquim
# print(galera[3][0]) #Exibir o nome de Maria
# print(galera[1]) #Exibir todos os dados de ana
#
# for pessoa in galera: #basicamente estou falando: "Para cada PESSOA em GALERA, exiba PESSOA", então para cada item da lista galera, ele irá exibir o item completo, então todas as informações da pessoa (Neste caso, nome e idade)
#     print(pessoa)
#
# for pessoa in galera:
#     print(pessoa[1]) #Diferente do exemplo anterior, aqui eu já especifíco o que eu vou querer de cada ítem, então, neste caso, estou pedindo que para cada pessoa de galera, me exiba o valor do índice 1 dela, no caso será a idade de todas as pessoas
#
# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade') #Podemos formatar também e exibir de forma mais bonita, organizada e clara

galera = list()
dado = list()
for contador in range(0, 5):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

#O programa acima criou duas lista, uma chamada 'galera', e outra chamada 'dado'. Ela vai ler o nome e idade de 1 pessoa, armazenar em 'dado', depois vai pegar esses valores de dado, e criar uma cópia em 'galera'. Depois disso, ele limpa o que foi digitado em dados, e vai repetir todo esse processo de novo. Fará 5 vezes isso, ou seja, 5 pessoas cadastradas com nome e idade