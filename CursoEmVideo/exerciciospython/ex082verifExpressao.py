print("Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu progra,a deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta")

expressao= str(input("Digite uma expressão: "))
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append("(")
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print('Sua expressão está errada!')
