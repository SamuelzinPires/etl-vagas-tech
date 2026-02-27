import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
target_url = "https://portal.gupy.io/job-search/term=dados"
response = requests.get(target_url, headers=headers)

# --- INÍCIO DA EXTRAÇÃO ---
Sopa = BeautifulSoup(response.text, 'html.parser')

# 1. Busca todos os itens de lista (os cartões de vaga)
vagas = Sopa.find_all('li') 

print(f"Foram encontradas {len(vagas)} possíveis vagas na página.\n")

for vaga in vagas:
    # 2. Busca o Título
    titulo_tag = vaga.find('h3')
    
    # 3. Busca a Empresa (Tentando pegar o primeiro <p> ou <span>)
    # Primeiro tentamos <p>, se não achar, tentamos <span>
    empresa_tag = vaga.find('p') 
    if not empresa_tag:
        empresa_tag = vaga.find('span')

    # 4. Só imprime se achar o título (para ignorar os <li> do menu superior do site)
    if titulo_tag:
        titulo = titulo_tag.text.strip()
        
        # Se achou a tag da empresa, limpa o texto, senão, diz "Empresa não encontrada"
        empresa = empresa_tag.text.strip() if empresa_tag else "Empresa não encontrada"
        
        print(f"📌 {titulo} | 🏢 {empresa}")