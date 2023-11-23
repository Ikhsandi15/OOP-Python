"""
Class & Object
"""

# class Player:
#     name = 'Mbappe'

#     def getName(self):
#         return self.name

# pemain = Player()
# print(pemain.name)
# print(pemain.getName())

class Player():
    name = ''

    def getName(self, name2):
        self.name = name2
        return self.name

pemain = Player()
pemain2 = Player()
print("Pemain 1 ", pemain.getName('Gondo'))
print("Pemain 2 ", pemain2.getName('Bambi'))

# satu class bisa punya banyak object