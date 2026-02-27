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
    
    #passar por cada dicionário (vaga) dentro da lista
    for vaga in lista_de_vagas:
        
        #Pegando os valores exatos usando as chaves 
        titulo = vaga['name']
        empresa = vaga['careerPageName']
        modelo = vaga['workplaceType']
        link = vaga['jobUrl']
        
        #Imprimindo um "Cartão" no terminal
        print(f"📌 Vaga: {titulo}")
        print(f"🏢 Empresa: {empresa} | 📍 Formato: {modelo}")
        print(f"🔗 Link: {link}")
        print("-" * 50) # Imprime uma linha de separação
#Criando uma lista vazia antes do loop
vagas_extraidas = []