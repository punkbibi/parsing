import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
import random

# payload_1 = {'p.': 1}
# base_url = 'https://steamcharts.com/top/p.'
# file_steam = open('steam_charts.csv', 'w', newline='\n', encoding='UTF-8_sig')
# csv_obj_steam = csv.writer(file_steam)
# csv_obj_steam.writerow(['Name', 'peak playes'])
# while payload_1['p.'] < 6:
#     url_steam = base_url + str(payload_1['p.'])
#     response_steam = requests.get(url_steam)
#     filename_steam = f'steam_page{payload_1["p."]}.html'
#     with open(filename_steam, 'w', encoding='UTF-8_sig') as file:
#         file.write(response_steam.text)

#     print(response_steam.status_code)
#     soup_steam = BeautifulSoup(response_steam.text, "html.parser")
#     games = soup_steam.find("tbody")

    # for i in games.find_all('tr'):
    #     game_name = i.find("td", class_='game-name left')
    #     peak_players = i.find("td", class_='num')
    #     print(f"game: {game_name.a.text.strip()}, has peak players: {peak_players.text}")
    #     csv_obj_steam.writerow([game_name.a.text.strip(), peak_players.text])
    # payload_1['p.'] += 1
    # sleep(random.randint(5, 20))

print("*********************************************")

payload_mods = {'page': 1}
url = "https://garrysmods.org/browse/tag/maps?per-page=30"
file_mods= open('maps.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj_mods = csv.writer(file_mods)
csv_obj_mods.writerow(['Name', 'downloads'])
while payload_mods['page']< 6:
    response_mod = requests.get(url, params=payload_mods)
    filename_mods = f'mods_page{payload_mods["page"]}.html'
    with open(filename_mods, 'w', encoding='UTF-8_sig') as file:
        file.write(response_mod.text)
    print(response_mod.status_code)
    soup_mod = BeautifulSoup(response_mod.text, 'html.parser')
    panel = soup_mod.find_all('div', class_= 'four columns end')
    
    for e in panel:
        name = e.find('div', class_ = 'download-title')
        download = e.find('li')
        print(f"map: {name.h3.text} has downloads:{download.text}")
        csv_obj_mods.writerow([name.h3.text, download.text])
    payload_mods['page'] += 1
    sleep(random.randint(5, 15))