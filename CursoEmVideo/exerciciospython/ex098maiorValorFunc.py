from time import sleep
print("Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.")
def maior(*num):
    print("-=" * 30)
    if len(num) != 0:
        for k, v in enumerate(num):
            if k == 0 or v > maiorValor:
                maiorValor = v
            sleep(0.5)
            print(f"{v} ",end="")
        print(f"Foram informados {len(num)} valores ao todo.")
        print(f"O maior valor informado foi {maiorValor}.")
    else:
        print("Nenhum parâmetro foi passado para a função!")


print("Analisando os valores passados...")
maior(7, 9, 8, 3, 4, 1)
maior(5, 1, 2)
maior(0, 8)
maior(1, 6, 7, 2)
maior(1)
maior(4, 5, 1, 8, 7)
maior()
