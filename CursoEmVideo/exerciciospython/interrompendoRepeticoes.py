cont = 1
s = n = 0

while cont<= 10:
    print(cont, '-> ', end='')
    cont += 1
print("Acabou")
#Da forma acima, o programa será executado ENQUANTO o 'cont', for menor ou igual a 10, então o resultado que será exibido é: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

#Mas para casos em que eu não sei quando vai terminar, podemos usar loops infinitos com condições de parada usando o break:

salario = 2440.7788655
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
# print("Soma: ", s)
# print("Soma: {}".format(s))
print(f"Soma: {s}") # Usando F strings, substitui o .format na exibição e usa uma espécie de interpolação, igual do JS
print (f"Salario: R${salario:.2f}")