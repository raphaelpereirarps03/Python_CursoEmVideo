import datetime

print("Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade), em um dicionário. Se por acaso o CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcile e acrescente, além da idade, com quantos anos a pessoa vai se aposentar")

trabalhador = {}
trabalhador['nome'] = str(input("Nome trabalhador: "))
anoNasc = int(input("Data de Nascimento: "))
trabalhador['idade'] = datetime.date.today().year - anoNasc
trabalhador['ctps'] = int(input("Carteira de Trabalho (CTPS) (0 não tem): "))
if trabalhador['ctps'] == 0:
    print('-=' * 30)
    for k, v in trabalhador.items():
        print(f'{k} é {v}')
    print('Não possui CTPS!')
elif trabalhador['ctps'] < 0:
    print("Número de CTPS negativo. INVÁLIDO. Programa encerrado!")
else:
    trabalhador['anoContratacao'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = float(input("Salário: "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['anoContratacao'] + 35) - datetime.date.today().year)
    print('-=' * 30)
    for k, v in trabalhador.items():
        print(f'{k} é {v}')