import pandas as pd 
import sqlite3

print("=====LOAD======")
df = pd.read_csv('../data/processed/vagas_limpas.csv', sep=';')
print("Dados limpos carregados")

caminho_banco = '../data/processed/banco_de_vagas.db'
conexao = sqlite3.connect(caminho_banco)

#Injetar o DataFrame para dentro do banco
#name='vagas' -> O nome da tabela dentro do banco
#con=conexao -> Diz ao Pandas para onde mandar os dados
#if_exists='replace' -> Se a tabela já existir, ele apaga a antiga e põe a nova
#index=False -> Para não salvar a coluna inútil de contagem (0, 1, 2...) do Pandas
df.to_sql(name='vagas', con=conexao, if_exists='replace', index=False)

print(" As vagas foram inseridas na tabela 'vagas'.")
print(f"📁 Banco de Dados criado em: {caminho_banco}")