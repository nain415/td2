import sqlite3

conn = sqlite3.connect('td2.db')
cur = conn.cursor()

def close():
    conn.close()
    cur.close()

def connect():
    conn = sqlite3.connect('td2.db')
    conn.cursor()

#enter this to end any transaction
def commit():
    conn.commit()

def rollback():
    conn.execute('ROLLBACK')

#enter this before beginning any transaction
def begin():
    conn.execute('BEGIN')



def ins(what, js):
    if what == 'player':
        fields = '(:_id, :playerName, :secondsPlayed, :gamesPlayed)'
    elif what == 'match':
        fields = '(:_id, :date, :queueType, :endingWave, :gameLength, :gameElo)'
    else:
        fields = '(:playerId, :match_id, :playerSlot, :legion, :workers, :value, :gameResult, :classicElo, :chosenSpell, :firstWaveFighters)'
    
    cur.executemany(
    f'''INSERT INTO {what} VALUES {fields}
        ON CONFLICT DO NOTHING;
    ''', js)

def create_table():
    
    cur.execute('''
    CREATE TABLE IF NOT EXISTS player (id TEXT PRIMARY KEY, playerName TEXT UNIQUE, secondsPlayed INTEGER, gamesPlayed INTEGER);
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS match (id TEXT PRIMARY KEY, date TEXT, queueType TEXT, endingWave INTEGER, gameLength INTEGER, gameElo INTEGER);
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS playermatch (player_id TEXT REFERENCES player(id), match_id TEXT REFERENCES match(id), playerSlot INTEGER, legion TEXT, workers INTEGER, value INTEGER,
    gameResult TEXT, classicElo INTEGER, chosenSpell TEXT, firstWaveFighters TEXT,
    PRIMARY KEY(player_id, match_id)
    );
    ''')
