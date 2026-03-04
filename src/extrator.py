import requests
import pandas as pd

#string abaixo, sua identidade diz: "Sou um humano usando Google Chrome no Windows".
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

#Paginação
offset = 0
limite = 10
vagas_extraidas = []
continuar_a_procurar = True

print("--- INICIANDO EXTRAÇÃO EM MASSA DA GUPY ---\n")

#LOOP WHILE)
while continuar_a_procurar:
    
    api_url = f"https://employability-portal.gupy.io/api/v1/jobs?jobName=dados&limit={limite}&offset={offset}"

    # THE REQUEST
    response = requests.get(api_url, headers=headers)

    # Verificando se deu certo
    if response.status_code == 200:
        # transforma em JSON
        dados_json = response.json()
        # cria a lista
        lista_de_vagas = dados_json['data']

        # Condição de paragem com recuo de espaço 
        if len(lista_de_vagas) == 0:
            print("\n Não há mais vagas. Extração concluída!")
            continuar_a_procurar = False
            break #break 

        print(f"A recolher vagas do offset {offset}...")
        
        # Loop de Extração
        for vaga in lista_de_vagas:
            # Pegando os valores usando .get() para evitar KeyErrors
            titulo = vaga.get('name', 'Não informado')
            empresa = vaga.get('careerPageName', 'Não informado')
            modelo = vaga.get('workplaceType', 'Não informado')
            link = vaga.get('jobUrl', 'Sem link')
            
            # Imprimindo no terminal só para a gente ver acontecendo
            print(f"📌 Extraindo: {titulo} |  {empresa}")
            
            # mini-dicionário da vaga atual com os dados dinâmicos
            vaga_atual = {
                'Titulo': titulo,
                'Empresa': empresa,
                'Formato': modelo,
                'Link': link
            }
            vagas_extraidas.append(vaga_atual)
            
        #VIRANDO A PÁGINA PARA A PRÓXIMA VOLTA DO LOOP
        offset += limite
        
    else:
        print(f"Erro ao acessar a API: Status Code {response.status_code}")
        continuar_a_procurar = False # Para o loop se der erro na internet

# FORA DO LOOP 

print(f"\n Total de vagas extraídas no final: {len(vagas_extraidas)}")

# Entrega de dados para o pandas 
df = pd.DataFrame(vagas_extraidas)

# Salvar em um Arquivo CSV, na pasta raw 
df.to_csv('../data/raw/vagas_gupy.csv', index=False, sep=';', encoding='utf-8')
print("\n Sucesso! Arquivo 'vagas_gupy.csv' salvo na pasta data/raw/")