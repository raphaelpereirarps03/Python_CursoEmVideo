print("Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, porém, fará a validação para aceitar apenas um valor numérico.")


def leiaInt(msg):
    """
    Função para verificar se é um número inteiro válido
    :param msg: mensagem que será exibida no input
    :return: Se o valor digitado for um inteiro de fato retorna o mesmo
    """
    while True:
        valor = (input(msg)).strip()
        if valor.isalpha() or valor == '':
            print("\033[31mERRO! Digite um número inteiro válido\033[m")
        else:
            return int(valor)
            break


#programa principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
