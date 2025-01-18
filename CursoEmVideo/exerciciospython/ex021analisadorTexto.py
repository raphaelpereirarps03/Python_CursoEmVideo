print("""Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúsculas;
2 - O nome com todas as letras minúscilas;
3 - Qual é o primeiro nome e quantas letras tem ele.
""")
nomeCompleto = str(input("Entre com o seu nome completo: ")).strip()
nomeDividido = nomeCompleto.split()
print("Seu nome em maiúsculas é {};".format(nomeCompleto.upper()))
print("Seu nome em minúsculas é {};".format(nomeCompleto.lower()))
print("Seu nome tem ao todo {} caracteres (com espaços);".format(len(nomeCompleto)))
print("Seu nome tem ao todo {} letras;".format(len(nomeCompleto.replace(" ", ""))))
#Aqui eu pedi para substituir todos os espaços em brancos (" "), por (""), ou seja tirei os espaços e juntei a string do nome completo e pedi o tamanho disso
print("Seu nome tem ao todo {} letras;".format(len(nomeCompleto) - nomeCompleto.count(" ")))
#Já aqui eu pedi para contar todos os espaços em branco (" "), e subtrair esse número do tamanho da string nome completo
print("Seu primeiro nome é {} e ele tem {} letras".format(nomeDividido[0], len(nomeDividido[0])))
