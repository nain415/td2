import config
import requests, pandas, time
import db_fns
from bs4 import BeautifulSoup as bs

headers = {'x-api-key':config.API_KEY, 'accept': 'application/json'}
API_URL = config.API_URL
LIMIT = 1000


#expects 1000 >= lim > 0 in integers
#offset > 0 in integers, optional
def player_stats(lim, offset=""):
    if offset:
        URL = f"{API_URL}/players/stats?limit={lim}&offset={offset}"
    else:
        URL = f"{API_URL}/players/stats?limit={lim}"
    re = requests.get(URL, headers=headers)
    return re.json()


#expects (byID, <id>), (byName, <name>), (bestFriends, <id>), (matchHistory, <id>) all strings
#example (byName, "Jules")
def player_path_id(path,pid):
    URL = f"{API_URL}/players/{path}/{pid}"
    re = requests.get(URL, headers=headers)
    return re.json()

#expects YYYY-MM-DD for start_date and end_date
#expects lim > 0 in integers
#offset > 0 in integers, optional
#example (2022-08-08, 2022-08-07, 10)
def game_stats(start_date, end_date, lim, offset=""):
    if offset:
        URL = f"{API_URL}/games?limit={str(lim)}&offset={offset}&sortBy=date&sortDirection=1&dateBefore={start_date}%2000%3A00%3A00&dateAfter={end_date}%2000%3A00%3A00&includeDetails=true&countResults=true&queueType=Classic"
    else:
        URL = URL = f"{API_URL}/games?limit={lim}&sortBy=date&sortDirection=1&dateBefore={start_date}%2000%3A00%3A00&dateAfter={end_date}%2000%3A00%3A00&includeDetails=true&countResults=true&queueType=Classic"
    re = requests.get(URL, headers=headers)
    return re.json()


#takes player statisics and converts to table-insertable form
#also some defensive if cases
def shape(stats):
    for num in range(len(stats)):
        if len(stats[num]['profile']) == 0:
            stats[num]['playerName'] = ""

        else:
            stats[num]['playerName'] = stats[num]['profile'][0]['playerName']
        
        if 'gamesPlayed' not in stats[num]:
            stats[num]['gamesPlayed'] = 0
        
        if 'secondsPlayed' not in stats[num]:
            stats[num]['secondsPlayed'] = 0


#query limit of 1000
#start and end are indices.  will fetch in multiples of 1000
#in range [start, end] inclusive.
#example populate_players(1,2)
def populate_players(start, end):
    try:
        for i in range(start,end+1):
            t = time.time()

            players = player_stats(LIMIT, i*LIMIT)
            shape(players)
            db_fns.ins('stats', players)

            print(f"inserted {i*LIMIT} to {(i+1)*LIMIT}.")
            print(f"It took {time.time() - t} seconds taken to do this.")

    except Exception as e:
        print(e)
        print('Done populating.  Program crashed.')



    
#db_fns.ins('player', first_player[0])
#print(first_player)
    



#res = game_stats('2022-07-01', '2022-07-2', 100)
# profile = player_byname("Cervixsmasher")
# stats = player_stats(profile['_id'])
# print(stats)