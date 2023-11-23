"""
Mewariskan sifat
Inheritance
"""

class Player:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


class ArgentinaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age

player = ArgentinaPlayer('Dybala', '86')
print(player.getName() + " umurnya " + player.setAge('23'))