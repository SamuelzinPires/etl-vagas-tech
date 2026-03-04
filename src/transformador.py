import pandas as pd    

#ler os dados brutos (Buscando o arquivo na pasta raw)
df = pd.read_csv('../data/raw/vagas_gupy.csv', sep=';')
print("Dados originais carregados com sucesso!")

#(Substituindo os valores da coluna 'Formato')
df['Formato'] = df['Formato'].replace('on-site', 'Presencial')
df['Formato'] = df['Formato'].replace('remote', 'Remoto')
df['Formato'] = df['Formato'].replace('hybrid', 'Híbrido')

print("Tradução dos formatos aplicada!")
df.to_csv('../data/processed/vagas_limpas.csv', index=False, sep=';', encoding='utf-8')

print("\n Arquivo 'vagas_limpas.csv' salvo na pasta data/processed/")