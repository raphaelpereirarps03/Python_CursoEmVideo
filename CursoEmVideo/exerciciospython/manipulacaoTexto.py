#Métodos de manipulação, edição e tratamento de textos (strings)

#Fatiando uma string:

frase = "Curso em Vídeo Python"
#EX1:
print(frase[3])
#Vamos lembrar que um texto, uma string, nada mais é do que uma cadeia de caracteres (fazer a analogia do char). Ou seja, uma String, é uma lista que contém chars. Do ponto de vista do cumputador é assim que ele enxerga. Como é uma lista, ele trabalha com posições, indices, então cada caractere ocupa um indice. No exemplo acima, eu pedi para exibir o VALOR do ÍNDICE 3, ou seja, o "S" (Assim como uma lista comum, o índice começa do 0).

#EX2:
print(frase[3:13])
#Aqui, eu peço para exibir todos os valores dos índices de 3 à 13, ou seja um range, um intervalo de índices
#resultado obtido: "so em Víde"
#OBS: O Python SEMPRE ignora o último caractere do intervalo, neste exemplo, o "O", de "Vídeo", é o 13 valor, mas ele não é exibido justamente é o último valor do intervalo, então podemos dizer que exibe de 3 à 13, excluindo o 13, basicamente

#EX3:
print(frase[:13])
#Aqui, eu peço para exibir todos os valores dos índices de 0 até o 13. Quando oculto o início do intervalo, o Python entende que será do índice 0
#Resultado obtido: "Curso em Víde"

#EX4:
print(frase[3:])
#Aqui, eu peço para exibir todos os valores dos índices de 3 até o fim da string. Quando oculto o fim do intervalo, o Python entende que será do índice 3 até o fim da string
#Resultado obtido: "so em Vídeo Python"

#EX5:
print(frase[1:18:3])
#Aqui, eu peço para exibir todos os valores dos índices de 5 à 15, ou seja um range, um intervalo de índices, pulando de 3 em 3 os índices
#resultado obtido: "uomíoy"

#Podemos combinar tudo o que vimos até agora da seguinte forma:
print(frase[1::3]) # Vai exibir do índice 1 até o fim da string pulando de 3 em 3
print(frase[:18:3]) # Vai exibir do índice 0 até o índice 18 da string pulando de 3 em 3
print(frase[::2]) #Vai exibir do índice 0 até o fim da string pulando de 2 em 2

#Para trabalharmos com uma string com quebra de linha, podemos exibir ela da seguinte maneira:
print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaa""")

#Para contar quantas vezes aparece determinado caractere, ou cadeia de caracteres, podemos fazer:
print(frase.count('o')) #Aqui, estamos contando quantos "o"'s aparecem na string frase. Vale lembrar que ele diferencia "o" de "O", ou seja, se é minúsculo ou maiúsculo.

#Podemos combinar métodos
print(frase.upper().count("O")) #Aqui eu joguei a frase para maiúsculo e pedi para ver quantos "o"'s maiusculos existem

print(frase.upper()) #Joguei a string para maiusculo
print(frase.lower()) #Joguei a string para minúsculo

#Para verificar o tamanho da frase:
print(len(frase)) #Resultado: 21

#Espaços em branco contam na contagem, então:
frase1 = "     Curso em Vídeo Python             " #Resultado: 39
print(len(frase1))
#OBS: Tira os espaços em branco inúteis, ou seja, aqueles epsaços em branco do começo ou do final da string, os espaços entre as palavras, ele continua considerando pois ele entende que está ali separando "itens"

#Para ignorar os espaços em branco, podemos utilizar:
print(len(frase1.strip())) #Resultado: 21 - Nota-se que tirou todos os espaços em branco da contagem, voltando para o resultado 21 caracteres

#Para eu trocar uma cadeia de caracteres, por outra:
frase1 = "Curso em Vídeo Python"
print(frase.replace("Python", "Android"))
print(frase1)
#Vale lembrar que, neste caso, eu não estou mudando a estrutura do objeto frase, ou seja, seu valor continua sendo "Curso em Vídeo Python", em sua essencia, o que eu fiz em cima, foi invés de exibir "Python", exibirá "Android". Coloquei como se fosse uma máscara na palavra. Agora, se eu quiser trocar a estrutura, eu preciso fazer uma atribuição, ou seja, assim:
frase1 = frase.replace("Python", "PHP")
print(frase1)

#Para verificar se alguma coisa está dentro da string, podemos utilizar:
print("Curso" in frase1)
#Basicamente pergunto: "Curso" está em frase1? Resposta: True

#Já para pedir para buscar e informar a localização de alguma coisa, utilizamos o:
print (frase1.find("Curso"))
#O resultado aqui é 0, por que eu estou pedindo: "Encontre "Curso", em frase1!", o retorno disso, é onde se inicia , ou seja, no índice 0, por causa do "C"

#Provando mais uma vez que Python diferencia minúsculos de maiúsculos:
print (frase1.find("curso"))
#Aqui eu estou pedindo: "Encontre "curso", em frase1!", como eu estou pedindo "curso" e não "Curso", o retorno é -1 porque ele não encontra

#Já para transformar a frase1 em uma lista de palavras (irá identificar onde tem " ", e vai separá-las), eu faço:
dividido = frase1.split()
print(dividido)

#Quando eu faço isso, eu posso trabalhar como se esse objeto fosse uma matriz, pq eu posso exibir valor específico dentro do indíce de "dividido":
print(dividido[2])
#Aqui eu exibo o 2 valor de dividido

#E posso também exibir um valor específico dentro de um específico:
print(dividido[2][3])
#Aqui eu exibo o 3º valor do 2º valor de dividido


