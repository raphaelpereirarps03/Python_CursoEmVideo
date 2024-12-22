nome = input("Qual é seu nome?")
print("Prazer em te conhecer {}!".format(nome))

# print("Prazer em te conhecer {:20}".format(nome)) : Exibe o nome com 20 espaços
# print("Prazer em te conhecer {:>20}".format(nome)) : Exibe o "nome" em 20 espaços alinhado à direita
# print("Prazer em te conhecer {:<20}".format(nome)) : Exibe o "nome" em 20 espaços alinhado à esquerda
# print("Prazer em te conhecer {:^20}".format(nome)) : Exibe o "nome" em 20 espaços alinhado ao centro
# print("Prazer em te conhecer {:=^20}".format(nome)) : Exibe o "nome" em 20 espaços, alinhado ao centro e invés de espaços em branco, para dar os 20 espaços, ele vai preencher com "=" (no lugar de "=", pode colocar qualquer caractere) #

n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com outro número:"))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1**n2;
divisao_inteira = n1 // n2;
modulo = n1 % n2
print("A soma é: {}; A subtração é: {}; A multiplicação é {}; A divisão é {:.2f};".format(soma, subtracao, multiplicacao, divisao))
# print("A soma é: {}; A subtração é: {}; A multiplicação é {}; A divisão é {:.2f};".format(soma, subtracao, multiplicacao, divisao), end = ' ') : Para não pular linha de um print para o outro, vai exibir esse print de cima, na mesma linha do print de baixo. #
print("A potencia é: {}; A divisão inteira é: {}; E o módulo é: {}.".format(potencia, divisao_inteira, modulo))

# print("A potencia é: {};\nA divisão inteira é: {}; \nE o módulo é: {}.".format (potencia, divisao_inteira, modulo)) :  Os \n servem para pular linha, então nesse caso vai exibir a potência, pular uma linha, exibir a divisão inteira, pular uma linha, e exibir o módulo.#



