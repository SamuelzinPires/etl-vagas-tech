import requests
import time

# string abaixo, sua identidade diz: "Sou um humano usando Google Chrome no Windows".
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
#endereço do request
target_url = "https://portal.gupy.io/job-search/term=dados"
#THE REQUEST
response = requests.get(target_url, headers=headers)
#validação
print(f"Server Status Code: {response.status_code}")