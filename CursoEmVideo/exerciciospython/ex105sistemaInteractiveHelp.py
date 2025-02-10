from time import sleep
print("Faça um mini programa que utilize o Interactive Help do Python. O usuário vai digitar o comando/função que ele quer consultar o manual e o manual vai aparecer. Quando o usuário digitar 'FIM' o programa encerrará. Obs: Utilize cores")


def interactiveHelpConsult(comando):
    titulo = f"Acessando o manual do comando '{comando}' "
    tamanho = len(titulo) + 4
    print("\033[1;44m~" * (tamanho))
    print(f"{titulo:^{tamanho}}")
    print("~" * (tamanho))
    sleep(1)
    print("\033[7;40m")
    print(help(comando))
    print("\033[m", end="")

#programa principal
titulo = "SISTEMA DE AJUDA PyHELP"
tamanho = len(titulo) + 4
while True:
    print("\033[1;43m~" * (tamanho))
    print(f"{titulo:^{tamanho}}")
    print("~" * (tamanho))
    print("\033[m",end="")

    comando = str(input("Comando ou biblioteca > ")).lower()
    if comando == "fim":
        titulo = "ATÉ LOGO!"
        tamanho = len(titulo) + 4
        print("\033[1;41m~" * (tamanho))
        print(f"{titulo:^{tamanho}}")
        print("~" * (tamanho))
        break
    else:
        interactiveHelpConsult(comando)

