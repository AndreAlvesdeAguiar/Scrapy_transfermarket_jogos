import requests
from bs4 import BeautifulSoup

# URL alvo
url = 'https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/2022'

# Cabeçalhos da requisição para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Enviar a requisição HTTP para a URL com os cabeçalhos
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Parsear o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos os elementos <a> com a classe 'ergebnis-link'
    links = soup.find_all('a', class_='ergebnis-link')
    
    # Iterar sobre os links encontrados
    for link in links:
        href = link.get('href')
        print(href)

else:
    print(f'Não foi possível obter o conteúdo da página. Código de status: {response.status_code}')
