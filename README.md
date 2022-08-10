# TD2 Analysis

<p align="center">
<img src=https://user-images.githubusercontent.com/78244259/183784327-d59589e8-f450-4ed3-b1f2-a70e787a96dc.png>

</p>

1. identify techniques to be represented.
2. ask how those can be implemented using my database
3. consider visuals, draw visuals
4. encode visuals


SELECT playerName, ROUND(secondsPlayed / POW(60.0,2), 2) as hours_played, gamesPlayed, classicElo
FROM
	(SELECT *, row_number() OVER (PARTITION BY match_id) as n
		FROM playermatch
		JOIN player on player.id = playermatch.player_id
		WHERE substr(player.playerName, 1, 1) LIKE 's'
		GROUP BY playerName) results
WHERE results.n > 1
ORDER BY hours_played DESC, classicElo DESC
