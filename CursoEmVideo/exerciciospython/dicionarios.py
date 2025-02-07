"""
Semelhantes as listas, são variáveis compostas, estrutura composta. Porém, diferentemente das listas, que seus índices/chaves são números inteiros de 0 à N, os dicionários trabalham com chaves literais ou ************

Podemos declarar dicionários da seguinte maneira:
dicionario = {}
OU
dicionario = dict()

então podemos ter um dicionário assim:

dados = {'nome':"Júlio", 'idade': 20}

ou seja, invés do índice 0, ser reconhecido pelo seu numeral, ele é reconhecido pela sua nomenclatura definida, que neste caso seria o 'nome'. Então se eu der:

print(dados['nome'])

E na tela será exibido "Júlio"

Podemos também criar índices e já adicioná-los no dicionário:

dados['sexo'] = 'M'

O estrutura do dicionário é alterada automáticamente e ficará assim:

dados = {'nome':"Júlio", 'idade': 20, 'sexo':"M"}

se dermos:

del dados['idade']

a estrura se reinventa novamente e fica:

dados = {'nome':"Júlio", 'sexo':"M"}

Vamos falar agora sobre a diferenças entre chaves, valores e itens, ou values, keys e items, respectivamente:
filme = {
    'titulo':'Star Wars',
    'ano': 1977,
    'diretor': 'George Luccas'
}

print(filme.values()) # Exibirá os somente os valores dos índices, ou seja: 'Star Wars', 1977, 'George Luccas', da seguinte forma:
dict_values(['Star Wars', 1977, 'George Luccas'])

print(filme.keys()) #  Exibirá somente as chaves da estrutura: 'titulo', 'ano', 'diretor', da seguinte forma:
dict_keys(['titulo', 'ano', 'diretor'])

print(filme.items()) # Exibirá o conjunto, chave e valor, então: 'titulo', da seguinte forma:
dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Luccas')])

"Items" podem ser usados bastante em laços para o seu controle, de forma semelhante ao "enumerate". Exemplo:
for key, value in filme.items():
    print (f"O {key} é {value}")

RESULTADO:
O titulo é Star Wars
O ano é 1977
O diretor é George Luccas

As estruturas podem ser integradas umas nas outras
listas podem conter listas, tuplas e dicionarios
dicionários podem conter dicionários, listas e tuplas
tuplas podem conter tuplas, listas e dicionarios

EXEMPLO PRÁTICO:
locadora = [
    {'titulo':"Star Wars", 'ano':"1977", 'diretor':"George Luccas"},
    {'titulo':"Vingadores", 'ano':"2012", 'diretor':"Joss Whedon"},
    {'titulo':"Matrix", 'ano':"1999", 'diretor':"Wachowski"}
]
LOCADORA = LISTA
Dentro da lista locadora existem dicionários de filmes

print(locadora[0]['ano']) # 1977
print(locadora[2]['titulo']) # Matrix
print(locadora[1]['diretor']) # Joss Whedon
"""

# pessoa = {'nome':'Raphael', 'idade': 21, 'sexo':'M'}
# # print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos e é do sexo {pessoa["sexo"]}') # A referência às chaves precisam ser entre aspas duplas ("")
#
# #Usando laços para exibir:
# for keys in pessoa.keys():
#     print(keys)
# """
# Resultado:
# nome
# idade
# sexo
# """
# for values in pessoa.values():
#     print(values)
# """
# Resultado:
# Raphael
# 21
# M
# """
#
# for keys, values in pessoa.items():
#     print(f"{keys} = {values}")
# """
# Resultado:
# nome = Raphael
# idade = 21
# sexo = M
# """
#

estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy()) #Esse ".copy", substitui o fatiamento em LISTAS, pois em DICIONÁRIOS, não existe fatiamento
for e in brasil:
    print(e)