from ex113menu.lib.interface import *
from ex113menu.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

from time import sleep
while True:
    resp = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #Opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resp == 3:
        #Opção de sair do programa
        cabecalho("PROGRAMA ENCERRADO! ATÉ A PRÓXIMA")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)