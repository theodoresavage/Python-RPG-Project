
import random


tier1_creatures = ['Bat','Wolf','Giant Wasp']
tier2_creatures = ['Zombie','Warrior','Death Hound']
tier3_creatures = ['Basilisk','Witch','Dragon']


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

class Enemy(StatBlock):
    def __init__(self, name = ' ', attack = 0, defense = 0, hp = 0):
        super().__init__(attack, defense, hp)
        self._name = name

player_hp = 50

enemy_tier = 0
enemy_count = 0

enemy1 = 0
enemy2 = 0
enemy3 = 0

def hp_generation(num1):
    return random.randrange(5,11) + num1
 
def attack_generation(num1):
    return (random.randrange(3,11) + num1)

def defense_generation(num1):
    return (random.randrange(3,11) + num1)

def potion_generation(num1):
    pass

def enemy_encounter_level():
    global enemy_tier
    enemy_tier = random.randrange(1,11)

def enemy_total():
    global enemy_count
    enemy_count = random.randrange(1,11)

def creature_generator(creature):
    
    enemy_encounter_level()

    if enemy_tier > 9:
        creature = Enemy(creature_name(tier3_creatures),attack_generation(10),defense_generation(10),hp_generation(10))

    elif enemy_tier > 7:
        creature = Enemy(creature_name(tier2_creatures),attack_generation(5),defense_generation(5),hp_generation(5))

    else:
        creature = Enemy(creature_name(tier1_creatures),attack_generation(0),defense_generation(0),hp_generation(0))
    
    return creature

def creature_name(tier):
    return tier[random.randrange(0,len(tier))]

def print_stat_block(creature):
    print(f'{creature._name} - HP: {creature._hp} ATK: {creature._attack} DEF: {creature._defense}')

def creature_party_generator():
    global enemy_count
    global enemy1
    global enemy2
    global enemy3

    enemy_total()

    if enemy_count > 9:
        enemy1 = creature_generator(enemy1)
        enemy2 = creature_generator(enemy2)
        enemy3 = creature_generator(enemy3)
        print(f'You are facing a {enemy1._name}, a {enemy2._name}, and a {enemy3._name}\n')
        print('Their stats are as follows: \n')
        print_stat_block(enemy1)
        print_stat_block(enemy2)
        print_stat_block(enemy3)

    elif enemy_count > 6:
        enemy1 = creature_generator(enemy1)
        enemy2 = creature_generator(enemy2)
        print(f'You are facing a {enemy1._name} and a {enemy2._name}\n')
        print('Their stats are as follows: \n')
        print_stat_block(enemy1)
        print_stat_block(enemy2)

    else:
        enemy1 = creature_generator(enemy1)
        print(f'You are facing a {enemy1._name}\n')
        print('Their stats are as follows: \n')
        print_stat_block(enemy1)


creature_party_generator()