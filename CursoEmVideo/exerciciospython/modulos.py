"""
Para fazer a importação de uma biblioteca utilizamos a seguinte estrutura:

 1 - import nomeDaBiblioteca;

Dessa forma todos as funções dessa biblioteca virão e poderão ser usadas, porém, o programa ficará pesado e muitas vezes nem utilizaremos todas elas. Então, para otimizar isso, utilizamos:

2 - from nomeDaBiblioteca import nomeDaFuncao;

Com isso, temos a forma mais generalista de se importar as funcionalidades dos módulos (1) e a maneira mais específica (2);

EXEMPLO REAL:
A biblioteca math, é uma biblioteca que já vem INSTALADA (diferente de importada) no Python. Se eu quiser IMPORTAR biblioteca math para o meu programa, e fizer da seguinte forma:

1 - import math;

Eu importarei também, as funções "ceil", "floor", "trunc", "pow", "sqrt", "factorial", entre muitas outras. Todas elas ficarão disponíveis para uso. Porém, se o seu programa, só utiliza, por exemplo, a função "sqrt", as outras estarão apenas estorvando o meu programa, fazendo peso, pois não estarão sendo utilizadas, e em consequência, deixarei o programa pesado, lento e etc.
Para corrigir isso, eu posso importar assim:

2 - from math import sqrt;

Pronto, importei apenas a função "sqrt", da biblioteca "math". Deixei meu programa mais leve e mais rápido. Não poderei utilizar as outras, funções, porém deixei o programa mais otimizado. E nada impede de eu ter mais de 1 importação:

3 - from math import sqrt
    from math import pow
    from math import ceil

Dessa forma, eu importei 3 funções do pacote math e poderei utilizar todas elas. O exemplo acima é IGUAL à:

4 - from math import sqrt, pow, ceil (economizei linhas)


OBS:
1 - ceil - função para arredondar um número para cima
2 - floor - função para arredondar um número para baixo
3 - trunc - função para retirar todos os números depois da casa decimal, então 6.154, se torna só 6, joga o .154 fora
4 - pow - para calcular uma potência
5 - sqrt - para calcular uma raíz quadrada
6 - factorial - para calcular o fatorial de um número

"""

# neste caso poderia importar apenas as funções utilizadas, e elas seriam todas na mesma linha assim:
# from math import ceil, floor, sqrt
# quando eu faço assim, eu não preciso da referência "math." antes das funções em uso
import math
import random
print("Exercício Testes de Módulos Math:")
#Exibir sem formatação
print("Exemplo 1:")
num = int(input("Entre com um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {} \n".format(num, raiz))
#Exibir com a raiz arredondada para cima
print("Exemplo 2:")
num = int(input("Entre com um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {} \n".format(num, math.floor(raiz)))
#Exibir com a raiz arredondada para baixo
print("Exemplo 3:")
num = int(input("Entre com um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {} \n".format(num, math.ceil(raiz)))
#Exibir com a raiz duas casas decimais
print("Exemplo 4:")
num = int(input("Entre com um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f} \n".format(num, raiz))

#python.org - para ter acesso a documentação do python e logo todas bibliotecas padrões e como utilizar elas

#Gerando um número aleatório com uma variável
print("Exemplo 5:")
num = random.random()
print(num)

#Gerando um número aleatório sem variável
print("Exemplo 6:")
print(random.random())

#Gerando um número aleatório inteiro e dentro de um intervalo
print("Exemplo 7:")
num = random.randint(1, 10);
print(num)

#A função random.random() gera números aleatórios entra 0 e 1 e a randint só funciona com um intervalo pré estabelecido

