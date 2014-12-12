import numpy as np
import os

data = np.genfromtxt('leagues_NBA_2014_team.csv',delimiter=',',skip_header=1)

teams = []
teamplayers = []
teamplayersdata = []
uniqplayers = []
uniqplayersdata = []
n = 0

for teamname in os.listdir("./Teams"):
	teams.append(teamname)
	playersinteam = []
	playersinteamdata = []
	if str(teamname) not in ".DS_Store":
		print ('The team name is ' + str(teamname))
		for player in os.listdir("./Teams/" + str(teamname)):
			playersinteam.append(player)
			playerdata = np.genfromtxt(('Teams/' + str(teamname) + '/' + player),delimiter=',',skip_header=1)
			playersinteamdata.append(playerdata)
			playername = str(player)[10:-13]
			if playername not in uniqplayers:
				uniqplayers.append(playername)
				n += 1
			print ('	Player: ' + playername)
		teamplayers.append(playersinteam)
		teamplayersdata.append(playersinteamdata)

print (uniqplayers)
print ('Number of players switching = ' + str(n - len(uniqplayers)))
