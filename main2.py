
import random

warrior = {
    'name' : 'warrior',
    'potion' : 3,
    'atk' : 7,
    'def' : 7,
    'hp' : 20,
    'id' : 0
}

zombie = {
    'name' : 'zombie',
    'atk' : 10,
    'def' : 2,
    'hp' : 8,
    'id' : 1
}

bat = {
    'name' : 'bat',
    'atk' : 3,
    'def' : 2,
    'hp' : 4,
    'id' : 2
}

class StatBlock:
    def __init__(self, attack, defense, hp):
        self._attack = attack
        self._defense = defense
        self._hp = hp

    def attack(self):
        return random.randrange(1, (self._attack + 1))
    
    def defend(self):
        return random.randrange(1, (self._defense + 1))

class Player(StatBlock):
    def __init__(self, name, potion, attack, defense, hp):
        super().__init__(attack, defense, hp)
        self._name = name
        self._potion = potion

    def healing(self):
        print('You heal yourself for 5 points!')
        return 5
    
    def remove_potions(self):
        print('One potion has been used')
        return -1

class Warrior(StatBlock):
    def __init__(self, name, potion, attack, defense, hp):
        super().__init__(attack, defense, hp)
        self._name = name
        self._potion = potion

    def healing(self):
        return 5
    
    def remove_potions(self):
        return -1

class Scorpion(StatBlock):
    def __init__(self, name, poison, attack, defense, hp):
        super().__init__(attack, defense, hp)
        self._name = name
        self._poison_count = poison
    
    def poison(self):
        return 1

class Bat(StatBlock):
    def __init__(self, name, attack, defense, hp):
        super().__init__(attack, defense, hp)
        self._name = name

potion_count = 0

player_hp = 50

while player_hp > 0:

    enemy_count = random.randrange(0, 11)

    if enemy_count > 8:
        enemy1 = Warrior(warrior.get('name'), warrior.get('potion'), warrior.get('atk'), warrior.get('def'), warrior.get('hp'))
        enemy2 = Warrior(warrior.get('name'), warrior.get('potion'), warrior.get('atk'), warrior.get('def'), warrior.get('hp'))
        enemy3 = Warrior(warrior.get('name'), warrior.get('potion'), warrior.get('atk'), warrior.get('def'), warrior.get('hp'))

    elif enemy_count > 5:
        enemy1 = Warrior(warrior.get('name'), warrior.get('potion'), warrior.get('atk'), warrior.get('def'), warrior.get('hp'))
        enemy2 = Warrior(warrior.get('name'), warrior.get('potion'), warrior.get('atk'), warrior.get('def'), warrior.get('hp'))
        enemy3 = 'No Enemy Here'
        
    else:
        enemy1 = Warrior(warrior.get('name'), warrior.get('potion'), warrior.get('atk'), warrior.get('def'), warrior.get('hp'))
        enemy2 = 'No Enemy Here'
        enemy3 = 'No Enemy Here'
        


