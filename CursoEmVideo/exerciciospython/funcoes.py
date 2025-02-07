"""
Funções são "blocos de códigos", que são executados quando chamados. Usados quando temos uma rotina e rotina de código, nada mais é do que quando temos uma estrtura de códigos que se repete constantemente, então, invés de eu digitar ela sempre, eu crio a função dela apenas uma vez e basta eu chama-la sempre que precisar.

Para definirmos uma função usamos:
def nomeFuncao():
    codigo que serão executados pela função quando chamarmos
    ~~~~~
    ~~~~
    ~~~~


Uma boa prática das funções é sempre deixar duas linhas de distância entre ela e algum outro código, seja a aplicação principal, seu programa ou até mesmo outras funções. Exemplo

def funcao1():
    ~~~~
    ~~~~


def funcao2():
    ~~~~
    ~~~~


#programa principal
~~~~
~~~~
funcao1() #chamada de função
funcao2() #chamada de função

--------------------------------------------
Funções podem receber parâmetros. Parâmetros são "componentes" que são passados para as funções funcionarem. Como regras definidas para a função ser usada de forma correta ou o que se espera. Exemplo:

--------------------------------------------
# funcao soma definida que precisa receber 2 valores, 'a' e 'b'. Ao receber esses valores, vamos pegar eles, soma-los entre si e atribuir o resultado à variável 'resultado', e a conclusão (return) dessa função será a variável resultado
def soma(a, b):
    resultado = a + b
    return resultado


# Programa principal
valor1 = int(input("Entre com um valor A: ") # variável 'valor1' recebe um número inteiro via teclado
valor2 = int(input("Entre com um valor B: ") # variável 'valor2' recebe um valor inteiro via teclado
print(soma(valor1, valor2) # Chamamos a função 'soma()' e exibimos no terminal sua conclusão

# Ou seja, o usuário entrará com dois valores, chamamos a função e falamos: "olha, o valor a e b que vc precisa, serão os valores 1 e 2 que eu recebi aqui". Aí a função vai falar: "Ok, vou somar os dois e te retornar o resultado"
--------------------------------------------

Uma função pode ter N parâmetros, se esse for o caso definimos a função assim:
def funcao(*num):
    ~~~~
    ~~~~
    ~~~~


#programa principal
~~~~
~~~~
funcao(n, n, n, n, ... n) # Passei N parãmetros de N valores para a função, ao fazer isso, eu empacotei os valores/parâmetros e joguei lá na função. Quando chegar lá, ela vai desempacotar e fazer o que estiver definido para fazer. Você basicamente falou: "Olha, to mandando um pacote com vários valores aí mas eu não sei quantos são, quando chegar, desempacota e trabalha com eles"

------------------------------------------------
O Interactive Help em Python é um sistema de ajuda embutido que permite obter informações sobre funções, classes, módulos e outros elementos do código. Ele é útil para entender rapidamente como algo funciona sem precisar consultar a documentação externa.

Para utilizar ela no ambiente de desenvolvimento (pycharm, vscode e etc):
<>
help(print) # Isso exibe uma descrição da função print, seus parâmetros e exemplos de uso.
<>

No console interativo do Python basta digitar help() e pressionar Enter para abrir um modo interativo onde você pode pesquisar sobre qualquer comando digitando seu nome.
<>
">>> help()
help> print  # Digite 'print' e pressione Enter
<>

Para sair do modo interativo, basta digitar q ou quit e pressionar Enter.

-------------------------------------------------

Uma docstring é um comentário especial usado para documentar funções, classes e módulos em Python. Ela é escrita entre três aspas duplas (""" """) (ou simples) logo na primeira linha do corpo da função. Sua principal função é explicar o que a função faz, tornando o código mais legível. Exemplo:

def soma(a, b):
    ''""Retorna a soma de dois números.""''
    return a + b

Como acessar a docstring:
Você pode visualizar a documentação da função usando:
help(soma)
print(soma.__doc__)  # Outra forma de exibir a docstring

-------------------------------------------------

Imagine o seguinte cenário: 
Uma função que obrigatoriamente recebe 3 parâmetros: a, b, c. Para que ela funcione precisamos enviar os 3 valores para ela

def soma(a, b, c)
    resultado = a + b + c
    print(f"{resultado}")
    
soma(2, 5, 3) # Passado os 3 valores, a função funcionará normalmente.

Agora, imagina se eu passo:
soma (6, 2) # Apenas dois valores, o 3º ficará faltando e dará erro no meu programa. Para resolver isso, podemos definir parâmetros opcionais da seguinte maneira:

def soma(a, b, c = 0)
    resultado = a + b + c
    print(f"{resultado}")
    
    
soma (6, 2) 
#Eu basicamente falo para o meu programa: "Olha, pra essa função funcionar, ela PRECISA receber A e B e C, porém, A e B PRECISAM SER PASSADOS COM VALORES, JÁ O C, ELE PODE SER PASSADO TAMBÉM, MAS SE NÃO CHEGAR, NÃO TEM PROBLEMA, COLOCA UM 0 NO LUGAR DELE. Neste caso, A e B vão receber 6 e 2 respectivamente, e o C vai receber 0

****** E NADA IMPEDE DE EU FAZER ISSO PARA TODOS OS PARÂMETROS: ******"
def soma(a = , b = 0, c = 0)
    resultado = a + b + c
    print(f"{resultado}")
    
soma (6) 
# "PRECISO DE A, B E C, PORÉM SE NÃO CHEGAR NADA, PODE TROCAR TUDO POR 0, NÃO TEM PROBLEMA. Neste caso, A vai receber 6 e o restante 0"

soma()
# Neste caso todos receberão 0 e fé
"""