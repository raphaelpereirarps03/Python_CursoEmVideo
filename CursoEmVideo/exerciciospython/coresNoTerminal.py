"""Para colorir o terminal, num primeiro momentos, vamos utilizar o código ANSI.
Para isso, a base é:

\033[style;text;backgrounm

O primeiro parâmentro ali, "style", é o comportamento do texto, ou seja, o estilo da fonte, se é negrito, itálico e etc.
O segundo parâmentro, "text" diz respeito à cor de texto
O terceito parâmetro "background", é sobre a cor de fundo

Exemplo real:

\033[0;33;44m

TODOS ELES SÃO OPCIONAIS E A ORDEM NÃO IMPORTA

CÓDIGOS PARA STYLE (existem outros, mas os que funcionam melhor em Python são esses):
1 - 0: none
2 - 1: negrito
3 - 4: sublinhado
4 - 7: negative

CÓDIGOS PARA TEXT (existem outros, mas os que funcionam melhor em Python são esses):
1 - 30: Branco
2 - 31: Vermelho
3 - 32: Verde
4 - 33: Amarelo
5 - 34: Azul
6 - 35: Magenta
7 - 36: Azul-claro
8 - 37: Cinza

CÓDIGOS PARA BACKGROUND (existem outros, mas os que funcionam melhor em Python são esses):
1 - 40: Branco
2 - 41: Vermelho
3 - 42: Verde
4 - 43: Amarelo
5 - 44: Azul
6 - 45: Magenta
7 - 46: Azul-claro
8 - 47: Cinza
"""
print("\033[1;32;41mTestando com o fundo ocupando toda a linha")
print("\033[1;31;46mPara não pegar toda a linha \033[m")
