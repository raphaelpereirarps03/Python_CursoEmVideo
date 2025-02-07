def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print("~" * tamanho)
    print(f"{mensagem:^{tamanho}}")
    print("~" * tamanho)


texto = str(input("Entre com a sua mensagem: "))
escreva(texto)