"""
Memanggil Metode
Parent dengan Super()
"""

class Player:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getSkill(self):
        return 'normal'

class ArgentinaPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        print("Mantep")

    def getSkill(self):
        return 'cepat'

pemain = ArgentinaPlayer('Dybala')
print(f"{pemain.getName()} skillnya {pemain.getSkill()}")