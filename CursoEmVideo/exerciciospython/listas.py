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
a = [7, 8, 2, 6]
# b = a
# b[2] = 4
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
#Se eu quiser criar uma cópia de A em B realmente, sem ligá-las, eu precisamos fatiar a lista dessa forma. Dessa forma eu pego realmente apenas os valores, sem criar a ligação entre as listas
b = a[:]
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')