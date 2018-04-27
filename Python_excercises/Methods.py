class Fighter:

    def __init__(self, name):
        self.name = name
        self.damage = 10
        self.health = 100

    def attack(self, opponent):
         opponent.health = opponent.health - self.damage
         print("{} attcks {}!".format(self.name, opponent.name))


    def __str__(self):
        return "{}: {}".format(self.name, self.health)


ken = Fighter("ken") #object,instance of a class
honda = Fighter("Honda")

ken.attack(honda)
print(honda.health)

ken.attack(honda)
print(honda.health)

