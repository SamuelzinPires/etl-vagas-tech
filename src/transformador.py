import pandas as pd    

print("--- INICIANDO A TRATAMENTO DE DADOS ---\n")

#ler os dados brutos (Buscando o arquivo na pasta raw)
df = pd.read_csv('../data/raw/vagas_gupy.csv', sep=';')
print("Dados originais carregados com sucesso!")

#Tratamento sobre os niveis das vagas
def descobrir_nivel(titulo):
    # O str() protege o código caso o título venha vazio
    titulo_limpo = str(titulo).lower()

    #palavra chave
    if 'junior' in titulo_limpo or 'jr' in titulo_limpo:
        return 'Júnior'
    elif 'pleno' in titulo_limpo or 'pl' in titulo_limpo:
        return 'Pleno'
    elif 'senior' in titulo_limpo or 'sênior' in titulo_limpo or 'sr' in titulo_limpo:
        return 'Sênior'
    else:
        return 'Não Informado'

#(Substituindo os valores da coluna 'Formato')
df['Formato'] = df['Formato'].replace('on-site', 'Presencial')
df['Formato'] = df['Formato'].replace('remote', 'Remoto')
df['Formato'] = df['Formato'].replace('hybrid', 'Híbrido')
print("Tradução dos formatos aplicada!")

#Descobrindo a Senioridade 
df['Nivel'] = df['Titulo'].apply(descobrir_nivel)
print("Senioridade extraída dos títulos!")

df.to_csv('../data/processed/vagas_limpas.csv', index=False, sep=';', encoding='utf-8')

print("\n Arquivo 'vagas_limpas.csv' salvo na pasta data/processed/")