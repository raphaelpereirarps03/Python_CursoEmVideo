print("Reescreva a função leiaint(), que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.")


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (TypeError, ValueError):
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return valor

def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (TypeError, ValueError):
            print("\033[1;31mERRO! Digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return valor

 
#programa principal
valorInt = leiaInt("Digite um valor inteiro: ")
valorFloat = leiaFloat("Digite um valor real: ")
print(f"O valor inteiro digitado foi {valorInt} e o real {valorFloat}")
