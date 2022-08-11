# TD2 Analysis

<p align="center">
<img src=https://user-images.githubusercontent.com/78244259/183784327-d59589e8-f450-4ed3-b1f2-a70e787a96dc.png>

</p>

1. identify techniques to be represented.
2. ask how those can be implemented using my database
3. consider visuals, draw visuals
4. encode visuals

1 - all players whose names start with 'S' or 's', and have a common game with another player who also is like that.  data about them

SELECT playerName, ROUND(secondsPlayed / POW(60.0,2), 2) as hours_played, gamesPlayed, classicElo
FROM
	(SELECT *, row_number() OVER (PARTITION BY match_id) as n
		FROM playermatch
		JOIN player on player.id = playermatch.player_id
		WHERE substr(player.playerName, 1, 1) LIKE 's'
		GROUP BY playerName) results
WHERE results.n > 1
ORDER BY hours_played DESC, classicElo DESC


2 - stats about games played throughout each day of the first week of august 2022

SELECT COUNT(*) as count_games, ROUND(SUM(gameLength / POW(60.0, 2)), 2) as total_game_len,  ROUND(AVG(gameLength) / 60.0) as avg_game_len,
	
	CASE CAST(STRFTIME('%w', date) AS INTEGER)
		WHEN 0 THEN DATE(date) || ' Sun'
		WHEN 1 THEN DATE(date) || ' Mon'
		WHEN 2 THEN DATE(date) || ' Tue' 
		WHEN 3 THEN DATE(date) || ' Wed' 
		WHEN 4 THEN DATE(date) || ' Thu' 
		WHEN 5 THEN DATE(date) || ' Fri' 
		ELSE DATE(date) || ' Sat' END as dt
FROM match
GROUP BY dt
ORDER BY count_games DESC;

3 - top 3 openers for each day.  more window fns

SELECT * FROM (
SELECT *, dense_rank () OVER (PARTITION BY dt ORDER BY num_occ DESC) rk FROM
(SELECT *, COUNT(*) as num_occ, DATE(match.date) as dt
FROM match
GROUP BY endingWave, dt))
WHERE rk < 4

4 - how many times people have played Pyro each day.  having clause demo.  maybe restructure this so we can have a select within a select?

SELECT *, COUNT(firstwaveFighters) as ct, DATE(date) as dt FROM match
JOIN playermatch on match.id = playermatch.match_id
WHERE firstWaveFighters != ""
GROUP BY firstWaveFighters, dt
HAVING firstWaveFighters = 'Pyro'

5 - cross join

6 - self join
