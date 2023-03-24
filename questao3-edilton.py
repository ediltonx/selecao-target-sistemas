# QUESTÃO 3 DESAFIO TARGET - EDILTON JR

import json

# Abrindo o arquivo dados.json
with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamento_diario = [dado['valor'] for dado in dados]

# Encontrar o menor e o maior valor de faturamento
min_faturamento = min(faturamento_diario)
max_faturamento = max(faturamento_diario)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Encontrar o número de dias em que o faturamento foi superior à média mensal
dias_acima_media = sum(1 for f in faturamento_diario if f > media_mensal)

# Imprimir os resultados
print('Menor valor de faturamento:', min_faturamento)
print('Maior valor de faturamento:', max_faturamento)
print('Valor da média mensal:', media_mensal)
print('Número de dias com faturamento acima da média:', dias_acima_media)
