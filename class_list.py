from random import randrange

class StatBlock:
    def __init__(self, attack, defense, hp):
        self._attack = attack
        self._defense = defense
        self._hp = hp

    def attack(self):
        return randrange(1, (self._attack + 1))
    
    def defend(self):
        return randrange(1, (self._defense + 1))

class Player(StatBlock):
    def __init__(self, name, potion = 0, attack = 10, defense = 8, hp = 50):
        super().__init__(attack, defense, hp)
        self._name = name
        self._potion = potion

    def healing(self):
        print('You heal yourself for 5 points!')
        return 5
    
    def remove_potions(self):
        print('One potion has been used')
        return -1

class Enemy(StatBlock):
    def __init__(self, name = ' ', attack = 0, defense = 0, hp = 0):
        super().__init__(attack, defense, hp)
        self._name = name
