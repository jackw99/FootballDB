# Classes for Football DB

class League():
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.teams = []

    def addTeam(self, Team):
        self.teams.append(Team)

    def showTeams(self):
        print(f"{self.name} teams:\n")
        for team in self.teams:
            print(team.name)


class Team():
    maxPlayers = 30

    def __init__(self, name):
        self.name = name
        self.playerCount = 0
        self.points = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.goalkeepers = []
        self.defenders = []
        self.midfielders = []
        self.attackers = []

    def addGoalkeeper(self, Player):
        if (self.playerCount < self.maxPlayers):
            self.goalkeepers.append(Player)
            self.playerCount += 1

    def addDefender(self, Player):
        if (self.playerCount < self.maxPlayers):
            self.defenders.append(Player)
            self.playerCount += 1

    def addMidfielder(self, Player):
        if (self.playerCount < self.maxPlayers):
            self.midfielders.append(Player)
            self.playerCount += 1

    def addAttacker(self, Player):
        if (self.playerCount < self.maxPlayers):
            self.attackers.append(Player)
            self.playerCount += 1

    def teamSheet(self):
        print(f"{self.name} players:\n")
        if (self.playerCount > 0):
            for player in self.goalkeepers:
                print(f"{player.name} age: {player.age}, position: {type(player)}")
                print("\n")
            for player in self.defenders:
                print(f"{player.name} age: {player.age}, position: {type(player)}")
                print("\n")
            for player in self.midfielders:
                print(f"{player.name} age: {player.age}, position: {type(player)}")
                print("\n")
            for player in self.attackers:
                print(f"{player.name} age: {player.age}, position: {type(player)}")
                print("\n")
        else:
            print("No Players")

    def Win(self):
        self.points += 3
        self.wins += 1

    def Loss(self):
        self.losses += 1

    def Draw(self):
        self.points += 1
        self.draws += 1






class NationalTeam(Team):
    pass


class Player():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.goals = 0
        self.assists = 0
        self.appearances = 0
        self.yellows = 0
        self.reds = 0

    def Show(self):
        print(f"{self.name} is {self.age} years old")


class Goalkeeper(Player):

    def cleanSheets(self):
        return self.cleanSheets()


class Defender(Player):

    def cleanSheets(self):
        return self.cleanSheets()


class Midfielder(Player):
    pass


class Attacker(Player):
    pass
