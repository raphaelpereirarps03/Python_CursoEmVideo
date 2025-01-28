print("Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.")
while True:
    c = 1
    numero = int(input("Entre com um valor:\n\033[1:31mSe quiser parar o programa, digite qualquer número negativo (<0)\033[m\n"))
    if numero < 0:
        break
    print("-" * 30)
    while c < 11:
        print(f"{numero} x {c} = {numero * c}")
        c += 1
    print("-" * 30)