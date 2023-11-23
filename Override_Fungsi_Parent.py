"""
Override Fungsi
Parent
"""

class Player:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getSkill(self):
        return "normal"

class ArgentinaPlayer(Player):
    def getSkill(self):
        return "cepat"

class BrazilPlayer(Player):
    def getSkill(self):
        return "Keras"

class MalaysiaPlayer(Player):
    pass

player1 = ArgentinaPlayer('Dybala', '87')
player2 = MalaysiaPlayer('Sultan', '77')

print(player1.getName() + " Skill " + player1.getSkill())
print(player2.getName() + " Skill " + player2.getSkill())