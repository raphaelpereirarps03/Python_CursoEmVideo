def aumentar(v=0, porcent=0, formatado=False):
    """
    Função para aumentar um valor baseado em porcentagem
    :param v: valor
    :param porcent: porcentagem que será aplicada no valor para aumentá-lo
    :param formatado: se será exibido de forma formatada como valor monetário de fato ou não
    :return: resultado sem formatação monetária se formatado == false, se não, resultado com formato monetário
    """
    result = v + ((v * porcent) / 100)
    return result if formatado is False else moeda(result)

def diminuir(v=0, porcent=0, formatado=False):
    """
    Função para diminuir um valor baseado em porcentagem
    :param v: valor
    :param porcent: porcentagem que será aplicada no valor para diminuí-lo
    :param formatado: se será exibido de forma formatada como valor monetário de fato ou não
    :return: resultado sem formatação monetária se formatado == false, se não, resultado com formato monetário
    """
    result = v - ((v * porcent) / 100)
    return result if not formatado else moeda(result)

def dobro(v=0, formatado=False):
    """
    Função para dobrar um valor
    :param v: valor
    :param formatado:  se será exibido de forma formatada como valor monetário de fato ou não
    :return: resultado sem formatação monetária se formatado == false, se não, resultado com formato monetário
    """
    result = v * 2
    return result if formatado is False else moeda(result)

def metade(v=0, formatado=False):
    """
    Função para calcular a metade de um valor
    :param v: valor
    :param formatado: se será exibido de forma formatada como valor monetário de fato ou não
    :return: resultado sem formatação monetária se formatado == false, se não, resultado com formato monetário
    """
    result = v / 2
    return result if not formatado else moeda(result)

def moeda(v=0, moeda='R$'):
    """
    Formata um valor para que fique de forma monetária
    :param v: valor
    :param moeda: a moeda (R$, U$, EUR...)
    :return: valor formatado de forma monetária
    """
    valorFormatado = str(f"{moeda}{v:.2f}".replace('.', ','))
    return valorFormatado
