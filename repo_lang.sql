--corrects github repo language
CREATE TABLE IF NOT EXISTS playermatch (player_id TEXT REFERENCES player(id), match_id TEXT REFERENCES match(id), playerSlot INTEGER, legion TEXT, workers INTEGER, value INTEGER,
    gameResult TEXT, classicElo INTEGER, chosenSpell TEXT, firstWaveFighters TEXT,
    PRIMARY KEY(player_id, match_id)
    );
