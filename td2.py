import config
import requests
from bs4 import BeautifulSoup as bs

headers = {'x-api-key':config.API_KEY, 'accept': 'application/json'}
API_URL = config.API_URL


def player_byname(p_name):
    URL = f"{API_URL}/players/byName/{p_name}"
    re = requests.get(URL, headers=headers)
    return re.json()

def player_stats():
    URL = f"{API_URL}/games?limit=5&offset=5&sortBy=date&sortDirection=1&dateBefore=2022-08-08%2000%3A00%3A00&dateAfter=2022-08-06%2000%3A00%3A00&includeDetails=true&countResults=true&queueType=Classic"
    re = requests.get(URL, headers=headers)
    return re.json()

res = player_stats()


# profile = player_byname("Cervixsmasher")
# stats = player_stats(profile['_id'])
# print(stats)