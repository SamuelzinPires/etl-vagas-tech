import requests
import pandas as pd

# string abaixo, sua identidade diz: "Sou um humano usando Google Chrome no Windows".
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
#endereço do request, api 
api_url = "https://employability-portal.gupy.io/api/v1/jobs?jobName=dados&limit=10&offset=0"

#THE REQUEST
response = requests.get(api_url, headers=headers)

#Verificando se deu certo
if response.status_code == 200:
    print("Conexão com a API estabelecida com sucesso!\n")
    #transforma em JSON
    dados_json = response.json()
    #cria a lista
    lista_de_vagas = dados_json['data']
    print("\n--- VAGAS EXTRAÍDAS COM SUCESSO ---\n")
    
    vagas_extraidas = []
    #Loop de Extração
    for vaga in lista_de_vagas:
        
        #Pegando os valores exatos usando as chaves 
        titulo = vaga['name']
        empresa = vaga['careerPageName']
        modelo = vaga['workplaceType']
        link = vaga['jobUrl']
        #Imprimindo no terminal só para a gente ver acontecendo
        print(f"📌 Extraindo: {titulo} |  {empresa}")
        #mini-dicionário da vaga atual com os dados dinâmicos
        vaga_atual = {
            'Titulo': titulo,
            'Empresa': empresa,
            'Formato': modelo,
            'Link': link
        }
        vagas_extraidas.append(vaga_atual)
#Entrega de dados para o pandas 
    df = pd.DataFrame(vagas_extraidas)
#Salvar em um Arquivo CSV, na pasta raw | index=False evita que ele crie uma coluna inútil com números de 0 a 10
    df.to_csv('../data/raw/vagas_csv', index=False, sep=';', encoding='utf-8')
    print("\n Sucesso! Arquivo 'vagas_gupy.csv' salvo na pasta data/raw/")
else:
    print(f" Erro ao acessar a API: Status Code {response.status_code}")