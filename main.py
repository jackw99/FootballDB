# creating examples of player, team and league classes
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
        self.players = []

    def addPlayer(self, Player):
        if (len(self.players)<self.maxPlayers):
            self.players.append(Player)

    def teamSheet(self):
        print(f"{self.name} players:\n")
        if(len(self.players) != 0):
            for player in self.players:
                print(f"{player.name} age: {player.age}, position: {player.position}")
                print("\n")
        else:
            print("No Players")



class Player():
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.goals = 0
        self.assists = 0
        self.appearances = 0

    def Show(self):
        print(f"{self.name} is {self.age} years old")




if __name__ == '__main__':

    #LFC Players
    p = Player("Alisson", 28, "GK")
    p1 = Player("Alexander-Arnold", 20, "RB")
    p2 = Player("Gomez", 21, "CB")
    p3 = Player("Van Dijk", 27, "CB")
    p4 = Player("Robertson", 24, "LB")
    p5 = Player("Henderson", 28, "RCM")
    p6 = Player("Fabinho", 27, "CDM")
    p7 = Player("Thiago", 28, "LCM")
    p8 = Player("Salah", 29, "RW")
    p9 = Player("Firmino", 28, "CF")
    p10 = Player("Mane", 29, "LW")

    #Man City Players
    t = Player("Ederson", 29, "GK")
    t1 = Player("Walker", 32, "RB")
    t2 = Player("Diaz", 25, "CB")
    t3 = Player("Laporte", 23, "CB")
    t4 = Player("Mendy", 24, "LB")
    t5 = Player("Gundogan", 31, "RCM")
    t6 = Player("Rodri", 27, "CDM")
    t7 = Player("Foden", 21, "LCM")
    t8 = Player("Mahrez", 29, "RW")
    t9 = Player("Jesus", 23, "CF")
    t10 = Player("Sterling", 27, "LW")

    #Tottenham Players
    r = Player("Lloris", 30, "GK")
    r1 = Player("Aurier", 26, "RB")
    r2 = Player("Dier", 24, "CB")
    r3 = Player("Alderweireld", 32, "CB")
    r4 = Player("Davies", 27, "LB")
    r5 = Player("Ndombele", 25, "RDCM")
    r6 = Player("Winks", 24, "LDCM")
    r7 = Player("Bale", 32, "RM")
    r8 = Player("Son", 28, "CAM")
    r9 = Player("Bergjwin", 24, "LM")
    r10 = Player("Kane", 25, "ST")

    #List of Teams players
    players = [p, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    players1 = [t, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
    players2 = [r, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]

    t = Team("Liverpool FC")
    t1 = Team("Manchester City")
    t2 = Team("Tottenham Hotspur")

    engTeams = [t, t1, t2]

    for i in players:
        t.addPlayer(i)

    for i in players1:
        t1.addPlayer(i)

    for i in players2:
        t2.addPlayer(i)

    #t.teamSheet()
    #t1.teamSheet()
    #t2.teamSheet()

    league = League("Premier League", "England")

    league.addTeam(t)
    league.addTeam(t1)
    league.addTeam(t2)

    league.showTeams()





