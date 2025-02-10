def aumentar(v=0, porcent=0):
    result = v + ((v * porcent) / 100)
    return result

def diminuir(v=0, porcent=0):
    result = v - ((v * porcent) / 100)
    return result

def dobro(v=0):
    result = v * 2
    return result

def metade(v=0):
    result = v / 2
    return result

def moeda(v=0, moeda='R$'):
    valorFormatado = str(f"{moeda}{v:.2f}".replace('.', ','))
    return valorFormatado
