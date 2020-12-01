#Object-Oriented approach to a Football DB
# creating examples of player, team and league classes
import pandas as pd
import Classes as c

#2018-19 premier league season csv's for initiation
players = pd.read_csv(r'C:\DATASETS\FootballDB\premplayers.csv', sep=',')
teams = pd.read_csv(r'C:\DATASETS\FootballDB\premteams.csv', sep=',')

players = players.get(['full_name', 'age', 'Current Club', 'position', 'appearances_overall', 'goals_overall',
                          'assists_overall', 'clean_sheets_overall', 'yellow_cards_overall',
                          'red_cards_overall']).sort_values(by=['Current Club'])

teams = teams.get(['team_name', 'common_name', 'country', 'matches_played', 'wins', 'draws', 'losses', 'goals_scored',
                      'goals_conceded']).sort_values(by=['team_name'])


#code has to add all teams to league, then iterate through all players and add them to each team
prem = c.League("Premier League", "England")

#loops through DF of teams and creates objects for each team, then populates league object with the teams
for i, f in teams.iterrows():
    prem.addTeam(c.Team(f['team_name'], f['common_name'], f['wins'], f['draws'], "England"))

#prem.showTeams()

#iterating through players adding to teams
for i, j in players.iterrows():
    #checking players position, creating temp player object
    # then appending to correct club according to correct method
    if(j['position'] == 'Goalkeeper'):
        p = c.Goalkeeper(j['full_name'], j['age'])
        for team in prem.getTeams():
            if(j['Current Club'] == team.common):
                team.addGoalkeeper(p)
    if (j['position'] == 'Defender'):
        p = c.Defender(j['full_name'], j['age'])
        for team in prem.getTeams():
            if (j['Current Club'] == team.common):
                team.addDefender(p)
    if (j['position'] == 'Midfielder'):
        p = c.Midfielder(j['full_name'], j['age'])
        for team in prem.getTeams():
            if (j['Current Club'] == team.common):
                team.addMidfielder(p)
    if (j['position'] == 'Forward'):
        p = c.Attacker(j['full_name'], j['age'])
        for team in prem.getTeams():
            if (j['Current Club'] == team.common):
                team.addAttacker(p)


print("Teams in prem:\n")
for team in prem.getTeams():
    print(team.name)
print("\nThe Mighty Reds:\n")

for player in prem.getTeams()[11].allPlayers:
    print(player.name)

print("\nPremier League Table 2018/19:")
#Sorting and printing a league table
for team in prem.getTeams():
    for i in range(team.wins):
        team.Win()
    for i in range(team.draws):
        team.Draw()

j = 1
for team in prem.table():
    print(f"{j}. {team.name}: {team.points} Points")
    j += 1

#main
#if __name__ == '__main__':
#    pass







