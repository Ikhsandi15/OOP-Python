"""
Staticmethod
dan
Classmethod
"""
class Player:
    job = 'Pemain bola'

    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    @staticmethod
    def retiredIn(age):
        return str(40-age)

    @classmethod
    def generalInfo(cls, age): #Butuh parameter cls->class bukan self karena dia informasi tentang class
        return cls.job + ' akan pensiun dalam ' + cls.retiredIn(age)

pemain = Player('Dybala')
print(Player.generalInfo(25))