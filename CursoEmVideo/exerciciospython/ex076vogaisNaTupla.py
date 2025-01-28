print("Crie um programa que tenha uma tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais")
palavras = ('aprender', 'programar', 'linguagem', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')