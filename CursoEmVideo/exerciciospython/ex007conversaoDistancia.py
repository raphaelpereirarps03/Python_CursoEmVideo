print("Crie um programa que leia um valor em metros e converta-o em kilômetros, hectômetros, decâmetros, decímetro centímetros e milímetros")
metro = float(input("Entre com um valor de distância em metros (m): "))
kilometro = metro / 1000
hectometro = metro / 100
decametro = metro / 10
decímetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000
print("Valor em kilometro: {}km; \nValor em hectômetro: {}hm; \nValor em decâmetro: {}dam; \nValor em metros : {}m;\nValor em decímetro: {}dm; \nValor em centímetros: {:.0f}cm;\nValor em milímetros: {:.0f}mm.".format(kilometro, hectometro, decametro, metro, decímetro, centimetro, milimetro))
