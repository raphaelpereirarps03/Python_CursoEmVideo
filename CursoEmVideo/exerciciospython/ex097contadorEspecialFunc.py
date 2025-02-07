from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if fim > inicio:
        for i in range(inicio, (fim + 1), passo):
            sleep(0.5)
            print(f"{i} ", end="")
    elif inicio > fim:
        if passo > 0:
            passo = passo - (passo * 2)
            for i in range(inicio, (fim - 1), passo):
                sleep(0.5)
                print(f"{i} ", end="")
        else:
            for i in range(inicio, (fim - 1), passo):
                sleep(0.5)
                print(f"{i} ", end="")
    print("FIM!")


print('-=' * 20)
contador(1, 10, 1)
print('-=' * 20)
contador(10, 0, -2)
print('-=' * 20)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
