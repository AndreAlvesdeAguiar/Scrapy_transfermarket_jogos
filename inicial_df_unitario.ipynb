import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# URL da página que queremos fazer scraping
url = "https://www.transfermarkt.com.br/se-palmeiras_cuiaba-ec/statistik/spielbericht/4055814"

# Cabeçalhos da requisição para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Enviar a requisição HTTP para a URL com os cabeçalhos
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code != 200:
    print("Erro na requisição:", response.status_code)
    exit()

# Analisar o conteúdo HTML da página
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar o div com a classe 'box-content'
box_content_divs = soup.find_all('div', class_='box-content')

# Listas para armazenar os dados
data = {
    "Time da Casa": [],
    "Posição do Time da Casa": [],
    "Time Visitante": [],
    "Posição do Time Visitante": [],
    "Rodada": [],
    "Data do Jogo": [],
    "Hora do Jogo": [],
    "Resultado Final - Time da Casa": [],
    "Resultado Final - Time Visitante": [],
    "Estádio": [],
    "Público": [],
    "Árbitro": []
}

# Iterar sobre os elementos encontrados
for div in box_content_divs:
    # Extrair informações do time da casa (SE Palmeiras)
    home_team = div.find('div', class_='sb-team sb-heim')
    home_team_name = home_team.find('a', class_='sb-vereinslink').text.strip()
    home_team_position = home_team.find('p').text.strip().replace('Posição:', '').strip()
    
    # Extrair informações do time visitante (Cuiabá EC)
    away_team = div.find('div', class_='sb-team sb-gast')
    away_team_name = away_team.find('a', class_='sb-vereinslink').text.strip()
    away_team_position = away_team.find('p').text.strip().replace('Posição:', '').strip()

    # Extrair informações sobre o jogo
    game_info = div.find('div', class_='sb-spieldaten')
    
    # Extrair a informação da rodada usando regex
    round_info = game_info.find('p', class_='sb-datum hide-for-small').text.strip()
    round_number = re.search(r'(\d+)\.', round_info).group(1)  # Busca o número antes do ponto usando regex
    round_number = round_number.strip()  # Remover espaços extras
    
    # Extrair a data e a hora do jogo
    round_info_parts = round_info.split('|')
    game_date = round_info_parts[1].strip()
    game_time = round_info_parts[2].strip()

    # Extrair o resultado final do jogo
    result = game_info.find('div', class_='sb-endstand').text.strip()
    if ':' in result:
        result_parts = result.split(':')
        home_final_goals = result_parts[0].strip()
        if len(result_parts) > 1:
            away_final_goals = result_parts[1].strip()[0]  # Considera apenas o primeiro número após o ':'
        else:
            away_final_goals = "N/A"  # Se não houver um segundo número após ':'
    else:
        home_final_goals = "N/A"
        away_final_goals = "N/A"

    # Extrair o estádio, público e árbitro
    stadium_info = game_info.find('p', class_='sb-zusatzinfos').find('a').text.strip()
    attendance = game_info.find('strong').text.strip()
    referee = game_info.find_all('a')[-1].text.strip()

    # Armazenar os dados nas listas
    data["Time da Casa"].append(home_team_name)
    data["Posição do Time da Casa"].append(home_team_position)
    data["Time Visitante"].append(away_team_name)
    data["Posição do Time Visitante"].append(away_team_position)
    data["Rodada"].append(round_number)
    data["Data do Jogo"].append(game_date)
    data["Hora do Jogo"].append(game_time)
    data["Resultado Final - Time da Casa"].append(home_final_goals)
    data["Resultado Final - Time Visitante"].append(away_final_goals)
    data["Estádio"].append(stadium_info)
    data["Público"].append(attendance)
    data["Árbitro"].append(referee)

# Criar o DataFrame
df = pd.DataFrame(data)

# Exibir o DataFrame
df
