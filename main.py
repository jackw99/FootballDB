# creating examples of player, team and league classes
import Classes as c

#LFC Players
p = c.Goalkeeper("Alisson", 28)
p1 = c.Defender("Alexander-Arnold", 20)
p2 = c.Defender("Gomez", 21)
p3 = c.Defender("Van Dijk", 27)
p4 = c.Defender("Robertson", 24)
p5 = c.Midfielder("Henderson", 28)
p6 = c.Midfielder("Fabinho", 27)
p7 = c.Midfielder("Thiago", 28)
p8 = c.Attacker("Salah", 29)
p9 = c.Attacker("Firmino", 28)
p10 = c.Attacker("Mane", 29)

#Man City Players
t = c.Goalkeeper("Ederson", 29)
t1 = c.Defender("Walker", 32)
t2 = c.Defender("Diaz", 25)
t3 = c.Defender("Laporte", 23)
t4 = c.Defender("Mendy", 24)
t5 = c.Midfielder("Gundogan", 31)
t6 = c.Midfielder("Rodri", 27)
t7 = c.Midfielder("Foden", 21)
t8 = c.Attacker("Mahrez", 29)
t9 = c.Attacker("Jesus", 23)
t10 = c.Attacker("Sterling", 27)

#Tottenham Players
r = c.Goalkeeper("Lloris", 30)
r1 = c.Defender("Aurier", 26)
r2 = c.Defender("Dier", 24)
r3 = c.Defender("Alderweireld", 32)
r4 = c.Defender("Davies", 27)
r5 = c.Midfielder("Ndombele", 25)
r6 = c.Midfielder("Winks", 24)
r7 = c.Attacker("Bale", 32)
r8 = c.Attacker("Son", 28)
r9 = c.Attacker("Bergjwin", 24)
r10 = c.Attacker("Kane", 25)

# Barca
e = c.Goalkeeper("ter Stegen", 27)
e1 = c.Defender("Dest", 19)
e2 = c.Defender("Garcia", 21)
e3 = c.Defender("Lenglet", 27)
e4 = c.Defender("Alba", 33)
e5 = c.Midfielder("Lopez", 22)
e6 = c.Midfielder("de Jong", 23)
e7 = c.Midfielder("Coutinho", 28)
e8 = c.Attacker("Messi", 33)
e9 = c.Attacker("Braithwaite", 26)
e10 = c.Attacker("Griezmann", 29)

# Real Madrid Players
f = c.Goalkeeper("Courtois", 28)
f1 = c.Defender("Vazquez", 19)
f2 = c.Defender("Varane", 27)
f3 = c.Defender("Ramos", 32)
f4 = c.Defender("Marcelo", 34)
f5 = c.Midfielder("Modric", 33)
f6 = c.Midfielder("Casemiro", 30)
f7 = c.Midfielder("Kroos", 31)
f8 = c.Attacker("Asensio", 25)
f9 = c.Attacker("Benzema", 29)
f10 = c.Attacker("Hazard", 28)

# Atleti Players
v = c.Goalkeeper("Oblak", 28)
v1 = c.Defender("Savic", 31)
v2 = c.Defender("Gimenez", 27)
v3 = c.Defender("Hermoso", 22)
v4 = c.Defender("Trippier", 29)
v5 = c.Midfielder("Koke", 31)
v6 = c.Midfielder("Niguez", 27)
v7 = c.Midfielder("Lodi", 24)
v8 = c.Attacker("Llorente", 28)
v9 = c.Attacker("Correa", 25)
v10 = c.Attacker("Lemar", 27)

t, t1, t2 = c.Team("Liverpool FC"), c.Team("Manchester City"), c.Team("Tottenham Hotspur")
t3, t4, t5 = c.Team("Barcelona"), c.Team("Real Madrid"), c.Team("Atletico Madrid")
t6, t7, t8, t9, t10 = c.Team("West Ham"), c.Team("Southampton"), c.Team("Chelsea"), c.Team("Wolverhampton Wanderers"), c.Team("Arsenal")

league = c.League("Premier League", "England")
league2 = c.League("Liga Santander", "Spain")

#main
if __name__ == '__main__':

    #Adding Players to teams
    t.addGoalkeeper(p)
    t.addDefender(p1)
    t.addDefender(p2)
    t.addDefender(p3)
    t.addDefender(p4)
    t.addMidfielder(p5)
    t.addMidfielder(p6)
    t.addMidfielder(p7)
    t.addAttacker(p8)
    t.addAttacker(p9)
    t.addAttacker(p10)

    t1.addGoalkeeper(t)
    t1.addDefender(t1)
    t1.addDefender(t2)
    t1.addDefender(t3)
    t1.addDefender(t4)
    t1.addMidfielder(t5)
    t1.addMidfielder(t6)
    t1.addMidfielder(t7)
    t1.addAttacker(t8)
    t1.addAttacker(t9)
    t1.addAttacker(t10)

    t2.addGoalkeeper(r)
    t2.addDefender(r1)
    t2.addDefender(r2)
    t2.addDefender(r3)
    t2.addDefender(r4)
    t2.addMidfielder(r5)
    t2.addMidfielder(r6)
    t2.addMidfielder(r7)
    t2.addAttacker(r8)
    t2.addAttacker(r9)
    t2.addAttacker(r10)

    t3.addGoalkeeper(e)
    t3.addDefender(e1)
    t3.addDefender(e2)
    t3.addDefender(e3)
    t3.addDefender(e4)
    t3.addMidfielder(e5)
    t3.addMidfielder(e6)
    t3.addMidfielder(e7)
    t3.addAttacker(e8)
    t3.addAttacker(e9)
    t3.addAttacker(e10)

    t4.addGoalkeeper(f)
    t4.addDefender(f1)
    t4.addDefender(f2)
    t4.addDefender(f3)
    t4.addDefender(f4)
    t4.addMidfielder(f5)
    t4.addMidfielder(f6)
    t4.addMidfielder(f7)
    t4.addAttacker(f8)
    t4.addAttacker(f9)
    t4.addAttacker(f10)

    t5.addGoalkeeper(v)
    t5.addDefender(v1)
    t5.addDefender(v2)
    t5.addDefender(v3)
    t5.addDefender(v4)
    t5.addMidfielder(v5)
    t5.addMidfielder(v6)
    t5.addMidfielder(v7)
    t5.addAttacker(v8)
    t5.addAttacker(v9)
    t5.addAttacker(v10)


    #Adding teams to leagues
    league.addTeam(t)
    league.addTeam(t1)
    league.addTeam(t2)
    league2.addTeam(t3)
    league2.addTeam(t4)
    league2.addTeam(t5)
    league.addTeam(t6)
    league.addTeam(t7)
    league.addTeam(t8)
    league.addTeam(t9)
    league.addTeam(t10)

    #print("First League:\n")
    #league.showTeams()
    #print("\n")
    #print("Second League:\n")
    #league2.showTeams()

    #t.teamSheet()

    #print(t.attackers[2].goals)

    for i in range(67):
        t.Win()
    for i in range(54):
        t1.Win()
    for i in range(33):
        t2.Win()
    for i in range(5):
        t6.Win()
    for i in range(11):
        t7.Win()
    for i in range(8):
        t8.Win()
    for i in range(17):
        t9.Win()
    for i in range(49):
        t10.Win()

    print(t.points)
    print(t1.points)
    print(t2.points)

    j = 1
    for i in (league.table()):
        print(f"{j}. {i.name}:  {i.points} points")
        j += 1


