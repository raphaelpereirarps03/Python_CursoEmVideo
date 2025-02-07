print("Crie um programa que tnha uma função chamada 'voto()', que vai receber como parâmetro o ano de nascimento de uma pessoa e retornará um valor literal indicando se uma pessoa tem o voto NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições")
import datetime


def voto(anoNasc=datetime.date.today().year):
    """
    Função para definir a situação eleitoral de uma pessoa
    :param anoNasc: ano de nascimento, para calcular sua idade
    :return: idade e situação eleitoral
    """
    idade = datetime.date.today().year - anoNasc
    if  idade > 18 and idade < 65:
        situacao = "OBRIGATÓRIO"
    elif idade < 16:
        situacao = "NEGADO"
    else:
        situacao = "OPCIONAL"

    return (f"Com {idade} anos: VOTO {situacao}")


#programa principal
print("-=" * 30)
ano = input("Em que ano você nasceu? (ENTER para ano atual)")
if ano:
    voto(int(ano))
else:
    voto()
