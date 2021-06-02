
import random
import time


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

new_game = False
game_over = False

player1 = ''

enemy_tier = 0
enemy_count = 0
enemy_name = ''

enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

creature_list = []

def enemy_encounter_level():
    global enemy_tier
    enemy_tier = random.randrange(1,11)

def enemy_total():
    global enemy_count
    enemy_count = random.randrange(1,11)

def enemy_selection():
    global enemy_name
    
    print('')

    if enemy3._hp > 0:
        enemy_select = int(input('Please choose enemy 1, 2, or 3: '))
        print('')

    elif enemy2._hp > 0:
        enemy_select = int(input('Please choose enemy 1 or 2: '))
        print('')

    else:
        enemy_select = 1


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
        creature = Enemy(creature_name(tier3_creatures),random.randrange(10,15),random.randrange(10,15),random.randrange(10,15))

    elif enemy_tier > 7:
        creature = Enemy(creature_name(tier2_creatures),random.randrange(4,9),random.randrange(4,9),random.randrange(4,9))

    else:
        creature = Enemy(creature_name(tier1_creatures),random.randrange(2,6),random.randrange(2,6),random.randrange(2,6))
    
    return creature
    
def creature_name(tier):
    return tier[random.randrange(0,len(tier))]

def print_stat_block(creature):
    print(f'{creature._name} - HP: {creature._hp} ATK: {creature._attack} DEF: {creature._defense}')

def damage_calc(enemy):
    enemy_decision = random.randrange(0,11)

    player_choice = input('Would you like to Attack or Defend? ')
    print('')

    if enemy_decision > 4 and player_choice == 'Attack':
        print(f'You attacked with {player1._attack} and they attacked with {enemy._attack}\n')
        enemy._hp -= player1._attack
        player1._hp -= enemy._attack
    elif enemy_decision > 4 and player_choice == 'Defend':
        print(f'You defended with {player1._defense} and they attacked with {enemy._attack}\n')
        if enemy._attack > player1._defense:
            player1._hp -= (enemy._attack - player1._defense)
        else:
            pass
    elif enemy_decision < 5 and player_choice == 'Attack':
        print(f'You attacked with {player1._attack} and they defended with {enemy._defense}\n')
        if player1._attack > enemy._defense:
            enemy._hp -= (player1._attack - enemy._defense)
        else:
            pass
    else:
        print(f'You Defended with {player1._defense} and they defended with {enemy._defense}\n')

    print_stat_block(enemy)
    print_stat_block(player1)

def creature_party_generator():
    global enemy_count
    global enemy1
    global enemy2
    global enemy3
    global creature_list

    enemy_total()

    print('')

    if enemy_count > 9:
        enemy1 = creature_generator(enemy1)
        enemy2 = creature_generator(enemy2)
        enemy3 = creature_generator(enemy3)
        print(f'You are facing a {enemy1._name}, a {enemy2._name}, and a {enemy3._name}:')
        creature_list.append(enemy1)
        creature_list.append(enemy2)
        creature_list.append(enemy3)

    elif enemy_count > 6:
        enemy1 = creature_generator(enemy1)
        enemy2 = creature_generator(enemy2)
        print(f'You are facing a {enemy1._name} and a {enemy2._name}:')
        creature_list.append(enemy1)
        creature_list.append(enemy2)

    else:
        enemy1 = creature_generator(enemy1)
        print(f'You are facing a {enemy1._name}:')
        creature_list.append(enemy1)

def start_new_game():
    global new_game
    global player1
    global creature_list

    new_game = True

    print('Thank you for deciding to play! \n')

    time.sleep(1)

    player_name = input('Please adventurer, tell me your name? ')

    print('')

    player1 = Player(player_name)

    time.sleep(1)

    stat_increase = input('Which stat would you like to increase?: ')

    print('')

    if stat_increase == 'HP':
        player1._hp += 5
    elif stat_increase == 'Attack':
        player1._attack += 5
    else:
        player1._defense += 5

    time.sleep(1)

    print('Here are your starting stats: \n')

    time.sleep(1)

    print_stat_block(player1)

    time.sleep(1)

def combat_sim():
    global player1
    global enemy_name
    global creature_list

    if enemy3._hp > 0:
        while (enemy3._hp > 0 or enemy2._hp > 0 or enemy1._hp > 0) and player1._hp > 0:
            enemy_selection()
            damage_calc(enemy_name)

    elif enemy2._hp > 0:
        while (enemy2._hp > 0 or enemy1._hp > 0) and player1._hp > 0:
            enemy_selection()
            damage_calc(enemy_name)

    elif enemy1._hp > 0:
        while enemy1._hp > 0 and player1._hp > 0:
            enemy_selection()
            damage_calc(enemy_name)

    creature_list.clear()

start_new_game()

while player1._hp > 0:

    creature_party_generator()

    for creature in creature_list:
        print_stat_block(creature)

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