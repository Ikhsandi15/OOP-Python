class Player:
    name = ''
    speed = ''

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed

pemain = Player('Susilo', '85')
pemain2 = Player('Josep', '78')
print(pemain.getName() + " mempunyai speed " + pemain.getSpeed())
print(pemain2.getName() + " mempunyai speed " + pemain2.getSpeed())