# QUESTÃO 4 DESAFIO TARGET - EDILTON JR

# Definir um dicionário com os valores de faturamento de cada estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o valor total mensal da distribuidora
total = sum(faturamento.values())

# Calcular o percentual de representação de cada estado
percentuais = {estado: (valor / total * 100) for estado, valor in faturamento.items()}

# Imprimir o resultado
print('O valor percentual do faturamento de cada estado é:')

for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
