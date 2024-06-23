import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Função para extrair dados de um jogo específico
def extrair_dados_jogo(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f'Erro na requisição para {url}: {response.status_code}')
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    box_content_divs = soup.find_all('div', class_='box-content')

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

    for div in box_content_divs:
        # Extrair informações do time da casa
        home_team = div.find('div', class_='sb-team sb-heim')
        if home_team:
            home_team_name_elem = home_team.find('a', class_='sb-vereinslink')
            if home_team_name_elem:
                home_team_name = home_team_name_elem.text.strip()
            else:
                home_team_name = "N/A"
            
            home_team_position_elem = home_team.find('p')
            if home_team_position_elem:
                home_team_position = home_team_position_elem.text.strip().replace('Posição:', '').strip()
            else:
                home_team_position = "N/A"
        else:
            home_team_name = "N/A"
            home_team_position = "N/A"
        
        # Extrair informações do time visitante
        away_team = div.find('div', class_='sb-team sb-gast')
        if away_team:
            away_team_name_elem = away_team.find('a', class_='sb-vereinslink')
            if away_team_name_elem:
                away_team_name = away_team_name_elem.text.strip()
            else:
                away_team_name = "N/A"
            
            away_team_position_elem = away_team.find('p')
            if away_team_position_elem:
                away_team_position = away_team_position_elem.text.strip().replace('Posição:', '').strip()
            else:
                away_team_position = "N/A"
        else:
            away_team_name = "N/A"
            away_team_position = "N/A"

        # Restante do código para extrair dados como rodada, data do jogo, etc.
        game_info = div.find('div', class_='sb-spieldaten')
        round_info_elem = game_info.find('p', class_='sb-datum hide-for-small') if game_info else None
        round_number = re.search(r'(\d+)\.', round_info_elem.text.strip()).group(1).strip() if round_info_elem else "N/A"
        round_info_parts = round_info_elem.text.strip().split('|') if round_info_elem else ["N/A", "N/A", "N/A"]
        game_date = round_info_parts[1].strip()
        game_time = round_info_parts[2].strip()

        result_elem = game_info.find('div', class_='sb-endstand') if game_info else None
        result = result_elem.text.strip() if result_elem else "N/A"
        if ':' in result:
            result_parts = result.split(':')
            home_final_goals = result_parts[0].strip()
            away_final_goals = result_parts[1].strip()[0] if len(result_parts) > 1 else "N/A"
        else:
            home_final_goals = "N/A"
            away_final_goals = "N/A"

        stadium_info_elem = game_info.find('p', class_='sb-zusatzinfos').find('a') if game_info else None
        stadium_info = stadium_info_elem.text.strip() if stadium_info_elem else "N/A"
        attendance_elem = game_info.find('strong') if game_info else None
        attendance = attendance_elem.text.strip() if attendance_elem else "N/A"
        referee_elem = game_info.find_all('a')[-1].text.strip() if game_info else "N/A"

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
        data["Árbitro"].append(referee_elem)  # Usar referee_elem para garantir que o valor seja definido

    return pd.DataFrame(data)

# URL alvo da página com o calendário de jogos
url_calendario = 'https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/gesamtspielplan/wettbewerb/BRA1/saison_id/2022'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url_calendario, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', class_='ergebnis-link')

    dfs = []
    for link in links:
        jogo_url = 'https://www.transfermarkt.com.br' + link.get('href')
        print(f'Raspando dados de {jogo_url}')
        df_jogo = extrair_dados_jogo(jogo_url)
        if df_jogo is not None:
            dfs.append(df_jogo)

    if dfs:
        df_final = pd.concat(dfs, ignore_index=True)
        print("Dados extraídos:")
        print(df_final)
    else:
        print("Nenhum dado foi extraído.")

else:
    print(f'Não foi possível obter o conteúdo da página. Código de status: {response.status_code}')


# Remover linhas que contenham valores "N/A"
# df_final = df_final.replace('N/A', pd.NA).dropna()
# df_final.to_csv('dados_br_campeonato_2022.csv', index=False, encoding='utf-8-sig')
