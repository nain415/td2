import config
import requests
from bs4 import BeautifulSoup as bs

headers = {'x-api-key':config.API_KEY, 'accept': 'application/json'}
API_URL = config.API_URL


def player_byname(p_name):
    URL = f"{API_URL}/players/byName/{p_name}"
    re = requests.get(URL, headers=headers)
    return re.json()

def player_stats(id):
    URL = f"{API_URL}/players/stats/{id}"
    re = requests.get(URL, headers=headers)
    return re.json()




# profile = player_byname("Cervixsmasher")
# stats = player_stats(profile['_id'])
# print(stats)