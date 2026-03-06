import pandas as pd

print("=== RELATÓRIO EXECUTIVO DE VAGAS ===\n")

# PUXANDO O DF (CARREGANDO OS DADOS)
# Lemos o arquivo limpo e guardamos na variável 'df'
df = pd.read_csv('../data/processed/vagas_limpas.csv', sep=';')


print(". DISTRIBUIÇÃO DE VAGAS POR SENIORIDADE:")

# O df['Nivel'] seleciona apenas a coluna dos níveis.
# O .value_counts() agrupa os nomes iguais e conta a quantidade de cada um.
contagem_niveis = df['Nivel'].value_counts()

print(contagem_niveis)
print("-" * 40) # Imprime uma linha tracejada para separar visualmente


print("\n TOP 5 EMPRESAS COM MAIS VAGAS ABERTAS:")

# df['Empresa'] seleciona a coluna das empresas.
# value_counts() conta quantas vagas cada empresa tem, ordenando da maior para a menor.
# head(5) "corta" a lista e mostra apenas os 5 primeiros resultados.
top_empresas = df['Empresa'].value_counts().head(5)

print(top_empresas)
print("-" * 40)