import config
import requests, pandas, time, datetime
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
#expects HH-MM-SS for start_time and end_time, optional
#lim > 0 in integers, optional
#offset > 0 in integers, optional
#example (2022-08-03, 00-00-00, 2022-08-04, 10:20:00, 10)
def game_stats(start_date, end_date, start_time='00-00-00', end_time='00-00-00', lim=50, offset=""):
    
    start_time = start_time.replace('-', '%3A')
    end_time = end_time.replace('-', '%3A')

    if offset:
        URL = f"{API_URL}/games?limit={str(lim)}&offset={offset}&sortBy=date&sortDirection=1&dateBefore={end_date}%20{end_time}&dateAfter={start_date}%20{start_time}&includeDetails=true&countResults=false&queueType=Classic"
    else:
        URL = f"{API_URL}/games?limit={str(lim)}&sortBy=date&sortDirection=1&dateBefore={end_date}%20{end_time}&dateAfter={start_date}%20{start_time}&includeDetails=true&countResults=false&queueType=Classic"

    re = requests.get(URL, headers=headers)
    return re.json()


#takes player statisics and converts to table-insertable form
#also some defensive if cases
def shape_players(stats):
    for num in range(len(stats)):
        if len(stats[num]['profile']) == 0:
            stats[num]['playerName'] = ""

        else:
            stats[num]['playerName'] = stats[num]['profile'][0]['playerName']
        
        if 'gamesPlayed' not in stats[num]:
            stats[num]['gamesPlayed'] = 0
        
        if 'secondsPlayed' not in stats[num]:
            stats[num]['secondsPlayed'] = 0

def shape_matches():
    pass

def shape_playerData():
    pass

#query limit of 1000
#start and end are indices.  will fetch in multiples of 1000
#in range [start, end] inclusive.
#example populate_players(1,2)
def populate_players(start, end):
    try:
        for i in range(start,end+1):
            t = time.time()

            players = player_stats(LIMIT, i*LIMIT)
            shape_players(players)
            db_fns.ins('player', players)

            print(f"inserted {i*LIMIT} to {(i+1)*LIMIT}.")
            print(f"It took {time.time() - t} seconds taken to do this.")

    except Exception as e:
        print(e)
        print('Done populating.  Program crashed.')


#query limit of 50

def populate_matches(start_date, end_date, start, end):
    try:
        for i in range(start,end+1):
            t = time.time()

            matches = game_stats(start_date, end_date, LIMIT, end)
            shape_players(matches)
            db_fns.ins('match', matches)

            print(f"inserted {i*LIMIT} to {(i+1)*LIMIT}.")
            print(f"It took {time.time() - t} seconds taken to do this.")

    except Exception as e:
        print(e)
        print('Done populating.  Program crashed.')

#subprocess of populate_matches
def populate_playerData(js):
        db_fns.ins('playerData', js)


    
#db_fns.ins('player', first_player[0])
#print(first_player)
    



#res = game_stats('2022-07-01', '2022-07-2', 100)
# profile = player_byname("Cervixsmasher")
# stats = player_stats(profile['_id'])
# print(stats)