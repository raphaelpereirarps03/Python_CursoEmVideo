print("""Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirão, na ordem de colocação. Depois mostre: 
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição da tabela está o Vasco
""")

brasileirao = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama", "EC - Vitória", "Atlético MG", "Fluminense", "Grêmio", "Juventude", "Bragantino", "Athletico PR", "Criciúma", "Atlético GO", "Cuiabá")
posicao = brasileirao.index("Vasco da Gama") + 1
print(f"Os 5 primeiros colocados da tabela são: {brasileirao[0:5]}")
print(f"Os 4 últimos colocados da tabela são: {brasileirao[-4:]}")
print(f"A tabela em ordem alfabética é: {sorted(brasileirao)}")

print(f"Vasco da Gama está na {posicao}ª da tabela do brasileirão 2024")
