"""
Private di
OOP Python
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.__age = '23'

    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

class ArgentinaPlayer(Player):
    pass

player = Player('Dybala')
print(player.getAge())