
import random
import time


tier1_creatures = ['Bat','Wolf','Giant Wasp']
tier2_creatures = ['Zombie','Warrior','Death Hound']
tier3_creatures = ['Basilisk','Witch','Dragon']


class StatBlock:
    def __init__(self, attack, defense, hp, initiative):
        self._attack = attack
        self._defense = defense
        self._hp = hp
        self._initiative = initiative

    def attack(self):
        return random.randrange(1, (self._attack + 1))
    
    def defend(self):
        return random.randrange(1, (self._defense + 1))

class Player(StatBlock):
    def __init__(self, name, potion = 0, attack = 10, defense = 10, hp = 20, initiative = 0):
        super().__init__(attack, defense, hp, initiative)
        self._name = name
        self._potion = potion

    def healing(self):
        print('You heal yourself for 5 points!')
        return 5
    
    def remove_potions(self):
        print('One potion has been used')
        return -1

class Enemy(StatBlock):
    def __init__(self, name = ' ', attack = 0, defense = 0, hp = 0, initiative = 0):
        super().__init__(attack, defense, hp, initiative)
        self._name = name

new_game = False
game_over = False

player1 = ''

enemy_tier = 0
enemy_count = 0
enemy_name = ''

enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

initiative_order = []

def hp_generation(num1):
    return random.randrange(5,11) + num1
 
def attack_generation(num1):
    return (random.randrange(3,11) + num1)

def defense_generation(num1):
    return (random.randrange(3,11) + num1)

def potion_generation(num1):
    pass

def initiative_roll():
    return random.randrange(1,21)

def initiative_check():
    if enemy3._initiative > enemy2._initiative > enemy1._initiative > player1._initiative:
        pass

def enemy_encounter_level():
    global enemy_tier
    enemy_tier = random.randrange(1,11)

def enemy_total():
    global enemy_count
    enemy_count = random.randrange(1,11)

def enemy_selection():
    global enemy_name
    
    if enemy3._hp > 0:
        enemy_select = input('Please choose enemy 1, 2, or 3: ' )
    elif enemy2._hp > 0:
        enemy_select = input('Please choose enemy 1 or 2: ' )
    else:
        enemy_select = input('Please choose enemy 1: ' )

    if enemy_select == 1:
        enemy_name = enemy1
    elif enemy_select == 2:
        enemy_name = enemy2
    else:
        enemy_name = enemy3

    return enemy_name 

def creature_generator(creature):
    
    enemy_encounter_level()

    if enemy_tier > 9:
        creature = Enemy(creature_name(tier3_creatures),attack_generation(10),defense_generation(10),hp_generation(10))

    elif enemy_tier > 7:
        creature = Enemy(creature_name(tier2_creatures),attack_generation(5),defense_generation(5),hp_generation(5))

    else:
        creature = Enemy(creature_name(tier1_creatures),attack_generation(0),defense_generation(0),hp_generation(0))
    
    creature._initiative = initiative_roll()
    return creature
    
def creature_name(tier):
    return tier[random.randrange(0,len(tier))]

def print_stat_block(creature):
    print(f'{creature._name} - HP: {creature._hp} ATK: {creature._attack} DEF: {creature._defense}')

def damage_calc(enemy):
    enemy_decision = 0
    player_choice = input('Would you like to Attack or Defend? ')

    if enemy_decision == 0 and player_choice == 'Attack':
        print('You attacked and they attacked')
        enemy._hp -= player1._attack
        player1._hp -= enemy._attack
    elif enemy_decision == 0 and player_choice == 'Defend':
        print('You defended and they attacked')
        if enemy._attack > player1._defense:
            player1._hp -= (enemy._attack - player1._defense)
        else:
            pass
    elif enemy_decision == 1 and player_choice == 'Attack':
        print('You attacked and they defended')
        if player1._attack > enemy._defense:
            enemy._hp -= (player1._attack - enemy._defense)
        else:
            pass


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

    elif enemy_count > 6:
        enemy1 = creature_generator(enemy1)
        enemy2 = creature_generator(enemy2)
        print(f'You are facing a {enemy1._name} and a {enemy2._name}\n')

    else:
        enemy1 = creature_generator(enemy1)
        print(f'You are facing a {enemy1._name}\n')

def start_new_game():
    global new_game
    global player1

    new_game = True

    print('Thank you for deciding to play! ')

    time.sleep(1)

    player_name = input('Please adventurer, tell me your name? ')

    player1 = Player(player_name)

    time.sleep(1)

    print('Here are your starting stats: ')

    time.sleep(1)

    print_stat_block(player1)

    time.sleep(1)

def combat_sim():
    global player1
    global enemy_name

    if enemy3._hp > 0:
        while (enemy3._hp > 0 or enemy2._hp > 0 or enemy1._hp > 0) and player1._hp > 0:
            enemy_selection()
            damage_calc(enemy_name)
            print(enemy1._hp)
            print(enemy2._hp)
            print(enemy3._hp)
            print(player1._hp)

        print('Enemy3')

    elif enemy2._hp > 0:
        while (enemy2._hp > 0 or enemy1._hp > 0) and player1._hp > 0:
            enemy_selection()
            damage_calc(enemy_name)
            print(enemy1._hp)
            print(enemy2._hp)
            print(player1._hp)
        print('Enemy2')

    elif enemy1._hp > 0:
        while enemy1._hp > 0 and player1._hp > 0:
            enemy_selection()
            damage_calc(enemy_name)
            print(enemy1._hp)
            print(player1._hp)
        print('Enemy1')

player1 = Player('Ted')

player1._initiative = initiative_roll()

creature_party_generator()

combat_sim()






# print('Welcome to Text RPG! ')

# time.sleep(1)

# game_decision = input('Would you like to play? ')

# time.sleep(1)

# while game_decision == 'Yes':

#     start_new_game()

#     while player1._hp > 0:
        
#         creature_party_generator()

#         break

#     break